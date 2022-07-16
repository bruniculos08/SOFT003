import unittest
from App import App
from Cliente import Cliente
from Entregador import Entregador
from Entrega import Entrega
from Slot import Slot

class Teste_Cliente(unittest.TestCase):
    
    def teste_aceitarEntrega(self):
        testeApp = App()
        Bruno = Cliente("Bruno", 1234, "bruno@gmail.com", testeApp, "Pix")
        Sonic = Entregador("Sonic", 12345, "sonic@gmail.com", testeApp)
        slot1 = Slot("www.armario01.com", (2,5), testeApp)
        slot2 = Slot("www.armario02.com", (5,7), testeApp)
        newEntregaID = Bruno.criarEntrega(("www.armario01.com"), (5,7))
        Sonic.aceitarEntrega((2,5), (5,7))
        self.assertNotEqual(None, Sonic.entregaAtual)
        self.assertEqual(newEntregaID, Sonic.entregaAtual.produto.ID)
        Sonic.tirarFoto("teste.JPEG")
        Sonic.finalizar()
        self.assertEqual(None, Sonic.entregaAtual)
        Sonic.aceitarEntrega((2,5), (5,7))
        self.assertEqual(None, Sonic.entregaAtual)
        Sonic.aceitarEntrega((2,5), (5,5))
        self.assertEqual(None, Sonic.entregaAtual)

    def teste_abrirSlotDeOrigem(self):
        testeApp = App()
        Bruno = Cliente("Bruno", 1234, "bruno@gmail.com", testeApp, "Pix")
        Sonic = Entregador("Sonic", 12345, "sonic@gmail.com", testeApp)
        slot1 = Slot("www.armario01.com", (2,5), testeApp)
        slot2 = Slot("www.armario02.com", (5,7), testeApp)
        newEntregaID = Bruno.criarEntrega(("www.armario01.com"), (5,7))
        self.assertFalse(Sonic.abrirSlotDeOrigem())
        Sonic.aceitarEntrega((2,5), (5,7))
        self.assertTrue(Sonic.abrirSlotDeOrigem())

    def teste_abrirSlotDeDestino(self):
        testeApp = App()
        Bruno = Cliente("Bruno", 1234, "bruno@gmail.com", testeApp, "Pix")
        Sonic = Entregador("Sonic", 12345, "sonic@gmail.com", testeApp)
        slot1 = Slot("www.armario01.com", (2,5), testeApp)
        slot2 = Slot("www.armario02.com", (5,7), testeApp)
        newEntregaID = Bruno.criarEntrega(("www.armario01.com"), (5,7))
        self.assertFalse(Sonic.abrirSlotDeDestino())
        Sonic.aceitarEntrega((2,5), (5,7))
        self.assertTrue(Sonic.abrirSlotDeDestino())

    def teste_tirarFoto(self):
        testeApp = App()
        Bruno = Cliente("Bruno", 1234, "bruno@gmail.com", testeApp, "Pix")
        Sonic = Entregador("Sonic", 12345, "sonic@gmail.com", testeApp)
        slot1 = Slot("www.armario01.com", (2,5), testeApp)
        slot2 = Slot("www.armario02.com", (5,7), testeApp)
        Bruno.criarEntrega(("www.armario01.com"), (5,7))
        Sonic.aceitarEntrega((2,5), (5,7))
        Sonic.tirarFoto("teste.JPEG")


if __name__ == "__main__":
    unittest.main()