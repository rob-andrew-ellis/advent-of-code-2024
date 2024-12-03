use std::{
    error::Error,
    fs::File,
    io::{BufRead, BufReader},
};

fn read_reports(file_path: &str) -> Result<Vec<Vec<i32>>, Box<dyn Error>> {
    let file = File::open(file_path)?;
    let reader = BufReader::new(file);

    let mut all_reports: Vec<Vec<i32>> = Vec::new();

    for line in reader.lines() {
        let line = line?;
        let numbers: Vec<&str> = line.split_whitespace().collect();

        let report: Vec<i32> = numbers
            .iter()
            .map(|&num_str| num_str.parse().unwrap())
            .collect();

        all_reports.push(report);
    }

    Ok(all_reports)
}

fn report_is_safe(report: &[i32]) -> bool {
    let diffs: Vec<i32> = report.windows(2).map(|w| w[1] - w[0]).collect();
    let safe_gaps: bool = diffs.iter().all(|&x| 1 <= x.abs() && x.abs() <= 3);
    let all_positive: bool = diffs.iter().all(|&x| x > 0);
    let all_negative: bool = diffs.iter().all(|&x| x < 0);

    safe_gaps && (all_positive || all_negative)
}

fn problem_dampener(all_reports: &[Vec<i32>]) -> i32 {
    let mut num_safe = 0;

    for report in all_reports {
        if report_is_safe(report) {
            num_safe += 1;
            continue;
        }

        for i in 0..report.len() {
            let mut modified_report = report.clone();
            modified_report.remove(i);

            if report_is_safe(&modified_report) {
                num_safe += 1;
                break;
            }
        }
    }

    num_safe
}

fn main() -> Result<(), Box<dyn Error>> {
    let all_reports = read_reports("data/day02.txt")?;

    let num_safe = all_reports
        .iter()
        .filter(|report| report_is_safe(report))
        .count();

    let num_safe_dampened = problem_dampener(&all_reports);

    println!("Part 1: {}", num_safe);
    println!("Part 2: {}", num_safe_dampened);

    Ok(())
}
