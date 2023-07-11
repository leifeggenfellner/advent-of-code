mod part1;
mod part2;

use part1::part1;
use part2::part2;

fn main() {
    let input = "data/input.txt";
    let ans1 = part1(input);
    let ans2 = part2(input);

    println!("Part 1: {}", ans1);
    println!("Part 2: {}", ans2);
}
