use std::fs::File;
use std::io::Read;

fn part1(input: &str) -> i32 {
    let mut file = File::open(input).expect("Failed to open file");
    let mut contents = String::new();
    file.read_to_string(&mut contents)
        .expect("Failed to read file");

    let floor = contents.chars().fold(0, |sum, ch| match ch {
        '(' => sum + 1,
        ')' => sum - 1,
        _ => sum,
    });

    return floor;
}

fn part2(input: &str) -> i32 {
    let mut file = File::open(input).expect("Failed to open file");
    let mut contents = String::new();
    file.read_to_string(&mut contents)
        .expect("Failed to read file");

    let mut floor = 0;
    for (index, ch) in contents.chars().enumerate() {
        match ch {
            '(' => floor += 1,
            ')' => floor -= 1,
            _ => panic!("Invalid character: {}", ch),
        }

        if floor == -1 {
            return index as i32 + 1;
        }
    }

    return -1;
}

pub fn solve() {
    let input = "input/day1.txt";
    println!("Part 1: {}", part1(input));
    println!("Part 2: {}", part2(input));
}
