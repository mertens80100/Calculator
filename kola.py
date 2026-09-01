"""Tkinter interface for the arithmetic calculator."""

from calculator import CalculationError, calculate_expression


def main():
    # Keeping Tk initialization here allows tests to import this module headlessly.
    import tkinter as tk

    window = tk.Tk()
    window.title("Arithmetic Calculator")
    expression = tk.StringVar()
    status = tk.StringVar()
    entry = tk.Entry(window, textvariable=expression, font=("Arial", 24), width=20)
    entry.grid(row=0, column=0, columnspan=4, padx=8, pady=8, sticky="ew")

    def append(value):
        status.set("")
        expression.set(expression.get() + value)

    def calculate(event=None):
        try:
            result = calculate_expression(expression.get())
        except CalculationError as error:
            status.set(str(error))
        else:
            expression.set(str(result))
            status.set("")

    def clear(event=None):
        expression.set("")
        status.set("")

    keys = ["7", "8", "9", "/", "4", "5", "6", "*", "1", "2", "3", "-", "0", ".", "=", "+"]
    for index, key in enumerate(keys):
        action = calculate if key == "=" else lambda value=key: append(value)
        tk.Button(window, text=key, font=("Arial", 18), command=action).grid(
            row=index // 4 + 1, column=index % 4, padx=2, pady=2, sticky="nsew"
        )
    tk.Button(window, text="Clear", command=clear).grid(row=5, column=0, columnspan=4, sticky="ew")
    tk.Label(window, textvariable=status, foreground="#a40000", wraplength=340).grid(
        row=6, column=0, columnspan=4, padx=8, pady=8
    )
    for column in range(4):
        window.columnconfigure(column, weight=1)
    window.bind("<Return>", calculate)
    window.bind("<Escape>", clear)
    entry.focus_set()
    window.mainloop()


if __name__ == "__main__":
    main()
