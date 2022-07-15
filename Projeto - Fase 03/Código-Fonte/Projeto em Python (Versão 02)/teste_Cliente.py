import unittest
from App import App
from Cliente import Cliente
from Entregador import Entregador
from Entrega import Entrega
from Slot import Slot

class Teste_Cliente(unittest.TestCase):

    def test_criarEntrega(self):
        testeApp = App()
        Bruno = Cliente("Bruno", 1234, "bruno@gmail.com", testeApp, "Pix")
        Sonic = Cliente("Sonic", 12345, "sonic@gmail.com", testeApp, "Débito")
        slot1 = Slot("www.armario01.com", (2,5), testeApp)
        slot2 = Slot("www.armario02.com", (5,7), testeApp)
        slot3 = Slot("www.armario03.com", (5,4), testeApp)
        slot4 = Slot("www.armario04.com", (4,1), testeApp)
        Sonic.criarEntrega(("www.armario02.com"), (5,4))
        self.assertEqual(None, Bruno.criarEntrega(("www.armario02.com"), (5,4)))
    
    def teste_receberEntrega(self):
        
        pass

if __name__ == "__main__":
    unittest.main()