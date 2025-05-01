# Basic Text Diff Viewer

A command-line tool to compare two `.txt` files and highlight their differences line by line.

## Features
- Highlights added, removed, and modified lines with color in the terminal
- Supports ignoring case and whitespace
- Supports unified diff format
- Can save the diff result to a separate file

## Usage

```bash
# Basic usage
python text_diff_viewer.py ./file1.txt ./file2.txt

# Ignore case
python text_diff_viewer.py ./file1.txt ./file2.txt --ignore-case

# Ignore whitespace
python text_diff_viewer.py ./file1.txt ./file2.txt --ignore-whitespace

# Unified diff format
python text_diff_viewer.py ./file1.txt ./file2.txt --unified

# Save diff to a file
python text_diff_viewer.py ./file1.txt ./file2.txt --output ./diff_output.txt
