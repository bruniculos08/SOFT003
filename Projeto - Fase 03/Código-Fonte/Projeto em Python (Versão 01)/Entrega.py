#!/usr/bin/python
#-*- coding: utf-8 -*-

# random é um módulo
import random
# importa-se Produto pois esta classe compõe a classe entrega
from Produto import Produto

class Entrega:
    def __init__(self, statusFinal, valor, origem, destino, foto, data, hora, slot, produto):
        self.statusFinal = statusFinal
        self.valor = valor
        self.origem = origem
        self.destino = destino
        self.foto = foto
        self.data = data
        self.hora = hora
        self.slot = slot
        self.produto = produto
        self.slot.IDatual = self.produtoDaEntrega.ID
