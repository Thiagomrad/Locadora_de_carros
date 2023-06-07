from pessoas import Clientes
from veiculos import VeiculosUtilitarios,VeiculosEsportivos
from datetime import datetime

class Reserva:
    def __init__(self,codigo: int,cliente: Clientes,veiculo: VeiculosUtilitarios | VeiculosEsportivos,data_inicio: datetime,data_fim: datetime ,status = True):
        self.codigo = codigo
        self.cliente = cliente
        self.data_inicio = data_inicio
        self.data_fim = data_fim
        self.status = status
        self.veiculo = veiculo

    @property
    def prazo(self):
        return self.data_fim - self.data_inicio

    @property
    def ativar(self):
        if self.status is False:
            self.status = True
    
    @property
    def desativar(self):
        if self.status is True:
            self.status = False
    
    @property
    def tipo_veiculo(self):
        return type(self.veiculo)