#!/usr/bin/python
#-*- coding: utf-8 -*-

from Usuário import Usuário
import random

class Entregador(Usuário):
    
    def __init__(self, nome, CPF, email, localizacao, appMain):
        self.nome = nome
        self.CPF = CPF
        self.email = email
        self.disponibilidade = True
        self.localizacao = localizacao
        self.entrega = None
        self.appMain = appMain

    def aceitarEntrega(self, ListaDeEntregas, number):
        number = random.randint(0, len(ListaDeEntregas))
        self.entrega = ListaDeEntregas[number]

    def finalizar(self):
        self.appMain.finalizarEntrega(self.entrega.foto, self.entrega.produtoDaEntrega.ID)
        self.disponibilidade = True

    def tirarFoto(self, foto):
        self.entrega.foto = foto