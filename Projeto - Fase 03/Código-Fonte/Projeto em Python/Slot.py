#!/usr/bin/python
#-*- coding: utf-8 -*-

class Slot:
    def __init__(self):
        self.link = None
        self.disponibilidade = True
        self.IDatual = None
        self.trancado = False

    def mudarTrancado(self):
        if(self.trancado == False): self.trancado = True
        else: self.trancado = False

    def mudarID(self, ID):
        self.IDatual = ID