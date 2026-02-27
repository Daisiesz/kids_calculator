try:
	from calculator.core import Calculator
except ModuleNotFoundError:
	# Allow running this file directly from inside the `calculator` folder
	import sys
	from pathlib import Path

	sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
	from calculator.core import Calculator


calc = Calculator()
print(calc.calculate("2 + 3 * 4"))          
calc.set_angle_mode("deg")
print(calc.calculate("sin(30) + pi"))       
print(calc.get_history())