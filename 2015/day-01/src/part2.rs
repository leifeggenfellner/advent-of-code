use std::fs::File;
use std::io::Read;

pub fn part2(input: &str) -> i32 {
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
