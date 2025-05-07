import os
import difflib
import argparse
from colorama import Fore, Style, init


init(autoreset=True)

def normalize_lines(lines, ignore_case, ignore_whitespace):
   
    normalized = []
    for line in lines:
        if ignore_whitespace:
            line = ' '.join(line.split())
        if ignore_case:
            line = line.lower()
        normalized.append(line + '\n')
    return normalized

def compare_files(file1_path, file2_path, ignore_case=False, ignore_whitespace=False, output_file=None, use_unified=False):
   
    try:
        with open(file1_path, 'r') as f1, open(file2_path, 'r') as f2:
            f1_lines = f1.readlines()
            f2_lines = f2.readlines()
    except FileNotFoundError as e:
        print(Fore.RED + f"Error: {e}")
        return

    f1_norm = normalize_lines(f1_lines, ignore_case, ignore_whitespace)
    f2_norm = normalize_lines(f2_lines, ignore_case, ignore_whitespace)

    
    if use_unified:
        diff = difflib.unified_diff(
            f1_norm, f2_norm,
            fromfile=file1_path,
            tofile=file2_path,
            lineterm=''
        )
    else:
        diff = difflib.ndiff(f1_norm, f2_norm)

    print(Fore.CYAN + f"\nComparing '{file1_path}' and '{file2_path}':\n" + Style.RESET_ALL)

    result = ""  

    for line in diff:
        result += line + '\n' 

        if not use_unified:
            if line.startswith('+ '):
                print(Fore.GREEN + line)
            elif line.startswith('- '):
                print(Fore.RED + line)
            elif line.startswith('? '):
                print(Fore.YELLOW + line)
            else:
                print(line, end='')
        else:

            print(line)

    if output_file:
        try:
            with open(output_file, 'w') as output:
                output.write(result)
            print(Fore.CYAN + f"\n\nDiff saved to '{output_file}'")
        except IOError as e:
            print(Fore.RED + f"Error writing to file: {e}")

def main():
    parser = argparse.ArgumentParser(description="Compare two text files line by line.")
    parser.add_argument("file1", help="Path to the first text file")
    parser.add_argument("file2", help="Path to the second text file")
    parser.add_argument("--ignore-case", action="store_true", help="Ignore case differences")
    parser.add_argument("--ignore-whitespace", action="store_true", help="Ignore whitespace differences")
    parser.add_argument("--output", help="Save diff result to a file")
    parser.add_argument("--unified", action="store_true", help="Use unified diff format instead of default")

    args = parser.parse_args()

    compare_files(
        args.file1,
        args.file2,
        ignore_case=args.ignore_case,
        ignore_whitespace=args.ignore_whitespace,
        output_file=args.output,
        use_unified=args.unified
    )

if __name__ == "__main__":
    main()
