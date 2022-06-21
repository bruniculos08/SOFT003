package hashgame;

import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.assertEquals;

/**
 * Unit test for simple App.
 */
class AppTest {
    /**
     * Rigorous Test.
     */
    @Test
    void testApp() {
        TicTacToe game = new TicTacToe();
        // (1) a classe TicTacToe foi alterada para que o resultado da partida fosse armazenando em um atributo...
        // ... result que pode ser retornado pelo novo método adicionado, getResult().
        assertEquals(2, game.getResult());
    }
}
