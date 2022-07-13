#!/usr/bin/python
#-*- coding: utf-8 -*-

# random é um módulo
from random import *
# importa-se Produto pois esta classe compõe a classe entrega
from Produto import Produto

class Entrega:
    def __init__(self, statusFinal, valor, destino, foto):
        self.statusFinal = statusFinal
        self.valor = valor
        self.destino = destino
        self.foto = foto
        self.produtoDaEntrega = self.criarProduto()

    def criarProduto(self):
        newProduct = Produto(random.randint(0, 1000000000000))
        # (1) Para testar essa classe:
        return newProduct

