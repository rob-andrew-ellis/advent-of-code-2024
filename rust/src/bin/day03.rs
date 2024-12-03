use regex::Regex;
use std::{error::Error, fs};

fn mul(data: &str) -> i32 {
    let re = Regex::new(r"mul\((\d{1,3}),(\d{1,3})\)").unwrap();
    let mut num_pairs = vec![];

    for (_, [num1, num2]) in re.captures_iter(data).map(|c| c.extract()) {
        num_pairs.push((num1, num2));
    }

    num_pairs
        .iter()
        .map(|(a, b)| a.parse::<i32>().unwrap() * b.parse::<i32>().unwrap())
        .sum()
}

fn conditional_mul(data: &str) -> i32 {
    let re = Regex::new(r"mul\(\d{1,3},\d{1,3}\)|do\(\)|don\'t\(\)").unwrap();

    let commands: Vec<String> = re
        .captures_iter(data)
        .map(|cap| cap[0].to_string())
        .collect();

    let mut muls = vec![];
    let mut do_mul = true;

    for command in commands {
        if command == "do()" {
            do_mul = true;
        } else if command == "don't()" {
            do_mul = false;
        } else if do_mul {
            muls.push(command);
        }
    }

    muls.iter()
        .map(|mul| {
            let re = Regex::new(r"\d+").unwrap();
            let nums: Vec<i32> = re
                .find_iter(mul)
                .map(|mat| mat.as_str().parse().unwrap())
                .collect();

            nums[0] * nums[1]
        })
        .sum()
}

fn main() -> Result<(), Box<dyn Error>> {
    let corrupt_data = fs::read_to_string("data/day03.txt")?;

    println!("{}", mul(&corrupt_data));
    println!("{}", conditional_mul(&corrupt_data));

    Ok(())
}
