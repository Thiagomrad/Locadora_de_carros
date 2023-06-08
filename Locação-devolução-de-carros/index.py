from reserva import Reserva
from veiculos import VeiculosEsportivos,VeiculosUtilitarios
from pessoas import Clientes
from datetime import datetime,timedelta

# Reserva

dia_inicio = 8
mes_inicio = 6
ano_inicio = 2023
dias_locacao = 5
data_inicio = datetime(ano_inicio,mes_inicio,dia_inicio)
data_fim = data_inicio + timedelta(days= dias_locacao)