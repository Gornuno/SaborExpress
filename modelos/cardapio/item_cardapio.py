from abc import ABC,abstractmethod
import sys
sys.path.append('D:\\Users\\mg10392ps\\Desktop\\Estudos\\BACKEND\\Sabor-express oo')

class ItemCardapio(ABC):
    def __init__(self, nome, preco):
        self._nome = nome
        self._preco = preco
    
    @abstractmethod
    def aplicar_desconto(self):
        pass
