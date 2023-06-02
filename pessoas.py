class Pessoas:
    def __init__(self,nome: str,cpf: str,idade: int,endereco: str,telefone: int):
        self.nome = nome
        self.cpf = cpf
        self.idade = idade
        self.endereco = endereco
        self.telefone = telefone

class Funcionarios(Pessoas):
    def __init__(self, nome: str, cpf: str, idade: int, endereco: str, telefone: int, salario: float, numero_de_alugueis: int, status:bool = True ):
       super().__init__(nome, cpf, idade, endereco, telefone)
       self.salario = salario
       self.numero_de_alugueis = numero_de_alugueis
       self._status = status

    @property
    def status(self):
        if self._status == True:
            return 'Ativado'
        return 'Desativado'

    @property
    def ativar(self):
        if self._status == False:
            self._status = True
    
    @property
    def desativar(self):
        if self._status == True:
            self._status = False
    
class Clientes(Pessoas):
    def __init__(self, nome: str, cpf: str, idade: int, endereco: str, telefone: int, numero_carteira_motorista: int):
        super().__init__(nome, cpf, idade, endereco, telefone)
        self.numero_carteira_motorista = numero_carteira_motorista

    

    