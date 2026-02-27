import math
from typing import List, Optional

class Calculator():
    """Professional, comprehensive calculator core.
    Supports full expressions, scientific ops, history, memory, DEG/RAD mode.
    Safe evaluation - only math functions allowed.
    """

    def __init__(self):
        self.history: List[str] = []          # Last 20 calculations
        self.memory: float = 0.0
        self.angle_mode: str = "deg"          # "deg" or "rad"

    def set_angle_mode(self, mode: str) -> None:
        """Switch between degrees and radians."""
        if mode.lower() in ("deg", "rad"):
            self.angle_mode = mode.lower()
        else:
            raise ValueError("Mode must be 'deg' or 'rad'")

    def get_safe_dict(self) -> dict:
        """Build restricted namespace for safe eval (best practice)."""
        is_deg = self.angle_mode == "deg"

        def make_trig(func, inverse: bool = False):
            if inverse:
                def wrapper(x: float) -> float:
                    res = func(x)
                    return math.degrees(res) if is_deg else res
                return wrapper
            else:
                def wrapper(x: float) -> float:
                    arg = math.radians(x) if is_deg else x
                    return func(arg)
                return wrapper

        safe_dict = {
            # Trigonometric
            "sin": make_trig(math.sin),
            "cos": make_trig(math.cos),
            "tan": make_trig(math.tan),
            "asin": make_trig(math.asin, inverse=True),
            "acos": make_trig(math.acos, inverse=True),
            "atan": make_trig(math.atan, inverse=True),
            # Hyperbolic (optional but comprehensive)
            "sinh": make_trig(math.sinh),
            "cosh": make_trig(math.cosh),
            "tanh": make_trig(math.tanh),
            # Other advanced
            "sqrt": math.sqrt,
            "log": math.log,      # natural log
            "log10": math.log10,
            "exp": math.exp,
            "factorial": math.factorial,
            "comb": math.comb,    # nCr (Python 3.8+)
            "perm": math.perm,    # nPr
            "degrees": math.degrees,
            "radians": math.radians,
            # Constants
            "pi": math.pi,
            "e": math.e,
            "tau": math.tau,
            # Built-ins we want
            "abs": abs,
            "round": round,
            "pow": pow,
        }
        return safe_dict

    def calculate(self, expression: str) -> float:
        """Main method: evaluate any math expression safely.
        Example: '2 + 3 * sin(30)' → 3.5 (in deg mode)
        """
        if not expression.strip():
            raise ValueError("Empty expression")

        try:
            safe_dict = self.get_safe_dict()
            result: float = eval(
                expression,
                {"__builtins__": {}},   # Block dangerous built-ins
                safe_dict
            )
            # Round for clean display (avoids float noise like 0.1+0.2)
            result = round(float(result), 10)
            self._add_to_history(expression, result)
            return result
        except (ZeroDivisionError, ValueError, TypeError, SyntaxError, NameError) as e:
            raise ValueError(f"Invalid expression: {str(e)}") from e
        except Exception as e:  # Catch-all for safety
            raise ValueError(f"Calculation error: {str(e)}") from e

    def _add_to_history(self, expr: str, result: float) -> None:
        entry = f"{expr} = {result}"
        self.history.append(entry)
        if len(self.history) > 20:
            self.history.pop(0)

    def get_history(self) -> List[str]:
        """Return calculation history (newest first)."""
        return self.history[::-1]

    def clear_history(self) -> None:
        self.history.clear()

    # Memory functions (like real calculators)
    def memory_store(self, value: Optional[float] = None) -> None:
        self.memory = value if value is not None else 0.0

    def memory_recall(self) -> float:
        return self.memory

    def memory_add(self, value: float) -> None:
        self.memory += value

    def memory_subtract(self, value: float) -> None:
        self.memory -= value

    def memory_clear(self) -> None:
        self.memory = 0.0