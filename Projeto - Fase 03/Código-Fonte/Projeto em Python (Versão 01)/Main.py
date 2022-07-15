from App import App

teste = App()
teste.addSlot("www.teste.com", None)
Bruno = teste.addEntregador("Bruno", 1111, "teste@gmail.com", (1, 1))
Sonic = teste.addCliente("Sonic", 1234, "rapido@gmail.com", "Pix")
Sonic.solicitarEntrega(1, (1,0), (0, 1), 1, 1, "wwww.teste.com")
teste.linkUse("www.teste.com", None)
Bruno.tirarFoto("JPEG")
Bruno.finalizar()
Sonic.solicitarEntrega(1, (1,0), (0, 1), 1, 1, "wwww.teste.com")
