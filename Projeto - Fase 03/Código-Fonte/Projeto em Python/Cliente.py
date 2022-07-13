#!/usr/bin/python
#-*- coding: utf-8 -*-

from Usuário import Usuário
from Entrega import Entrega

class Cliente(Usuário):
    def __init__(self, formaDePagamento):
        self.formaDePagamento = formaDePagamento

    def criarEntrega(self, cordX, cordY):
        newEntrega = Entrega(False, 0 , (cordX, cordY), 0)

