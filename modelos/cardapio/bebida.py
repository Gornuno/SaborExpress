import sys
sys.path.append('D:\\Users\\mg10392ps\\Desktop\\Estudos\\BACKEND\\Sabor-express oo')

from modelos.cardapio.item_cardapio import ItemCardapio

class Bebida(ItemCardapio):
    def __init__(self, nome,preco, tamanho):
        super().__init__(nome,preco)
        self.tamanho = tamanho

    def __str__(self):
        return self._nome
    
    def aplicar_desconto(self):
        self._preco -= (self._preco * 0.08)
        
        
