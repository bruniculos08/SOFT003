#!/usr/bin/python
#-*- coding: utf-8 -*-

# random é um módulo
import random
# importa-se Produto pois esta classe compõe a classe entrega
from Produto import Produto

class Entrega:
    def __init__(self, statusFinal, valor, origem, destino, foto, data, hora, slot):
        self.statusFinal = statusFinal
        self.valor = valor
        self.origem = origem
        self.destino = destino
        self.foto = foto
        self.data = data
        self.hora = hora
        self.slot = slot
        self.produtoDaEntrega = self.criarProduto()
        self.slot.IDatual = self.produtoDaEntrega.ID

    def criarProduto(self):
        newProduct = Produto(random.randint(0, 1))
        # (1) Para testar essa classe:
        return newProduct

