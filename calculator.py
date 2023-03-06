import tkinter as tk

class CalculatorGUI:
    def __init__(self, master):
        self.master = master
        master.title("Calculator")

        self.display = tk.Entry(master, width=30, justify="right")
        self.display.grid(row=0, column=0, columnspan=4, padx=5, pady=5)

        buttons = [
            "7", "8", "9", "/",
            "4", "5", "6", "*",
            "1", "2", "3", "-",
            "0", ".", "C", "+",
            "="
        ]

        row = 2
        col = 0

        for button_text in buttons:
            button = tk.Button(master, text=button_text, width=5, height=2,
                               command=lambda text=button_text: self.button_click(text))
            button.grid(row=row, column=col, padx=5, pady=5)

            col += 1

            if col > 3:
                col = 0
                row += 1

    def button_click(self, text):
        if text == "C":
            self.display.delete(0, tk.END)
        elif text == "=":
            try:
                result = str(eval(self.display.get()))
                self.display.delete(0, tk.END)
                self.display.insert(0, result)
            except:
                self.display.delete(0, tk.END)
                self.display.insert(0, "Error")
        else:
            self.display.insert(tk.END, text)

root = tk.Tk()
app = CalculatorGUI(root)
root.mainloop()
