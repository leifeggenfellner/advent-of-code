use std::fs::File;
use std::io::Read;

pub fn part1(input: &str) -> i32 {
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
