class Veiculo:
    def __init__(self, marca, qtdRodas, modelo, velocidade):
        self.marca = marca
        self.qtdRodas = qtdRodas
        self.modelo = modelo
        self.velocidade = velocidade
    def imprimirInformacoes(self):
        print("Marca:", self.marca, "\n Quantidade de rodas:", self.qtdRodas,
              "\n Modelo:", self.modelo, "\n Velocidade:", self.velocidade)
    def acelerar(self):
        valoracelerar = int(input("O quanto o veículo deve acelerar?"))
        self.velocidade = self.velocidade + valoracelerar
    def freio(self):
        self.velocidade = 0


class Bicicleta(Veiculo):
    def __init__(self, marca, qtdRodas, modelo, velocidade, numMarchas, bagageiro):
        
        self.numMarchas = numMarchas
        self.bagageiro = bagageiro
        Veiculo.__init__(self, marca, qtdRodas, modelo, velocidade)
    def imprimirbike(self):
        print("Marca:", self.marca, "\n Quantidade de rodas:", self.qtdRodas,"\n Modelo:", self.modelo, "\n Velocidade:", self.velocidade, "\n Marchas:", numMarchas, "\n Bagageiro:", bagageiro)


class Automovel(Veiculo):
    def __init__(self, marca, qtdRodas, modelo, velocidade, potenciaDoMotor):
        self.potenciaDoMotor = potenciaDoMotor
        Veiculo.__init__(self, marca, qtdRodas, modelo, velocidade)

    def imprimirauto(self):
           print("Marca:", self.marca, "\n Quantidade de rodas:", self.qtdRodas,
              "\n Modelo:", self.modelo, "\n Velocidade:", self.velocidade, "\n Potencia do motor:", potenciaDoMotor)
class Moto(Automovel):
    def __init__(self, marca, qtdRodas, modelo, velocidade, potenciaDoMotor, partidaEletrica):
        self.partidaEletrica = partidaEletrica
        Automovel.__init__(self, marca, qtdRodas, modelo, velocidade, potenciaDoMotor)
        
    def imprimirmoto(self):
           print("Marca:", self.marca, "\n Quantidade de rodas:", self.qtdRodas,
              "\n Modelo:", self.modelo, "\n Velocidade:", self.velocidade, "\n Potencia do motor:", potenciaDoMotor, "\n partida:" ,self.partidaEletrica)

class Carro(Automovel):
    def __init__(self, marca, qtdRodas, modelo, velocidade, potenciaDoMotor, qtdPortas):
        self.qtdPortas = qtdPortas
        Automovel.__init__(self, marca, qtdRodas, modelo, velocidade, potenciaDoMotor)

    def imprimircarro(self):
           print("Marca:", self.marca, "\n Quantidade de rodas:", self.qtdRodas,
              "\n Modelo:", self.modelo, "\n Velocidade:", self.velocidade, "\n Potencia do motor:", potenciaDoMotor, "\n portas:", qtdPortas)
