#!/usr/bin/python
#-*- coding: utf-8 -*-

from Usuário import Usuário

class Cliente(Usuário):
    def __init__(self):
        self.formaDePagamento = None

    def criarEntrega(self, String):
        pass

