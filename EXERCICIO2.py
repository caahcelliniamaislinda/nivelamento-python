class Exercicios:
    def __init__(self, nome_escola, estado, num_professores, cidade, num_militares, logradouro, numero, num_alunos, colegio_militar, disciplinas):
        self.nome_escola = nome_escola
        self.estado = estado
        self.num_professores = num_professores
        self.cidade = cidade
        self.num_militares = num_militares
        self.logradouro = logradouro
        self.numero = numero
        self.num_alunos = num_alunos
        self.colegio_militar = colegio_militar
        self.disciplinas = disciplinas
    def exibir_informacoes_escola(self):
        print("Informações da Escola:")
        print("Nome da Escola:", self.nome_escola)
        print("Estado:", self.estado)
        print("Número de Professores:", self.num_professores)
        print("Cidade:", self.cidade)
        print("Número de Militares:", self.num_militares)
        print("Logradouro:", self.logradouro)
        print("Número:", self.numero)
        print("Número de Alunos:", self.num_alunos)
        print("Colégio Militar?", "Sim" if self.colegio_militar else "Não")
        print("Disciplinas:", ", ".join(self.disciplinas))
        nome_escola = "Colégio Militar de Brasília"
        estado = "Distrito Federal"
        num_professores = 50
        cidade = "Brasília"
        num_militares = 20
        logradouro = "SGAN 905"
        numero = "Asa Norte"
        num_alunos = 1000
        colegio_militar = True
        disciplinas = ["Matemática", "Português", "História", "Física"]
        escola = Exercicios(nome_escola, estado, num_professores, cidade, num_militares, logradouro, numero, num_alunos, colegio_militar, disciplinas)
        escola.exibir_informacoes_escola()

    


