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