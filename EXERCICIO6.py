class Exercicios:
    def verificar_aprovacao(self):
        nota1 = 64
        nota2 = 45
        nota3 = 60
        
        # Calculando a média das notas
        media = (nota1 + nota2 + nota3) / 3
        
        # Verificando se o aluno está aprovado com certificado, apenas aprovado ou reprovado
        if media >= 90:
            print("O aluno foi aprovado com certificado!")
        elif media >= 60:
            print("O aluno está aprovado!")
        else:
            print("O aluno está reprovado.")

# Chamada do método para verificar a aprovação
ex = Exercicios()
ex.verificar_aprovacao()