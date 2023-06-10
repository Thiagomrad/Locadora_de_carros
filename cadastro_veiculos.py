from veiculos import VeiculosEsportivos, VeiculosUtilitarios

#Utilitários

uno = VeiculosUtilitarios('GRG-2000',2006,'Prata','Uno',110000,60.00,5,2.2,8.2)
celta= VeiculosUtilitarios('BTU-1750',2003,'Preto','Celta',135120,50.00,5,1.8,7.6)
gol = VeiculosUtilitarios('DSI-6226',2010,'Vermelho','Gol-G5',90122,70.00,5,2.0,8.5)

#esportivos

citroen_c4 = VeiculosEsportivos('CSL-2241',2015,'Prata','C4 Lounge Tendance',60213,120.00,214,8.8,'motor v8')
mercedes = VeiculosEsportivos('TRI-7365',2008,'Preto','Mercedes-Benz C200 Kompressor Classic',96523,130.00,225,9,'Trasmissão melhorada')

#Lists

esportivo:list[VeiculosEsportivos] = []
utilitario:list[VeiculosUtilitarios] = []

def cadastrar_veiculo(veiculo:VeiculosEsportivos | VeiculosUtilitarios):
    try:
        if type(veiculo) == VeiculosUtilitarios:
            utilitario.append(veiculo)
        else:
            esportivo.append(veiculo)
    except TypeError:
        'Não é um tipo de veículo'

cadastrar_veiculo(uno)
cadastrar_veiculo(celta)
cadastrar_veiculo(gol)
cadastrar_veiculo(citroen_c4)
cadastrar_veiculo(mercedes)
        
    
