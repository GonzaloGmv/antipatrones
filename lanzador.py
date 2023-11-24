import tkinter as tk
from calculadora.calculadora_grafica import CalculadoraGUI

def main():
    root = tk.Tk()
    app = CalculadoraGUI(root)
    root.mainloop()