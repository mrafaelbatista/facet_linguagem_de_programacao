class Bolo():

    def __init__(self, sabor, cor, textura, tamanho, formato):
        
        self.sabor = sabor
        self.cor = cor
        self.textura = textura
        self.tamanho = tamanho
        self.formato = formato
    
    def ser_gostoso(self):
        print('Esse bolo de '  + self.sabor + '.')
    
    def ser_gostoso2(self):
        return 'Esse bolo de '  + self.sabor + '.'

bolo_macaxeira = Bolo('macaxeira', 'branco amarelado', 'baêta', 'pequeno', 'quadrado')

bolo_macaxeira.ser_gostoso2()
