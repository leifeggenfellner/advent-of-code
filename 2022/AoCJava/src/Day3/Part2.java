package Day3;

import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.HashSet;
import java.util.List;
import java.util.Set;

public class Part2 {
    public static void main(String[] args) throws IOException {
        BufferedReader input = new BufferedReader(new FileReader("inputs/day3.txt"));

        int score = 0;

        String alphabet = "0abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ";


        List<Set<Integer>> lists = new ArrayList<>();
        lists.add(new HashSet<>());
        lists.add(new HashSet<>());
        lists.add(new HashSet<>());

        int listIndex = 0;
        String line;

        while ((line = input.readLine()) != null) {
            for (String e : line.split("")) {
                lists.get(listIndex).add(alphabet.indexOf(e));
            }

            listIndex++;
            if (listIndex < 3) {
                continue;
            }

            lists.get(0).retainAll(lists.get(1));
            lists.get(0).retainAll(lists.get(2));

            score += lists.get(0).stream().reduce(Integer::sum).orElseThrow();

            lists = new ArrayList<>();
            lists.add(new HashSet<>());
            lists.add(new HashSet<>());
            lists.add(new HashSet<>());
            listIndex = 0;
        }

        System.out.println(score);
    }
}
