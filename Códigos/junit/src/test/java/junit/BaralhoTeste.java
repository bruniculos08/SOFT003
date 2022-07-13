package junit;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertNotNull;
import static org.junit.jupiter.api.Assertions.assertNotSame;
import static org.junit.jupiter.api.Assertions.assertSame;

import java.util.Iterator;
import java.util.Vector;

import org.junit.jupiter.api.Test;

public class BaralhoTeste {
    
    Baralho baralhoTeste = new Baralho();

    @Test
    public void lookBaralho() {
        assertEquals(1, baralhoTeste.menorValor());
        assertEquals(13, baralhoTeste.maiorValor());
        assertEquals(0, baralhoTeste.primeiroNaipe());
        assertEquals(3, baralhoTeste.ultimoNaipe());

        // (1) Número de cartas no baralho = 13 . 4 = 52:
        assertEquals(52, baralhoTeste.numeroDeCartas());

        // (2) O método interator() de Baralho retorna o iterator do atributo baralho, que por sua vez...
        // ... pertence a classe Vector:
        Vector vector = baralhoTeste.baralho;
        Iterator iterator = vector.iterator();
        assertNotSame(iterator, baralhoTeste.iterator());

        // (3) Como após "baralhar" o baralho não terá mais as cartas na mesma ordem temos que baralho deve...
        // ser diferente do retorno de baralhar():
        assertSame(baralhoTeste.baralho, baralhoTeste.baralhar());

        // (4) Visto que o baralho tem 52 cartas, se removermos a carta do topo através da função pegar carta...
        // ... esta irá retornar a carta do topo e o baralho ficará com 51 cartas:
        assertNotNull(baralhoTeste.pegaCarta());

        // (5) A carta da última posição no vetor é sempre a carta a ser removida:
        int cartasRestantes = baralhoTeste.numeroDeCartas();
        for(int i = 0; i < cartasRestantes; i++){
            assertEquals(baralhoTeste.baralho.get(baralhoTeste.numeroDeCartas()-1) , baralhoTeste.pegaCarta());
        }
    }
}