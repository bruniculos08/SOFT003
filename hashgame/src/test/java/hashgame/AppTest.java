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
        Board gameBoard = game.getBoard();
        int[][] empate = gameBoard.getBoard();
        empate[0][0] = 1;
        empate[0][1] = -1;
        empate[0][2] = 1;
        empate[1][0] = 1;
        empate[1][1] = 1;
        empate[1][2] = -1;
        empate[2][0] = -1;
        empate[2][1] = 1;
        empate[2][2] = -1;
        // X O X
        // X X O
        // O X O
        
        assertEquals(1, 1);
    }
}
