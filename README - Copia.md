Classe App
operação: solicita(IDProduto, localização)

alias: (onde vão as variáveis, ou algo que pode ser usado em pós ou pré)
    entregadoresDisponiveis <- select(entregador.disponível == true)

pré: (o que deve haver antes da operação)
    entregadoresDisponíveis -> size() > 0

pós: (o que deve ocorrer pela operação)
     entregadorSelecionado <- getEntregador(entregadoresDisponíveis)
