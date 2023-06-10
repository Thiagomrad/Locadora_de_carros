from datetime import datetime,timedelta
from cadastro_veiculos import utilitario,esportivo
from cadastro_clientes import clientes
from reserva import Reserva


nome_cliente = input('Digite o nome do cliente: ')
modelo_veiculo = input('Digite o modelo do veículo: ')

dia_inicio = 8
mes_inicio = 6
ano_inicio = 2023
dias_locacao = 5
data_inicio = datetime(ano_inicio,mes_inicio,dia_inicio)
data_fim = data_inicio + timedelta(days= dias_locacao)

#verificar se cliente está cadastrado
def verificar_cliente(nome):
    for cliente in clientes:
        if cliente.nome == nome:
            return True
    return False

#verificar se carro está cadastrado

def verificar_veiculo(modelo):
    for veiculo in utilitario:
        if veiculo.modelo == modelo:
            return True
    for veiculo in esportivo:
        if veiculo.modelo == modelo:
            return True
    return False

#criar uma reserva
# colocar o veiculo e o cliente em uma variavel

reservas: list[Reserva] = []
verificar_veiculo_um = verificar_veiculo(nome_cliente)
verificar_cliente_um = verificar_cliente(modelo_veiculo)

'''
if verificar_cliente_um is True and verificar_veiculo_um is True:
    reservas.append(
        Reserva
    )
'''