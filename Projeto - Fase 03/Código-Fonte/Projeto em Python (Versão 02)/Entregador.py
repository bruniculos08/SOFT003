#!/usr/bin/python
#-*- coding: utf-8 -*-

from Usuário import Usuário

class Entregador(Usuário):
    def __init__(self, nome, CPF, email, appMain):
        super().__init__(nome, CPF, email, appMain)
        self.disponibilidade = True
        self.entregaAtual = None
        self.appMain.addEntregador(self)

    # (1) O entregador seleciona uma origem e um destino para o qual aceitará fazer entrega e...
    # ... então o App seleciona uma entrega a ser feita:   
    def aceitarEntrega(self, origem, destino):
        slotDeOrigem = self.appMain.buscaSlot(origem)
        slotDeDestino = self.appMain.buscaSlot(destino)
        self.entregaAtual = self.appMain.associarEntregador(self, slotDeDestino, slotDeOrigem)
        if self.entregaAtual == None: print("Entrega não disponível.")

    # (2) O entregador pode abrir o slot de origem para buscar o produto, sem nenhuma restrição:
    def abrirSlotDeOrigem(self):
        if(self.entregaAtual == None): return False
        self.appMain.linkUse(self.entregaAtual.slotDeOrigem.link, self.entregaAtual.produto.ID)
        return True

    # (3) Diferente de quando o se abre o slotDeOrigem, para evitar que o entregador tire a foto,...
    # ... abra o slotDeDestino novamente e furte o produto, deve-se apagar a foto anterior a abertura...
    # ... do slotDeDestino:
    def abrirSlotDeDestino(self):
        if(self.entregaAtual == None): return False
        self.entregaAtual.foto = None
        self.appMain.linkUse(self.entregaAtual.slotDeDestino.link, self.entregaAtual.produto.ID)
        return True

    # (4) Tirar foto de entrega, para depois poder finalizar a entrega:
    def tirarFoto(self, foto):
        if(self.entregaAtual == None): return
        self.entregaAtual.foto = foto


    # (5) O entregador ao chegar no destino da entrega e depois de ter deixado o item dentro...
    # ... do slot e ter tirado uma foto, pode finalizar a entrega:
    def finalizar(self):
        if(self.entregaAtual == None): return True
        elif self.entregaAtual.foto == None:
            print("Deve-se tirar a foto da entrega antes de poder finaliza-la")
            return False
        else:
            self.appMain.finalizar(self.entregaAtual.foto)
            print("Entrega finalizada por " + self.nome)
        self.entregaAtual = None
        return True    
