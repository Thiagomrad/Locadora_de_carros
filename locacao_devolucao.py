from datetime import datetime,timedelta
from cadastro_veiculos import utilitario,esportivo

# Reserva

dia_inicio = 8
mes_inicio = 6
ano_inicio = 2023
dias_locacao = 5
data_inicio = datetime(ano_inicio,mes_inicio,dia_inicio)
data_fim = data_inicio + timedelta(days= dias_locacao)

# teste temporário

for veiculo in utilitario:
    print(veiculo.modelo)
for veiculo in esportivo:
    print(veiculo.modelo)