#!/usr/bin/python
#-*- coding: utf-8 -*-

from Entregador import Entregador
from Cliente import Cliente
from Entrega import Entrega
from Slot import Slot
import time

class App:

    def __init__(self):
        self.listaDeEntregadores = []
        self.listaDeClientes = []
        self.listaDeUsuarios = []
        self.listaDeEntregas = []
        self.listaDeSlots = []

    def addEntregador(self, nome, cpf, email, localizacao):
        newEntregador = Entregador(nome, cpf, email, localizacao, self)
        self.listaDeEntregadores.append(newEntregador)

    def addCliente(self, nome, cpf, email, formaDePagamento):
        newCliente = Cliente(nome, cpf, email, formaDePagamento, self)
        self.listaDeClientes.append(newCliente)
        # (1) Para teste:
        return newCliente

    def addSlot(self, link, ID):
        newSlot = Slot(link, ID)
        self.listaDeSlots.append(newSlot)
        return newSlot

    def removeEntregador(self, oldEntregador):
        self.listaDeEntregadores.remove(oldEntregador)

    def removeCliente(self, oldCliente):
        self.listaDeClientes.remove(oldCliente)

    def alterarStatus(self, oldUsuario, argumentoExtra):
        if(type(oldUsuario) == Cliente):
            self.addEntregador(oldUsuario.nome, oldUsuario.cpf, oldUsuario.email, argumentoExtra)
            self.removeCliente(oldUsuario)
        elif(type(oldUsuario) == Entregador):
            self.addCliente(oldUsuario.nome, oldUsuario.cpf, oldUsuario.email, argumentoExtra)
            self.removeEntregador(oldUsuario)
        else:
            print("Erro.")

    def slotLivre(self, link):
        for item in self.listaDeSlots:
            if(item.link == link): return item
            else: return self.addSlot(link, None)

    def solicita(self, valor, origem, destino, data, hora, link):
        for item in self.listaDeEntregadores:
            if(item.disponibilidade == True):
                item.disponibilidade = False
                item.entrega = Entrega(False, valor, origem, destino, None, data, hora, self.slotLivre(link))
                self.listaDeEntregas.append(item.entrega)
                print("Entrega solicitada e aceita por " + item.nome)

    def linkUse(self, link, ID):
        for item in self.listaDeSlots:
            if(item.link == link and item.IDatual == ID):
                item.trancado = False
                print("Slot link " + str(link) + " aberto por 5 segundos...")
                for i in range(0, 6):
                    print(5-i)
                    time.sleep(1)
                print("Slot link " + str(link) + " fechado.")
                item.trancado = True
                return
    
    def finalizarEntrega(self, foto, ID):
        for item in self.listaDeEntregas:
            if(item.entrega.produtoDaEntrega.ID == ID):
                self.produtoEntregue(item)
                item.entrega.foto = foto
                return
            else:
                print("A entrega não existe.")

    def produtoEntregue(self, entrega):
        if(entrega.foto != None):
            entrega.statusFinal = True
            return