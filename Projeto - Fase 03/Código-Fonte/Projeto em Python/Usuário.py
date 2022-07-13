#!/usr/bin/python
#-*- coding: utf-8 -*-

from Rotas import Rotas

class Usuário:
    def __init__(self):
        self.nome = None
        self.CPF = None
        self.email = None
        self.listaDeRotas = []

    def deletarUsuario(self):
        del (self)

    def criarRota(self):
        newRota = Rotas()
        self.listaDeRotas.append(newRota)

