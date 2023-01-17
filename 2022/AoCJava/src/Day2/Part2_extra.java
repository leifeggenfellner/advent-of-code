package Day2;

import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.HashMap;
import java.util.Map;

public class Part2_extra {
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

            switch (match[1]) {
                case "X" -> {
                    score += loss;
                    if (shapes.get(match[0]) == rock) {
                        score += scissors;
                    } else if (shapes.get(match[0]) == paper) {
                        score += rock;
                    } else if (shapes.get(match[0]) == scissors) {
                        score += paper;
                    }
                }
                case "Y" -> score += draw + shapes.get(match[0]);
                case "Z" -> {
                    score += win;
                    if (shapes.get(match[0]) == rock) {
                        score += paper;
                    } else if (shapes.get(match[0]) == paper) {
                        score += scissors;
                    } else if (shapes.get(match[0]) == scissors) {
                        score += rock;
                    }
                }
            }
        }

        System.out.println(score);
    }
}
