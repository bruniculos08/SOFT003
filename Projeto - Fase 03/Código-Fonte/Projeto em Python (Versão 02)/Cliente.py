#!/usr/bin/python
#-*- coding: utf-8 -*-

from Usuário import Usuário
from Entrega import Entrega
from Slot import Slot

class Cliente(Usuário):
    def __init__(self, nome, CPF, email, appMain, formaDePagamento):
        super().__init__(nome, CPF, email, appMain)
        self.formaDePagamento = formaDePagamento
        self.appMain.addCliente(self)

    # (1) O cliente coloca o produto em um slotDeOrigem (mas ele só tem como saber o link desse slot)...
    # ... por isso a classe App deve ter um método para buscar tal slot.
    # Após encontrar tal slot, a entrega é criada com slotDeOrigem e slotDeDestino:
    def criarEntrega(self, link, destino):
        slotDeOrigem = self.appMain.buscaSlot(link)
        slotDeDestino = self.appMain.buscaSlot(destino)
        if(slotDeDestino.trancado == True or slotDeOrigem.trancado == True): return None
        else:
            newEntrega = Entrega(slotDeOrigem, slotDeDestino, self.appMain)
            return newEntrega.produto.ID

    # (2) O cliente retira o produto do slot se estiver no link do armário cujo produto atual dentro...
    # ... do mesmo corresponda ao ID enviado pelo usuário:
    def receberEntrega(self, link, ID):
        slotDeDestino = self.appMain.buscaSlot(link)
        if(slotDeDestino.IDatual == ID):
            print("Armário de link " + slotDeDestino.link + " aberto para retirada.")
            slotDeDestino.trancado = False
            slotDeDestino.IDatual = None
            return True
        else:
            print("ID errado ou produto não recebido.") 
            return False


