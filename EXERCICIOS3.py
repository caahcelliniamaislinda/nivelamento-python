class Exercicios:
    def calcular_expressoes(self):
        valor1 = 10
        valor2 = 5
        valor3 = "2"
        valor4 = 8
        valor5 = -5
        
        # Calculando e mostrando cada caso
        print("Valor1 + Valor2:", valor1 + valor2)
        print("Valor1 + Valor2 + Valor4:", valor1 + valor2 + valor4)
        print("Valor1 + Valor2 - Valor5:", valor1 + valor2 - valor5)
        print("Valor1 + Valor3 (concatenação):", str(valor1) + valor3)
        print("Valor1 * Valor2:", valor1 * valor2)
        print("(Valor4 * Valor2) / 2:", (valor4 * valor2) / 2)
        print("(Valor1 + Valor2 + Valor4 + Valor5) / 4:", (valor1 + valor2 + valor4 + valor5) / 4)
        ex = Exercicios()
        ex.calcular_expressoes()


