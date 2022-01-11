
from classes.recipiente import Recipiente

class Copo(Recipiente):
    def __init__(self, tamanho,
    conteudo: float = 0,
    limpo: bool = True):
        super().__init__(tamanho, conteudo, limpo)
        
    def encher(self,  bebida: str = 'água' ):
        self.bebida = bebida
        if self.limpo == True:
            self.bebida = bebida
            self.conteudo = self.tamanho
            self.sujar()
        return 'Não se pode encher um copo sujo'    
        

    def beber(self, quantidade: float):
        self.quantidade = quantidade
        if quantidade < 0:
            return f'Quantidade deve ser positiva'
        elif quantidade > self.tamanho or quantidade > self.conteudo:
            return f'Não há bebida suficiente no copo'
        self.conteudo -= quantidade


    def lavar(self):
        self.bebida = None
        self.conteudo = 0
        self.limpo = True;
    
    def __str__(self):
        if self.conteudo == 0:
           return f'Um copo vazio de {float(self.tamanho)}ml'
        return f'Um copo de {float(self.tamanho)}ml contendo {float(self.conteudo)}ml de {self.bebida}'
        
        
    def __repr__(self):
        if self.conteudo == 0:
           return 'Um copo vazio de %sml' % float(self.tamanho) 
        return 'Um copo de %sml contendo %sml de %s' % (float(self.tamanho),float(self.conteudo),self.bebida)
    
    

