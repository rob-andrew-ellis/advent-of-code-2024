use std::{collections::HashSet, fs::read_to_string, time::Instant};

fn read_file(file_path: &str, split_char: char) -> Vec<Vec<i32>> {
    let now = Instant::now();

    let input = read_to_string(file_path).unwrap();

    let result = input
        .lines()
        .map(|line| {
            line.split(split_char)
                .filter_map(|s| s.trim().parse().ok())
                .collect()
        })
        .collect();

    println!("read_file:          {:.2?}", now.elapsed());

    return result;
}

fn find_correct_pages(rules: Vec<Vec<i32>>, pages: Vec<Vec<i32>>) -> (i32, Vec<Vec<i32>>) {
    let now = Instant::now();

    let mut correct_pages = Vec::new();
    let mut incorrect_pages = Vec::new();

    for page in pages {
        let page_set: HashSet<i32> = page.clone().into_iter().collect();
        let changes_needed = rules.iter().any(|rule| {
            page_set.contains(&rule[0])
                && page_set.contains(&rule[1])
                && page.iter().position(|&x| x == rule[0]).unwrap()
                    > page.iter().position(|&x| x == rule[1]).unwrap()
        });

        if !changes_needed {
            correct_pages.push(page);
        } else {
            incorrect_pages.push(page);
        }
    }

    let result = (
        correct_pages.iter().map(|page| page[page.len() / 2]).sum(),
        incorrect_pages,
    );

    println!("find_correct_pages: {:.2?}", now.elapsed());

    return result;
}

// FIX: This needs fixing
fn fix_pages(rules: Vec<Vec<i32>>, mut pages: Vec<Vec<i32>>) -> i32 {
    let now = Instant::now();

    let mut fixed_pages = Vec::new();

    while !pages.is_empty() {
        let mut incorrect_pages = Vec::new();
        for page in std::mem::take(&mut pages) {
            let mut changes_made = false;
            let page_set: HashSet<i32> = page.clone().into_iter().collect();
            let mut page = page;
            for rule in &rules {
                if page_set.contains(&rule[0])
                    && page_set.contains(&rule[1])
                    && page.iter().position(|&x| x == rule[0]).unwrap()
                        > page.iter().position(|&x| x == rule[1]).unwrap()
                {
                    let pos1 = page.iter().position(|&x| x == rule[0]).unwrap();
                    let pos2 = page.iter().position(|&x| x == rule[1]).unwrap();

                    if pos1 > pos2 {
                        page.swap(pos1, pos2);
                        changes_made = true;
                    }
                }
            }

            if !changes_made {
                fixed_pages.push(page);
            } else {
                incorrect_pages.push(page);
            }
        }
    }

    let result = fixed_pages.iter().map(|page| page[page.len() / 2]).sum();

    println!("fix_pages:          {:.2?}", now.elapsed());

    return result;
}

fn main() {
    let rules = read_file("data/rules.txt", '|');
    let pages = read_file("data/pages.txt", ',');

    let (correct_sum, incorrect_pages) = find_correct_pages(rules, pages);
    let rules = read_file("data/rules.txt", '|');
    let fixed_sum = fix_pages(rules, incorrect_pages);
    println!("Sum of middle values for fixed pages:   {fixed_sum}");
    println!("Sum of middle values for correct pages: {correct_sum}");
}
