#!/usr/bin/python
#-*- coding: utf-8 -*-

import time
from Cliente import Cliente
from Entregador import Entregador

class App:
    def __init__(self):
        self.listaDeClientes = []
        self.listaDeEntregadores = []
        self.listaDeSlots = []
        self.listaDeEntregas = []
        self.listaDeObjetosRemovidos = []

    def addCliente(self, newCliente):
        self.listaDeClientes.append(newCliente)

    def addEntregador(self, newEntregador):
        self.listaDeEntregadores.append(newEntregador)

    def addEntrega(self, newEntrega):
        self.listaDeEntregas.append(newEntrega)

    def addSlot(self, newSlot):
        self.listaDeSlots.append(newSlot)

    # (5) O usuáro removido vai para uma lista de usuários removidos (pois os dados das entregas precisam ser salvos):
    def removeUsuario(self, oldUsuario):
        if(type(oldUsuario) == Cliente):
            index = self.listaDeClientes.index(oldUsuario)
            self.listaDeObjetosRemovidos.append(self.listaDeClientes.pop(index))
        elif type(oldUsuario) == Entregador:
            index = self.listaDeEntregadores.index(oldUsuario)
            self.listaDeObjetosRemovidos.append(self.listaDeEntregadores.pop(index))
        else:
            print("O Usuário a ser removido não existe.")

    # (6) O slot pode ser encontrado por sua localizacao ou link:
    def buscaSlot(self, linkOrDestino):
        if type(linkOrDestino) == str:
            return next((x for x in self.listaDeSlots if x.link == linkOrDestino), None)
        else:
            return next((x for x in self.listaDeSlots if x.localizacao == linkOrDestino), None)
        
    
    # (7) O objeto usuário que alterou o status irá ser removido (para a lista de removidos) e...
    # ... e será criado um novo objeto da classe para qual o status foi alterado, e assim tal...
    # ... objeto será retornado:
    def alterarStatus(self, oldUsuario):
        if(type(oldUsuario) == Cliente):
            index = self.listaDeClientes.index(oldUsuario)
            self.listaDeObjetosRemovidos.append(self.listaDeClientes.pop(index))
            return Entregador(oldUsuario.nome, oldUsuario.CPF, oldUsuario.email, self)
        elif type(oldUsuario) == Entregador:
            index = self.listaDeEntregadores.index(oldUsuario)
            self.listaDeObjetosRemovidos.append(self.listaDeEntregadores.pop(index))
            return Cliente(oldUsuario.nome, oldUsuario.CPF, oldUsuario.email, self, "Indefinida")
        else:
            return None
            

    # (8) Quando o entregador aceitar uma entrega, o app tentará associa-lo à entrega...
    # ... porém ele só sera associado caso a entrega não tenha entregador atualmente:
    def associarEntregador(self, newEntregador, slotDeDestino, slotDeOrigem):
        entregaAssociada = next((x for x in self.listaDeEntregas if x.slotDeOrigem == x.slotDeOrigem and x.slotDeDestino == slotDeDestino), None)
        if(entregaAssociada == None): return None
        index = self.listaDeEntregas.index(entregaAssociada)

        if self.listaDeEntregas[index].entregadorAtual == None:
            self.listaDeEntregas[index].entregadorAtual = newEntregador
            print("O entregador " + newEntregador.nome + " aceitou a entrega pelo valor de " + str(self.listaDeEntregas[index].valor))
            return self.listaDeEntregas[index]
        else: 
            return None
        

    # (9) Quando ocorre um acesso à um slot que está sendo usado em uma entrega (tem um ID associado) este...
    # ... acesso ocorre através dessa função:
    def linkUse(self, link, ID):
        slotDoLink = next((x for x in self.listaDeSlots if x.link == link and x.IDatual == ID), None)
        index = self.listaDeSlots.index(slotDoLink) 
        if(self.listaDeSlots[index].link != link): return
        self.listaDeSlots[index].trancado = False
        print("Slot link " + str(link) + " aberto por 5 segundos...")
        for i in range(0, 6):
            print(5-i)
            time.sleep(1)
        print("Slot link " + str(link) + " fechado.")
        self.listaDeSlots[index].trancado = True

    # (10) Quando a entrega termina, os slots são abertos e o status da entrega é alterado:
    def finalizar(self, foto):
        entregaFinalizada = next((x for x in self.listaDeEntregas if x.foto == foto and x.statusFinal == False), None)
        #if(entregaFinalizada == None): return
        index = self.listaDeEntregas.index(entregaFinalizada)
        self.listaDeEntregas[index].slotDeOrigem.trancado = False
        self.listaDeEntregas[index].slotDeOrigem.IDatual = None
        self.listaDeEntregas[index].slotDeDestino.IDatual = None
        self.listaDeEntregas[index].statusFinal = True
        # (10.1) return adicionado para fins de teste:
        return self.listaDeEntregas[index]
    
