// TODO: Complete
use std::fs::read_to_string;

fn read_input(file_path: &str) -> Vec<Vec<char>> {
    let input = read_to_string(file_path).unwrap();

    input.lines().map(|line| line.chars().collect()).collect()
}

fn part1(data: &Vec<Vec<char>>) -> i32 {
    let targets = (('X', 'M', 'A', 'S'), ('S', 'A', 'M', 'X'));
    let num_found = 0;

    return 0;
}

fn main() {
    let data = read_input("data/day04.rs");
}
