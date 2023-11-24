from refactorizacion import Calculadora

def main():
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")
    op=input("Introduce la operación a realizar: ")
    if op=="1":
        operacion="suma"
    elif op=="2":
        operacion="resta"
    elif op=="3":
        operacion="multiplicacion"
    elif op=="4":
        operacion="division"
    num1=int(input("Introduce el primer número: "))
    num2=int(input("Introduce el segundo número: "))
    print("El resultado es: ",Calculadora.__dict__[operacion](num1,num2))