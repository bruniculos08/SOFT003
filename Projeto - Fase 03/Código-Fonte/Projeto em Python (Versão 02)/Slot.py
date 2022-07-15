#!/usr/bin/python
#-*- coding: utf-8 -*-

class Slot:
    def __init__(self, link, localizacao, appMain):
        self.link = link
        # self.disponibilidade = None       Obs.: este atributo é redundante
        self.IDatual = None
        self.trancado = False
        self.localizacao = localizacao
        self.appMain = appMain
        self.appMain.addSlot(self)

