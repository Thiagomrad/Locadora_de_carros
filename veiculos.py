class Veiculos:
    def __init__(self,placa: str,ano: int,cor: str,modelo: str,quilometragem: float,valor_diario:float):
        self.placa = placa
        self.ano = ano
        self.cor = cor
        self.modelo = modelo
        self.quilometragem = quilometragem
        self.valor_diario = valor_diario
    
class VeiculosEsportivos(Veiculos):
    def __init__(self, placa: str, ano: int, cor: str, modelo: str, quilometragem: float, valor_diario: float, velocidade: float, tempo_100_km_hora:float,*melhorias):
        super().__init__(placa, ano, cor, modelo, quilometragem, valor_diario)
        self.velocidade = velocidade
        self.tempo_100_km_hora = tempo_100_km_hora
        self.melhorias = list(melhorias)
    
class VeiculosUtilitarios(Veiculos):
    def __init__(self, placa: str, ano: int, cor: str, modelo: str, quilometragem: float, valor_diario: float,quantidade_de_passageiros: int, tamanho_bagageiro: float, km_por_litro: float):
        super().__init__(placa, ano, cor, modelo, quilometragem, valor_diario)
        self.quantidade_de_passageiros = quantidade_de_passageiros
        self.tamanho_bagageiro = tamanho_bagageiro
        self.km_por_litro = km_por_litro

    
    


