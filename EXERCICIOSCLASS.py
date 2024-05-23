class exercicios:
    def __init__(self, nome, idade, salario, cargo, turno, setor):
        self.nome = nome
        self.idade = idade
        self.salario = salario
        self.cargo = cargo
        self.turno = turno
        self.setor = setor
    def informacoes(self):
        print("Informações:")
        print("Nome:", self.nome)
        print("Idade:", self.idade)
        print("Salário:", self.salario)
        print("Cargo:", self.cargo)
        print("Turno:", self.turno)
        print("Setor:", self.setor)
        nome_funcionario = "amora"
        idade_funcionario = 22
        salario_funcionario = 3000.00
        cargo_funcionario = "advogada"
        turno_funcionario = "Matutino"
        setor_funcionario = "direitopenal"
        
        funcionario = Exercicios(nome_funcionario, idade_funcionario, salario_funcionario, cargo_funcionario, turno_funcionario, setor_funcionario)
        funcionario.exibir_informacoes()
