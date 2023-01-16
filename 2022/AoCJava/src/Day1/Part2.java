package Day1;

import java.io.BufferedReader;
import java.io.FileReader;
import java.util.ArrayList;
import java.util.List;

public class Part2 {
    public static void main(String[] args) throws Exception {
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
        
        System.out.println(calorieList.get(0) + calorieList.get(1) + calorieList.get(2));
    }
}
