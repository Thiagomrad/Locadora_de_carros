from pessoas import Clientes
from datetime import datetime

cliente_um = Clientes('Thiago Silva Tavares','135.987.343-33',23,'Rua das Palmeiras',32_98768_3736,73556256,2024)
cliente_dois = Clientes('Lucas Macedo Gomes','145.988.246-43',27,'Rua dos Almirantes',32_99832_7521,68456736,2025)

clientes:list[Clientes] = []

def adicionar_cliente(cliente:Clientes):
    verificador = True
    if cliente.idade < 18:
        verificador = False
        return('Idade inferior ao mínimo exigido por lei')
    if cliente.ano_vencimento_carteira_motorista < datetime.now().year:
        verificador = False
        return('Data da carteira de motorista vencida')
    if verificador == True:
        clientes.append(cliente)

adicionar_cliente(cliente_um)
adicionar_cliente(cliente_dois)