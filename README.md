# antipatrones

El link a este repositorio es: [github](https://github.com/GonzaloGmv/antipatrones)

El código proporcionado muestra características típicas de "Spaghetti Code" debido a la estructura de control de flujo. Esto es debido a la falta de coherencia en la estructura if y else.

He resuelto el problema de manera eficiente y estructurada utilizando la programación orientada a objetos (POO) en Python y la biblioteca Tkinter para la interfaz gráfica de usuario (GUI). Aquí hay algunas razones por las cuales este enfoque es beneficioso:

Clase Calculadora:

Encapsulación: Al definir una clase Calculadora, se encapsula las operaciones relacionadas en un solo lugar, lo que facilita la organización y mantenimiento del código.

Métodos estáticos: Al definir los métodos suma, resta, multiplicacion, y division como estáticos, se pueden utilizar sin necesidad de instanciar la clase. 

Clase CalculadoraGUI:

Abstracción: La interfaz gráfica está separada de la lógica de cálculo. La clase CalculadoraGUI maneja la interfaz de usuario y llama a la clase Calculadora para realizar las operaciones.

Manejo de eventos: Utiliza eventos de botones para manejar las interacciones del usuario. Esto facilita la extensión de la funcionalidad al agregar nuevos botones o funciones en el futuro.

Validación y manejo de errores: En el método click, se manejan diversos casos, como borrar la pantalla, insertar operadores o números, y realizar cálculos. Además, se manejan errores de manera elegante, mostrando un mensaje de "Error" en la pantalla en caso de una entrada incorrecta.

Primero el código de la clase Calculadora:
```
class Calculadora:
    @staticmethod
    def suma(num1,num2):
        return num1+num2

    @staticmethod
    def resta(num1,num2):
        return num1-num2

    @staticmethod
    def multiplicacion(num1,num2):
        return num1*num2

    @staticmethod
    def division(num1,num2):
        if num2!=0:
            return num1/num2
        else:
            print("No se puede dividir entre cero.")
```

Y este esl código con Tkinter donde se implementa la clase Calculadora en la clase CalculadoraGUI
```
import tkinter as tk
from calculadora_tk.calculadora_calculos import Calculadora

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
```
