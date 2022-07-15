from App import App
from Cliente import Cliente
from Entregador import Entregador
from Slot import Slot

teste = App()
Armario01 = Slot("www.armario01.com", (1, 1), teste)
Armario02 = Slot("www.armario02.com", (2, 1), teste)
Bruno = Cliente("Bruno", 1234, "bruno@gmail.com", teste, "Pix")
Sonic = Entregador("Sonic", 12345, "sonic@gmail.com", teste)
Bruno.criarEntrega("www.armario01.com", (2,1))
Sonic.aceitarEntrega((1,1), (2,1))
#Sonic.abrirSlotDeOrigem()
#Sonic.abrirSlotDeDestino()
Sonic.finalizar()
Sonic.tirarFoto("JPEG")
Sonic.finalizar()
Sonic.aceitarEntrega((1,1), (2,1))
Sonic = Sonic.alterarStatus()
print(str(type(Sonic)))
teste.removeUsuario(Sonic)
print(str(type(Sonic)))