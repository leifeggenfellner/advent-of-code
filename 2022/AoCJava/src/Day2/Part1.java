package Day2;

import java.io.BufferedReader;
import java.io.FileReader;
import java.util.Hashtable;

public class Part1 {
    public static void main(String[] args) throws Exception {
        BufferedReader input = new BufferedReader(new FileReader("inputs/day2.txt"));
        
        Hashtable<String, String> equivalentMoves = new Hashtable<>();
        equivalentMoves.put("X", "A");
        equivalentMoves.put("Y", "B");
        equivalentMoves.put("Z", "C");

        Hashtable<String, String> playerWins = new Hashtable<>();
        playerWins.put("Y", "A");
        playerWins.put("Z", "B");
        playerWins.put("X", "C");

        Hashtable<String, String> movePoints = new Hashtable<>();
        movePoints.put("X", "1");
        movePoints.put("Y", "2");
        movePoints.put("Z", "3");

        int totalPoints = 0;

        String line;

        while ((line = input.readLine()) != null) {
            line = line.trim();
            String[] moves = line.split(" ");
            totalPoints += Integer.parseInt(movePoints.get(moves[1]));

            if (moves[0].equals(equivalentMoves.get(moves[1]))) {
                totalPoints += 3;
            } else if (moves[0].equals(playerWins.get(moves[1]))) {
                totalPoints += 6;
            }
        }

        System.out.println(totalPoints);
    }
}
