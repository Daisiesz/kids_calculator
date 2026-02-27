from .core import Calculator

def run_cli():
    calc = Calculator()
    print("Kids Calculator CLI - Type 'quit' to exit, 'history', 'mode deg/rad', 'mem' commands")
    
    while True:
        try:
            expr = input("\nEnter expression: ").strip()
            if expr.lower() in ("quit", "exit"):
                break
            elif expr.lower() == "history":
                print("\n".join(calc.get_history()) or "No history yet")
                continue
            elif expr.lower().startswith("mode "):
                mode = expr.split()[1]
                calc.set_angle_mode(mode)
                print(f"Angle mode set to {mode.upper()}")
                continue
            # Memory shortcuts: m+ 5, mr, etc. (add more if you want)
            
            result = calc.calculate(expr)
            print(f"Result: {result}")
        except ValueError as e:
            print(f"❌ {e}")
        except Exception as e:
            print(f"Unexpected error: {e}")

if __name__ == "__main__":
    run_cli()