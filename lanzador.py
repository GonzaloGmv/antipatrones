import tkinter as tk
from calculadora_tk.calculadora_grafica import CalculadoraGUI

def main():
    root = tk.Tk()
    app = CalculadoraGUI(root)
    root.mainloop()