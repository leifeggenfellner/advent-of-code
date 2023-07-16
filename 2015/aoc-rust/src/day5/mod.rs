use regex::Regex;
use std::fs::File;
use std::io::Read;

fn get_input() -> String {
    let mut file = File::open("input/day5.txt").unwrap();
    let mut contents = String::new();
    file.read_to_string(&mut contents).unwrap();
    contents
}

fn has_repeaped_chars(line: &str) -> bool {
    let mut chars = line.chars();
    let mut prev_char = chars.next().unwrap();
    for c in chars {
        if c == prev_char {
            return true;
        }
        prev_char = c;
    }
    false
}

fn part1() -> i32 {
    let input = get_input();
    let bad_strings = ["ab", "cd", "pq", "xy"];
    let vowels = Regex::new(r"(?i)[aeiou]").unwrap();

    let nice_strings = input
        .lines()
        .filter(|line| {
            let has_three_vowels = vowels.find_iter(line).count() >= 3;
            let has_repeated_letter = has_repeaped_chars(line);
            let has_bad_string = bad_strings
                .iter()
                .any(|&bad_string| line.contains(bad_string));
            has_three_vowels && has_repeated_letter && !has_bad_string
        })
        .count();

    nice_strings as i32
}

fn contains_repeated_pair(line: &str) -> bool {
    let chars: Vec<char> = line.chars().collect();

    for i in 0..chars.len() - 3 {
        let pair = &line[i..i + 2];

        if line[i + 2..].contains(pair) {
            return true;
        }
    }

    false
}

fn contains_repeated_letter_with_letter_between(line: &str) -> bool {
    let chars: Vec<char> = line.chars().collect();

    for i in 0..chars.len() - 2 {
        if chars[i] == chars[i + 2] {
            return true;
        }
    }

    false
}

fn part2() -> i32 {
    let input = get_input();

    let mut nice_strings = 0;
    for line in input.lines() {
        let has_repeated_pair = contains_repeated_pair(line);
        let has_repeated_letter = contains_repeated_letter_with_letter_between(line);

        if has_repeated_pair && has_repeated_letter {
            nice_strings += 1;
        }
    }

    nice_strings
}

pub fn solve() {
    println!("Part 1: {}", part1());
    println!("Part 2: {}", part2());
}
