package junit;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertNotSame;
import static org.junit.jupiter.api.Assertions.assertTrue;

import org.junit.jupiter.api.Test;

public class CartaTeste {
    
    Carta carta = new Carta(1, 1);
    Carta outra = new Carta(1, 1);

    @Test
    public void lookCarta(){
        assertEquals(1, carta.getValor());
        assertEquals(1, carta.getNaipe());
        assertEquals(1, Carta.menorValor());
        assertEquals(13, Carta.maiorValor());
        assertEquals(0, carta.compareTo(outra));
        assertEquals(0, Carta.primeiroNaipe());
        assertEquals(3, Carta.ultimoNaipe());
        assertTrue(carta.equals(outra));
        String frase = "AS de OUROS";
        // (1) Perguntar pra professora por que assertNotSame tem o primeiro argumento identifcado no...
        // ... vsCode como "unexpected" (assim não deveriar reprovar no teste quando a == b?): 
        assertNotSame(frase, carta.toString());
    }
}
