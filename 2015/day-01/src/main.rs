mod part1;
mod part2;

use part1::part1;
use part2::part2;

fn main() {
    let ans1: i32 = part1("data/input.txt");
    let ans2: i32 = part2("data/input.txt");

    println!("Part 1: {}", ans1);
    println!("Part 2: {}", ans2);
}
