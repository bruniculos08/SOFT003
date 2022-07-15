#!/usr/bin/python
#-*- coding: utf-8 -*-
from Rota import Rota

class Usuário:
    def __init__(self, nome, CPF, email, appMain):
        self.nome = nome
        self.CPF = CPF
        self.email = email
        self.listaDeRotas = []
        self. appMain = appMain

    def deletarUsuario(self):
        del (self)

    def criarRota(self, nomeDaRota, ListaDeCoordenadas):
        newRota = Rota(nomeDaRota, ListaDeCoordenadas)
        self.listaDeRotas.append(newRota)

    def alterarStatus(self):
        return self.appMain.alterarStatus(self)
