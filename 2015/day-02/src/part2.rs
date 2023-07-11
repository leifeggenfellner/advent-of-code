use std::fs::File;
use std::io::{BufRead, BufReader};

pub fn part2(input: &str) -> i32 {
    let file = File::open(input).expect("File not found");
    let reader = BufReader::new(file);

    let mut total_feet = 0;
    for line in reader.lines() {
        let line = line.unwrap();
        let mut values: Vec<i32> = line.split("x").filter_map(|x| x.parse().ok()).collect();
        values.sort();

        let ribbon = 2 * values[0] + 2 * values[1];
        let bow = values.iter().fold(1, |acc, x| acc * x);
        total_feet += ribbon + bow;
    }

    return total_feet;
}
