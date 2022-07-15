#!/usr/bin/python
#-*- coding: utf-8 -*-

from Usuário import Usuário
from Entregador import Entregador
from Entrega import Entrega

class Cliente(Usuário):
    
    def __init__(self, nome, CPF, email, formaDePagamento, appMain):
        self.formaDePagamento = formaDePagamento
        self.nome = nome
        self.CPF = CPF
        self.email = email
        self.formaDePagamento = formaDePagamento
        self.appMain = appMain

    def solicitarEntrega(self, valor, origem, destino, data, hora, link):
        self.appMain.solicita(valor, origem, destino, data, hora, link)
        return