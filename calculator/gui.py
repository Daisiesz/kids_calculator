import tkinter as tk
from tkinter import messagebox, ttk
from .core import Calculator

class CalculatorGUI:
    def __init__(self):
        self.calc = Calculator()
        self.root = tk.Tk()
        self.root.title("🧠 Kids Math Calculator")
        self.root.geometry("680x820")           # Bigger, more comfortable size
        self.root.configure(bg="#f0f8ff")
        self.root.resizable(True, True)

        # ==================== DISPLAY (Fixed & Prominent) ====================
        self.display = tk.Entry(
            self.root,
            font=("Arial", 32, "bold"),         # Big bold text — visible immediately
            justify="right",
            bd=15,
            relief="sunken",
            bg="#ffffff"
        )
        self.display.grid(row=0, column=0, columnspan=5, padx=20, pady=30, sticky="ew")

        # ==================== HISTORY ====================
        history_frame = ttk.LabelFrame(self.root, text="History")
        history_frame.grid(row=1, column=4, rowspan=8, padx=10, pady=10, sticky="ns")
        self.history_list = tk.Listbox(history_frame, width=30, height=20, font=("Arial", 10))
        self.history_list.pack(padx=8, pady=8, fill="both", expand=True)

        # ==================== BUTTONS FRAME ====================
        btn_frame = tk.Frame(self.root, bg="#f0f8ff")
        btn_frame.grid(row=2, column=0, columnspan=4, padx=15, pady=10, sticky="nsew")

        # Make everything stretch nicely
        self.root.columnconfigure(0, weight=1)
        self.root.columnconfigure(1, weight=1)
        self.root.columnconfigure(2, weight=1)
        self.root.columnconfigure(3, weight=1)
        self.root.columnconfigure(4, weight=0)   # History column doesn't stretch

        for i in range(5):
            btn_frame.columnconfigure(i, weight=1)
        for i in range(10):                      # More rows for future buttons
            btn_frame.rowconfigure(i, weight=1)

        # Button creator helper
        def create_btn(text: str, row: int, col: int, color="#f8f9fa", colspan=1, rowspan=1, command=None):
            btn = tk.Button(
                btn_frame,
                text=text,
                font=("Arial", 18, "bold"),
                bg=color,
                fg="black",
                height=2,
                relief="raised",
                command=command or (lambda t=text: self._button_click(t))
            )
            btn.grid(row=row, column=col, columnspan=colspan, rowspan=rowspan,
                     padx=4, pady=4, sticky="nsew")

        # ==================== BUTTONS LAYOUT ====================
        buttons = [
            # Row 0
            ("C", 0, 0, "#ff6b6b"), ("(", 0, 1), (")", 0, 2), ("/", 0, 3, "#ffd166"),
            ("M+", 0, 4, "#a2d2ff"),
            # Row 1
            ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("*", 1, 3, "#ffd166"), ("MR", 1, 4, "#a2d2ff"),
            # Row 2
            ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("-", 2, 3, "#ffd166"),
            # Row 3
            ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("+", 3, 3, "#ffd166"),
            # Row 4
            ("0", 4, 0, "#f8f9fa", 2), (".", 4, 2), ("=", 4, 3, "#06d6a0", 1, 2),
            # Scientific row
            ("sin", 5, 0, "#b5e8cf"), ("cos", 5, 1, "#b5e8cf"), ("tan", 5, 2, "#b5e8cf"), ("log", 5, 3, "#b5e8cf"),
            # Mode
            ("DEG", 6, 0, "#ff9ebb", 2, 1, self._toggle_mode),
        ]

        for btn in buttons:
            create_btn(*btn)

        # Bind Enter key for keyboard input
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
        # You can add a label later to show current mode

if __name__ == "__main__":
    CalculatorGUI()