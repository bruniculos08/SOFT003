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

    // Devido ao problema de passagem por valor ou referências
    @Test
    void testApp() {
        TicTacToe game = new TicTacToe();
        int empate[][] = new int[3][3];
        empate[0][0] = 1;
        empate[0][1] = -1;
        empate[0][2] = 1;
        empate[1][0] = 1;
        empate[1][1] = 1;
        empate[1][2] = -1;
        empate[2][0] = -1;
        empate[2][1] = -1;
        empate[2][2] = -1;
        game.setBoard(empate);
        // X O X
        // X X O
        // O X O
        
        // Obs.: alterei os métodos da classe TicTacToe de modo que a método que play() altere...
        // ... o atributo result (proveniente de minhas alteração), de modo que result é igual à 2...
        // ... em caso de empate, e podemos obter o valor de result pelo método getResult.
        assertEquals(2, game.getResult());
    }
}
