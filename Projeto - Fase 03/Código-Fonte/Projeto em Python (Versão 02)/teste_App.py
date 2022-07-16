import unittest
from App import App
from Cliente import Cliente
from Entregador import Entregador
from Entrega import Entrega
from Slot import Slot

class Teste_App(unittest.TestCase):

    def test_addCliente(self):
        testeApp = App()
        Bruno = Cliente("Bruno", 1234, "bruno@gmail.com", testeApp, "Pix")
        self.assertEqual(Bruno, testeApp.listaDeClientes[0])

    def test_addEntregador(self):
        testeApp = App()
        Sonic = Entregador("Sonic", 12345, "sonic@gmail.com", testeApp)
        self.assertEqual(Sonic, testeApp.listaDeEntregadores[0])

    def test_addSlot(self):
        testeApp = App()
        slot1 = Slot("www.armario01.com", (2,5), testeApp)
        self.assertEqual(slot1, testeApp.listaDeSlots[0])

    def test_removeUsuario(self):
        testeApp = App()

        # (1) Para objeto da classe Cliente:
        Bruno = Cliente("Bruno", 1234, "bruno@gmail.com", testeApp, "Pix")
        testeApp.removeUsuario(Bruno)
        self.assertEqual([], testeApp.listaDeClientes)
        self.assertEqual(Bruno, testeApp.listaDeObjetosRemovidos[0])

        # (2) Para objeto da classe Entregador:
        Sonic = Entregador("Sonic", 12345, "sonic@gmail.com", testeApp)
        testeApp.removeUsuario(Sonic)
        self.assertEqual([], testeApp.listaDeEntregadores)
        self.assertEqual(Sonic, testeApp.listaDeObjetosRemovidos[1])
    
    def test_buscaSlot(self):
        testeApp = App()
        slot1 = Slot("www.armario01.com", (2,5), testeApp)
        self.assertEqual(testeApp.buscaSlot("www.armario01.com"), slot1)
        self.assertEqual(testeApp.buscaSlot((2,5)), slot1)

    def test_alterarStatus(self):
        testeApp = App()

        Bruno = Cliente("Bruno", 1234, "bruno@gmail.com", testeApp, "Pix")
        Bruno = testeApp.alterarStatus(Bruno)
        self.assertEqual([], testeApp.listaDeClientes)
        self.assertEqual(Bruno, testeApp.listaDeEntregadores[0])
        testeApp.removeUsuario(Bruno)

        Sonic = Entregador("Sonic", 12345, "sonic@gmail.com", testeApp)
        Sonic = testeApp.alterarStatus(Sonic)
        self.assertEqual([], testeApp.listaDeEntregadores)
        self.assertEqual(Sonic, testeApp.listaDeClientes[0])


    def test_associaEntregador(self):
        testeApp = App()
        Bruno = Cliente("Bruno", 1234, "bruno@gmail.com", testeApp, "Pix")
        Sonic = Entregador("Sonic", 12345, "sonic@gmail.com", testeApp)
        slot1 = Slot("www.armario01.com", (2,5), testeApp)
        slot2 = Slot("www.armario02.com", (5,7), testeApp)
        slot3 = Slot("www.armario03.com", (5,4), testeApp)
        slot4 = Slot("www.armario04.com", (4,1), testeApp)
        newEntregaID = Bruno.criarEntrega("www.armario01.com", (5,4))
        self.assertEqual(None, Sonic.entregaAtual)
        Sonic.aceitarEntrega((2,5), (5,4))
        self.assertEqual(newEntregaID, Sonic.entregaAtual.produto.ID)
        Sonic.tirarFoto("JPEG")
        Sonic.finalizar()
        Sonic.aceitarEntrega((2,5), (5,4))
        self.assertEqual(None, Sonic.entregaAtual)
        

    def test_finalizar(self):
        testeApp = App()
        Bruno = Cliente("Bruno", 1234, "bruno@gmail.com", testeApp, "Pix")
        Sonic = Entregador("Sonic", 12345, "sonic@gmail.com", testeApp)
        slot1 = Slot("www.armario01.com", (2,5), testeApp)
        slot2 = Slot("www.armario02.com", (5,7), testeApp)
        slot3 = Slot("www.armario03.com", (5,4), testeApp)
        slot4 = Slot("www.armario04.com", (4,1), testeApp)
        Bruno.criarEntrega("www.armario02.com", (4,1))
        Sonic.aceitarEntrega((5,7),(4,1))
        Sonic.tirarFoto("teste.JPEG")
        entregaFinalizada = Sonic.entregaAtual
        self.assertTrue(entregaFinalizada.slotDeDestino.trancado)
        self.assertEqual(entregaFinalizada, testeApp.finalizar("teste.JPEG"))
        self.assertTrue(entregaFinalizada.slotDeDestino.trancado)

if __name__ == "__main__":
    unittest.main()