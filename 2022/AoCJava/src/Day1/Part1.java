package Day1;

import java.io.BufferedReader;
import java.io.FileReader;

public class Part1 {
    public static void main(String[] args) throws Exception {
        BufferedReader input = new BufferedReader((new FileReader("inputs/day1.txt")));

        String line;
        int calories = 0;
        int mostCalories = 0;

        while ((line = input.readLine()) != null) {
            line = line.trim();

            if (line.isBlank()) {
                if (calories > mostCalories) {
                    mostCalories = calories;
                }

                calories = 0;
                continue;
            }

            calories += Integer.parseInt(line);
        }

        System.out.println(mostCalories);
    }
}
