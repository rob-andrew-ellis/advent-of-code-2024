use std::{
    error::Error,
    fs::File,
    io::{BufRead, BufReader},
};

/// Reads the vertical lists of location IDs into two vectors of integers
fn read_locations(filename: &str) -> Result<(Vec<i32>, Vec<i32>), Box<dyn Error>> {
    let file = File::open(filename)?;
    let reader = BufReader::new(file);

    let mut list1 = Vec::new();
    let mut list2 = Vec::new();

    for line in reader.lines() {
        let line = line?;
        let numbers: Vec<&str> = line.split_whitespace().collect();

        if numbers.len() == 2 {
            let num1: i32 = numbers[0].parse()?;
            list1.push(num1);

            let num2: i32 = numbers[1].parse()?;
            list2.push(num2);
        }
    }

    list1.sort_unstable();
    list2.sort_unstable();

    Ok((list1, list2))
}

/// Gets the absolute distance between each element in the two lists at the same indices
fn get_distance(list1: &[i32], list2: &[i32]) -> i32 {
    list1
        .iter()
        .zip(list2.iter())
        .map(|(a, b)| (b - a).abs())
        .sum()
}

/// Calculates the similarity score between the two lists, based on the number of occurences of
/// items in list 1 in list 2
fn get_similarity_score(list1: &[i32], list2: &[i32]) -> i32 {
    list1
        .iter()
        .map(|&num| {
            let occurences = list2.iter().filter(|&&x| x == num).count() as i32;
            num * occurences
        })
        .sum()
}

fn main() -> Result<(), Box<dyn Error>> {
    let (list1, list2) = read_locations("data.txt")?;

    println!(
        "The absolute distance between each location ID is: {}",
        get_distance(&list1, &list2)
    );

    println!(
        "The similarity score between the two lists is: {}",
        get_similarity_score(&list1, &list2)
    );

    Ok(())
}
