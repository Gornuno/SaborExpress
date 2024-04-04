#Em caso de problema com o reconhecimento do diretório usar as seguintes linhas
##import sys
##sys.path.append(camimho personalizado)

from modelos.avaliacao import Avaliacao

class Restaurante:
    restaurantes = []

    def __init__(self, nome, categoria):
        '''Construtor do objeto da classe Restaurante
        
        Parâmetros:
        - nome(str): Nome do restaurante;
        - categoria(str): Categoria da comida servida no restaurante
        '''
        self._nome = nome.title()
        self._categoria = categoria.upper()
        self._ativo = False
        self._avaliacao = []
        Restaurante.restaurantes.append(self)
    
    def __str__(self):
        '''Função responsável por imprimir de forma legível e individual o restaurante selecionado
        
        Output:
        (nome) | (categoria)
        '''
        return f'{self._nome} | {self._categoria}'
    
    @classmethod
    def listar_restaurantes(cls):
        '''Função responsável por dispor todos os restaurantes cadastros em forma de tabela para melhor visualização e compreensão dos atr'''
        print(f'{"Nome do restaurante".ljust(25)} | {"Categoria".ljust(25)} | {"Avaliação".ljust(25)} |{"Status"}')
        for restaurante in cls.restaurantes:
            print(f'{restaurante._nome.ljust(25)} | {restaurante._categoria.ljust(25)} | {str(restaurante.media_avaliacoes).ljust(25)} |{restaurante.ativo}')

    @property
    def ativo(self):
        '''Função usada para retornar o símbolo de ativo e inativo

        Retorno:
        ⌧ no caso de ativo
        ☐ no caso de inativo
        '''
        return '⌧' if self._ativo else '☐'
    
    def alternar_estado(self):
        '''Função usada para alternar o estado cadastral do restaurante, utilizando os símbolos de ativo e inativo.'''
        self._ativo = not self._ativo

    def receber_avaliacao(self, cliente, nota):
        '''Função usada para registrar uma avaliação
         
        Argumentos:
        - cliente(str): O nome do cliente que fez a avaliação.
        - nota(str): A nota dada pelo cliente avaliador.
        '''
        if 0 < nota <= 5:
            avaliacao = Avaliacao(cliente, nota)
            self._avaliacao.append(avaliacao)

    @property
    def media_avaliacoes(self):
        "Calcula e retorna a média das avaliação do restaurante."
        if not self._avaliacao:
            return '-'

        soma_das_notas = sum(avaliacao.nota for avaliacao in self._avaliacao)
        quantidade_de_notas = len(self._avaliacao)

        media = round(soma_das_notas / quantidade_de_notas, 1)

        return media
