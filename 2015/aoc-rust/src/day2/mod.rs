use std::fs::File;
use std::io::{BufRead, BufReader};

fn part1(input: &str) -> i32 {
    let file = File::open(input).expect("File not found");
    let reader = BufReader::new(file);

    let mut total_area = 0;
    for line in reader.lines() {
        let line = line.unwrap();
        let values: Vec<i32> = line.split("x").filter_map(|x| x.parse().ok()).collect();
        let sides: Vec<i32> = vec![
            values[0] * values[1],
            values[1] * values[2],
            values[2] * values[0],
        ];

        let min_side = sides.iter().min().unwrap();
        let circumfrance = sides.iter().fold(0, |acc, x| acc + 2 * x);
        total_area += circumfrance + min_side;
    }

    return total_area;
}

fn part2(input: &str) -> i32 {
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

pub fn solve() {
    let input = "input/day2.txt";
    println!("Part 1: {}", part1(input));
    println!("Part 2: {}", part2(input));
}
