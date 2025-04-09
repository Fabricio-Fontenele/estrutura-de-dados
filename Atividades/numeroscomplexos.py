
class NumeroComplexo:
    def __init__(self, real, imaginario):
        if not isinstance(real, (int,float)) or not isinstance(imaginario,(int,float)):
            raise TypeError("Os valores devem ser numeros reais")
        self.real = real
        self.imaginario = imaginario
    
    def summ(self, other):
        new_real = self.real + other.real
        new_imaginario = self.imaginario + other.imaginario
        return NumeroComplexo(new_real, new_imaginario)
        
    def multiply(self, other):
        new_real = (self.real * other.real) - (self.imaginario * other.imaginario)
        new_imaginario = (self.real * other.imaginario) + (self.imaginario * other.real)
        return NumeroComplexo(new_real, new_imaginario)

    def __str__(self):
        sinal = "+" if self.imaginario >= 0 else "-"
        return f"({self.real} {sinal} {abs(self.imaginario)}i)"
    

def main():
    z1 = NumeroComplexo(5,2)
    z2 = NumeroComplexo(3, 1)

    summ = z1.summ(z2)
    multiply = z1.multiply(z2)

    print(f'Soma = {summ}')
    print(f'Multiplicação = {multiply}')
if __name__ == "__main__":
    main()