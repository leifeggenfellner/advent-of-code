import java.io.BufferedReader;
import java.io.FileReader;
import java.util.ArrayList;
import java.util.List;

public class Day1 {
    public static void main(String[] args) throws Exception {
        System.out.println(solvePart1());
        System.out.println(solvePart2());
    }

    private static int solvePart1() throws Exception {
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

        return mostCalories;
    }

    private static int solvePart2() throws Exception {
        BufferedReader input = new BufferedReader((new FileReader("inputs/day1.txt")));

        String line;
        int calories = 0;

        List<Integer> calorieList = new ArrayList<>();

        while ((line = input.readLine()) != null) {
            String strCal = line.trim();

            if (strCal.isBlank()) {
                calorieList.add(calories);
                calories = 0;
                continue;
            }

            calories += Integer.parseInt(strCal);
        }

        calorieList.add(calories);

        calorieList.sort((a, b) -> b - a);
        return calorieList.get(0) + calorieList.get(1) + calorieList.get(2);
    }
}