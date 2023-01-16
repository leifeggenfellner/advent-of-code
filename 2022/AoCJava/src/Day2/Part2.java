package Day2;

import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.Hashtable;

public class Part2 {
    public static void main(String[] args) throws IOException {
        BufferedReader input = new BufferedReader(new FileReader("inputs/day2.txt"));

        Hashtable<String, String> draw = new Hashtable<>();
        draw.put("A", "R");
        draw.put("B", "P");
        draw.put("C", "S");

        Hashtable<String, String> playerLosses = new Hashtable<>();
        playerLosses.put("A", "S");
        playerLosses.put("B", "R");
        playerLosses.put("C", "P");

        Hashtable<String, String> playerWins = new Hashtable<>();
        playerWins.put("A", "P");
        playerWins.put("B", "S");
        playerWins.put("C", "R");

        Hashtable<String, String> movePoints = new Hashtable<>();
        movePoints.put("R", "1");
        movePoints.put("P", "2");
        movePoints.put("S", "3");

        int totalPoints = 0;

        String line;

        while ((line = input.readLine()) != null) {
            line = line.trim();
            String[] moves = line.split(" ");

            switch (moves[1]) {
                case "X" -> totalPoints += Integer.parseInt(movePoints.get(playerLosses.get(moves[0])));
                case "Y" -> totalPoints += 3 + Integer.parseInt(movePoints.get(draw.get(moves[0])));
                case "Z" -> totalPoints += 6 + Integer.parseInt(movePoints.get(playerWins.get(moves[0])));
            }
        }

        System.out.println(totalPoints);
    }
}
