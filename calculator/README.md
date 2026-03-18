Kids Calculator - Project Description
This is a comprehensive, professional-grade calculator built in Python, designed as a practice project for beginners with knowledge of loops, variables, and OOP. It's tailored for integration into a kids' learning platform, providing an honest, efficient, and extensible tool for educational math activities. The calculator supports full mathematical expressions with basic and advanced operations, ensuring safety through restricted evaluation (no raw eval() vulnerabilities). It's modular, with a pure logic core separated from interfaces (CLI and GUI), making it easy to reuse in larger projects like web apps or desktop tools.
The project emphasizes best practices: PEP 8 styling, type hints, docstrings, error handling, and Git versioning. All operations are O(1) efficient, with bounded history to prevent memory issues. Built with Python's standard library (plus Tkinter for GUI), no external dependencies are required.
This calculator can handle kid-friendly tasks like simple addition for early learners to trigonometry for older kids, with colorful, intuitive interfaces.
Features List

Core Operations:
Basic arithmetic: +, -, *, /, %, exponents (via pow or **).
Advanced functions: sqrt, log (natural), log10, exp, factorial, combinations (comb), permutations (perm).
Trigonometric: sin, cos, tan, asin, acos, atan (with hyperbolic: sinh, cosh, tanh).
Constants: pi, e, tau.
Angle mode toggle: Degrees (DEG) or Radians (RAD), with automatic conversion.
Full expression parsing: Supports parentheses, precedence (e.g., 2 + 3 * sin(30)).

Safety and Reliability:
Safe evaluation using a restricted namespace (only approved math functions; blocks dangerous built-ins).
Comprehensive error handling: Catches division by zero, invalid syntax, etc., with user-friendly messages.
Rounded results to avoid floating-point noise (e.g., 0.1 + 0.2 = 0.3).

Additional Tools:
Calculation history: Stores up to 20 recent expressions and results (accessible and clearable).
Memory functions: Store (MS), recall (MR), add (M+), subtract (M-), clear (MC) – like real calculators.

Interfaces:
CLI: Text-based for quick testing, with commands like 'history', 'mode deg/rad'.
GUI: Kid-friendly Tkinter interface with big colorful buttons, large fonts, history panel, and emojis for fun.

Extensibility:
Modular design: Core logic is standalone and testable.
Easy to add features like fractions (via fractions module) or symbolic math (via sympy).

Performance:
Efficient: No heavy computations; suitable for real-time use in learning apps.
Cross-platform: Runs on Windows, Mac, Linux.


Installation

Clone the repository:textgit clone https://github.com/yourusername/kids_calculator.git
cd kids_calculator
Set up a virtual environment (recommended):textpython -m venv venv
# Activate (Windows): venv\Scripts\activate
# Activate (Mac/Linux): source venv/bin/activate
No additional installs needed – uses Python standard library.

Usage
Running the Calculator

CLI mode:textpython main.py  # Or switch to CLI in the fileEnter expressions like 2 + 3 * 4 or commands like history.
GUI mode:textpython main.py  # Uncomment the GUI lineClick buttons to build expressions; results appear in the display.

Example: Using the Core in Code
Import and use the calculator core directly:
Pythonfrom calculator.core import Calculator

# Initialize
calc = Calculator()
calc.set_angle_mode("deg")  # Optional: switch to degrees (default)

# Calculate an expression
try:
    result = calc.calculate("2 + 3 * sin(30) + pi")
    print(f"Result: {result}")  # Output: Result: 6.6415926536
except ValueError as e:
    print(f"Error: {e}")

# Access history
print(calc.get_history())  # List of past calculations

# Memory example
calc.memory_add(result)
print(calc.memory_recall())  # Retrieves stored value
This snippet demonstrates safe, full-expression evaluation with advanced functions.
How to Integrate into Learning Platform
This calculator is designed for seamless integration into your larger kids' learning platform (e.g., a web-based app, desktop tool, or mobile wrapper). The core is fully decoupled from UIs, so you can use it without the CLI or GUI.

Copy the Package:
Copy the entire calculator/ folder (including __init__.py, core.py, etc.) into your platform's project root or a libs/ subfolder.

Import and Use:
In any file (e.g., a lesson module or API endpoint):Pythonfrom calculator.core import Calculator  # Adjust path if in subfolder: from libs.calculator.core import Calculator

calc = Calculator()  # Create instance (stores state like history/memory)

# In a user interaction (e.g., button click or form submit):
user_input = "3 * 4 + sin(30)"  # From kid's input field
try:
    result = calc.calculate(user_input)
    # Display: f"Wow! The answer is {result} 🎉"
    # Save progress: calc.get_history()
except ValueError:
    # Friendly feedback: "Oops! Check your expression and try again! 😊"

Customization for Your Platform:
Web (Flask/Django/Streamlit): Call calc.calculate() in a route or view; return JSON for frontend display.
Desktop (Tkinter/Kivy): Subclass CalculatorGUI or embed the core in your main app.
Mobile (BeeWare/Kivy): Use the core logic; build a custom touch interface.
Add kid-specific features: Integrate with lessons (e.g., auto-explain basic ops), sounds for correct answers, or limit to age-appropriate functions.

Testing Integration:
Write unit tests: e.g., assert calc.calculate("1+1") == 2.0.
Ensure the venv is activated in your platform for consistency.


This setup keeps your platform clean – the calculator adds value without bloat.
Testing

Run core tests in Python REPL or a script:Pythonfrom calculator.core import Calculator
calc = Calculator()
assert calc.calculate("2 + 3 * 4") == 14.0
calc.set_angle_mode("deg")
assert calc.calculate("sin(30)") == 0.5
Edge cases: Try 1/0 (should raise ValueError), invalid names, empty strings.

Contributing
Fork the repo, create a branch (git checkout -b feature/new-op), add changes, commit, and PR. Follow PEP 8 and add docstrings/tests.



License
MIT License – free to use, modify, and distribute.