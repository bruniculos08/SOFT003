#!/usr/bin/python
#-*- coding: utf-8 -*-

from math import sqrt
from Produto import Produto
import random

class Entrega:
    def __init__(self, slotDeOrigem, slotDeDestino, appMain):
        self.statusFinal = False
        self.valor = self.encontrarValor(slotDeOrigem, slotDeDestino)
        self.slotDeOrigem = slotDeOrigem
        self.slotDeDestino = slotDeDestino
        self.foto = None
        self.produto = self.criarProduto()
        self.appMain = appMain
        self.appMain.addEntrega(self)
        self.entregadorAtual = None

    def criarProduto(self):
        newProduto = Produto(random.randint(0, 10000))
        self.slotDeOrigem.IDatual = newProduto.ID
        self.slotDeOrigem.trancado = True
        self.slotDeDestino.IDatual = newProduto.ID
        self.slotDeDestino.trancado = True
        return newProduto

    def encontrarValor(self, slotDeOrigem, slotDeDestino):
        insideRoot = pow(slotDeOrigem.localizacao[0]-slotDeDestino.localizacao[0], 2) + pow(slotDeOrigem.localizacao[1]-slotDeDestino.localizacao[1], 2)
        distance = round(sqrt(insideRoot), 2)
        return distance*(1) 