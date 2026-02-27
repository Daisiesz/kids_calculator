import tkinter as tk
from tkinter import messagebox, ttk
from .core import Calculator

class CalculatorGUI():
    def __init__(self):
        self.calc = Calculator()
        self.root = tk.Tk()
        self.root.title("🧠 Kids Math Calculator")
        self.root.geometry("500x700")
        self.root.configure(bg="#f0f8ff")  # Light fun background
        self.root.resizable(False, False)

        # Display
        self.display = tk.Entry(self.root, font=("Arial", 24), justify="right", bd=10)
        self.display.grid(row=0, column=0, columnspan=5, padx=10, pady=20, sticky="ew")

        # History
        history_frame = ttk.LabelFrame(self.root, text="History")
        history_frame.grid(row=1, column=4, rowspan=6, padx=5, pady=5, sticky="ns")
        self.history_list = tk.Listbox(history_frame, width=25, height=15)
        self.history_list.pack(padx=5, pady=5)

        # Buttons frame
        btn_frame = tk.Frame(self.root, bg="#f0f8ff")
        btn_frame.grid(row=2, column=0, columnspan=4, padx=10, pady=10)

        # Example button creation helper
        def create_btn(text: str, row: int, col: int, color="#ffffff", colspan=1, command=None):
            btn = tk.Button(
                btn_frame, text=text, font=("Arial", 18, "bold"),
                bg=color, fg="black", height=2, width=6 if colspan==1 else 12,
                command=command or (lambda: self._button_click(text))
            )
            btn.grid(row=row, column=col, columnspan=colspan, padx=2, pady=2, sticky="nsew")

        # Basic buttons (expand this grid to your liking)
        buttons = [
            ("C", 0, 0, "#ff9999"), ("(", 0, 1), (")", 0, 2), ("/", 0, 3, "#ffe699"),
            ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("*", 1, 3, "#ffe699"),
            ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("-", 2, 3, "#ffe699"),
            ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("+", 3, 3, "#ffe699"),
            ("0", 4, 0, "#ffffff", 2), (".", 4, 2), ("=", 4, 3, "#99ff99"),
            # Add scientific row
            ("sin", 5, 0, "#ccffcc"), ("cos", 5, 1, "#ccffcc"), ("tan", 5, 2, "#ccffcc"), ("log", 5, 3, "#ccffcc"),
            # Memory & mode
            ("M+", 0, 4, "#d1e7ff"), ("MR", 1, 4, "#d1e7ff"), ("DEG", 6, 0, "#ffd1dc", 2, lambda: self._toggle_mode()),
        ]

        for btn in buttons:
            create_btn(*btn)

        # Configure grid weights
        for i in range(5):
            btn_frame.columnconfigure(i, weight=1)
            btn_frame.rowconfigure(i, weight=1)

        # Bind Enter key
        self.root.bind("<Return>", lambda e: self._calculate_result())

        self.root.mainloop()

    def _button_click(self, value: str):
        if value == "=":
            self._calculate_result()
        elif value == "C":
            self.display.delete(0, tk.END)
        else:
            self.display.insert(tk.END, value)

    def _calculate_result(self):
        expr = self.display.get().strip()
        if not expr:
            return
        try:
            result = self.calc.calculate(expr)
            self.display.delete(0, tk.END)
            self.display.insert(0, str(result))
            # Update history
            self.history_list.delete(0, tk.END)
            for entry in self.calc.get_history():
                self.history_list.insert(0, entry)
        except ValueError as e:
            messagebox.showerror("Oops! 👀", str(e))
            self.display.delete(0, tk.END)

    def _toggle_mode(self):
        new_mode = "rad" if self.calc.angle_mode == "deg" else "deg"
        self.calc.set_angle_mode(new_mode)
        # You could update a label here

if __name__ == "__main__":
    CalculatorGUI()