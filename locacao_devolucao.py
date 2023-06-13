from datetime import datetime,timedelta
from cadastro_veiculos import utilitario,esportivo
from cadastro_clientes import clientes
from reserva import Reserva


modelo_veiculo = input('Digite o modelo do veículo: ')
nome_cliente = input('Digite o nome do cliente: ')

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
            return cliente
    return False

#verificar se carro está cadastrado

def verificar_veiculo(modelo):
    for veiculo in utilitario:
        if veiculo.modelo == modelo:
            return veiculo
    for veiculo in esportivo:
        if veiculo.modelo == modelo:
            return veiculo
    return False

#criar uma reserva
# colocar o veiculo e o cliente em uma variavel

reservas: list[Reserva] = []
veiculo_verificado = verificar_veiculo(modelo_veiculo)
cliente_verificado = verificar_cliente(nome_cliente)


if cliente_verificado is not False and veiculo_verificado is not False:
    reserva_um = Reserva(1001,cliente_verificado,veiculo_verificado,data_inicio,data_fim)
    reservas.append(reserva_um)

for reserva in reservas:
    print(reserva)
    print('Data inicial: ',reserva.data_inicio.strftime('%d/%m/%Y'))
    print('Data final: ',data_fim.strftime('%d/%m/%Y'))