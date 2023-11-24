import tkinter as tk
from calculadora.calculadora_calculos import Calculadora

class CalculadoraGUI:
    def __init__(self, master):
        self.master = master
        master.title("Calculadora")

        self.entry = tk.Entry(master, width=20, font=('Arial', 14))
        self.entry.grid(row=0, column=0, columnspan=4)

        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', 'C', '=', '+'
        ]

        row_val = 1
        col_val = 0

        for button in buttons:
            tk.Button(master, text=button, width=5, height=2, command=lambda b=button: self.click(b)).grid(row=row_val, column=col_val)
            col_val += 1
            if col_val > 3:
                col_val = 0
                row_val += 1
    
    def calcular(self, operacion, num1, num2):
        if operacion == '+':
            return Calculadora.suma(num1, num2)
        elif operacion == '-':
            return Calculadora.resta(num1, num2)
        elif operacion == '*':
            return Calculadora.multiplicacion(num1, num2)
        elif operacion == '/':
            return Calculadora.division(num1, num2)

    def click(self, button):
        current_entry = self.entry.get()

        if button == 'C':
            self.entry.delete(0, tk.END)
        elif button in {'+', '-', '*', '/'}:
            self.entry.insert(tk.END, ' ' + button + ' ')
        elif button == '=':
            try:
                num1, operacion, num2 = current_entry.split()
                num1, num2 = float(num1), float(num2)
                result = self.calcular(operacion, num1, num2)
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, str(result))
            except:
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, "Error")
        else:
            self.entry.insert(tk.END, button)