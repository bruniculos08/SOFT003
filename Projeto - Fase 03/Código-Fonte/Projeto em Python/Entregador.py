#!/usr/bin/python
#-*- coding: utf-8 -*-

from Usuário import Usuário

class Entregador(Usuário):
    def __init__(self, Entrega):
        self.disponibilidade = True
        self.entrega = Entrega

    def finalizarEntrega(self):
        self.entrega.statusFinal = True