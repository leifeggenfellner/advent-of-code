use std::collections::HashSet;
use std::fs::File;
use std::io::Read;

fn get_input() -> String {
    let mut file = File::open("input/day3.txt").unwrap();
    let mut contents = String::new();
    file.read_to_string(&mut contents).unwrap();
    contents
}

fn part1() -> i32 {
    let input = get_input();
    let mut coordinates: HashSet<(i32, i32)> = HashSet::new();
    coordinates.insert((0, 0));

    let mut x = 0;
    let mut y = 0;

    for ch in input.chars() {
        match ch {
            '^' => y += 1,
            'v' => y -= 1,
            '>' => x += 1,
            '<' => x -= 1,
            _ => panic!("Unknown character: {}", ch),
        }
        coordinates.insert((x, y));
    }

    coordinates.len() as i32
}

fn part2() -> i32 {
    let input = get_input();
    let mut coordinates: HashSet<(i32, i32)> = HashSet::new();
    coordinates.insert((0, 0));

    let mut santa_x = 0;
    let mut santa_y = 0;

    let mut robot_x = 0;
    let mut robot_y = 0;

    for (index, ch) in input.chars().enumerate() {
        if index % 2 == 0 {
            match ch {
                '^' => santa_y += 1,
                'v' => santa_y -= 1,
                '>' => santa_x += 1,
                '<' => santa_x -= 1,
                _ => panic!("Unknown character: {}", ch),
            }
            coordinates.insert((santa_x, santa_y));
        } else {
            match ch {
                '^' => robot_y += 1,
                'v' => robot_y -= 1,
                '>' => robot_x += 1,
                '<' => robot_x -= 1,
                _ => panic!("Unknown character: {}", ch),
            }
            coordinates.insert((robot_x, robot_y));
        }
    }

    coordinates.len() as i32
}

pub fn solve() {
    println!("Part 1: {}", part1());
    println!("Part 2: {}", part2());
}
