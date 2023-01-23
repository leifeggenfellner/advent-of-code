package Day4;

import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;

public class Part2 {
    public static void main(String[] args) throws IOException {
        BufferedReader input = new BufferedReader(new FileReader("inputs/day4.txt"));

        int noOverlap = 0;
        int all = 0;

        String line;
        while ((line = input.readLine()) != null) {
            String[] elfAssign = line.split(",");
            String[] assign1 = elfAssign[0].split("-");
            String[] assign2 = elfAssign[1].split("-");

            int assign1Low = Integer.parseInt(assign1[0]);
            int assign1High = Integer.parseInt(assign1[1]);
            int assign2Low = Integer.parseInt(assign2[0]);
            int assign2High = Integer.parseInt(assign2[1]);

            if (assign1Low > assign2High) {
                noOverlap++;
            } else if (assign2Low > assign1High) {
                noOverlap++;
            }

            all++;
        }

        System.out.println(all - noOverlap);
    }
}
