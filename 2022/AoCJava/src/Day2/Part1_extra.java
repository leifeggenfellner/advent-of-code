package Day2;

import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.HashMap;
import java.util.Map;

public class Part1_extra {
    static final int rock = 1;
    static final int paper = 2;
    static final int scissors = 3;

    static final int loss = 0;
    static final int draw = 3;
    static final int win = 6;

    public static void main(String[] args) throws IOException {
        Map<String, Integer> shapes = new HashMap<>();
        shapes.put("A", rock);
        shapes.put("B", paper);
        shapes.put("C", scissors);
        shapes.put("X", rock);
        shapes.put("Y", paper);
        shapes.put("Z", scissors);

        BufferedReader input = new BufferedReader(new FileReader("inputs/day2.txt"));

        String line;
        int score = 0;

        while ((line = input.readLine()) != null) {
            String[] match = line.trim().split(" ");

            if (shapes.get(match[0]).equals(shapes.get(match[1]))) {
                score += draw;
            } else if (shapes.get(match[0]) == 1 && shapes.get(match[1]) == 2) {
                score += win;
            } else if (shapes.get(match[0]) == 2 && shapes.get(match[1]) == 3) {
                score += win;
            } else if (shapes.get(match[0]) == 3 && shapes.get(match[1]) == 1) {
                score += win;
            } else {
                score += loss;
            }

            score += shapes.get(match[1]);
        }

        System.out.println(score);
    }
}
