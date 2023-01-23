package Day3;

import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.Arrays;
import java.util.HashSet;
import java.util.Set;

public class Part1 {
    public static void main(String[] args) throws IOException {
        BufferedReader input = new BufferedReader(new FileReader("inputs/day3.txt"));

        int score = 0;

        String line;
        String alphabet = "0abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ";

        while ((line = input.readLine()) != null) {
            int[] chars = new int[line.length()];
            int i = 0;
            for (String e : line.split("")) {
                chars[i] = alphabet.indexOf(e);
                i++;
            }

            int[] first = Arrays.copyOfRange(chars, 0, chars.length / 2);
            int[] second = Arrays.copyOfRange(chars, chars.length / 2, chars.length);

            Set<Integer> scores = new HashSet<>();
            for (int firstChar : first) {
                for (int secondChar : second) {
                    if (firstChar == secondChar) {
                        scores.add(firstChar);
                    }
                }
            }

            score += scores.stream().reduce(Integer::sum).orElseThrow();
        }

        System.out.println(score);
    }
}
