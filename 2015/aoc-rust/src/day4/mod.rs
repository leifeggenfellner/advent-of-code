use std::fs::File;
use std::io::Read;

fn get_input() -> String {
    let mut file = File::open("input/day4.txt").unwrap();
    let mut contents = String::new();
    file.read_to_string(&mut contents).unwrap();
    contents
}

fn part1() -> i32 {
    let input = get_input();
    let mut i = 100_000;
    loop {
        let hash_string = format!("{}{}", input, i);
        let hash = md5::compute(hash_string);

        let hash_hex = format!("{:x}", hash);
        if hash_hex.starts_with("00000") {
            return i as i32;
        }
        i += 1;
    }
}

fn part2() -> i32 {
    let input = get_input();
    let mut i = 1_000_000;
    loop {
        let hash_string = format!("{}{}", input, i);
        let hash = md5::compute(hash_string);

        let hash_hex = format!("{:x}", hash);
        if hash_hex.starts_with("000000") {
            return i as i32;
        }
        i += 1;
    }
}

pub fn solve() {
    println!("Part 1: {}", part1());
    println!("Part 2: {}", part2());
}
