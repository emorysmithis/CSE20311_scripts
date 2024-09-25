import re
import argparse
from collections import Counter

def extract_numbers_from_file(file_path):
    """Extract all numbers from a file and return them as a list of integers."""
    try:
        with open(file_path, 'r') as file:
            content = file.read()
            # Use regex to find all numbers in the file
            numbers = re.findall(r'\d+', content)
            # Convert numbers to a list of integers
            return list(map(int, numbers))
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
        return None
    except Exception as e:
        print(f"Error reading '{file_path}': {e}")
        return None

def compare_files(file1, file2):
    """Compare if two files contain the same numbers and output the differences."""
    numbers_file1 = extract_numbers_from_file(file1)
    numbers_file2 = extract_numbers_from_file(file2)
    
    # If any of the files failed to load, stop the comparison
    if numbers_file1 is None or numbers_file2 is None:
        return

    # Use Counter to count frequency of each number
    count_file1 = Counter(numbers_file1)
    count_file2 = Counter(numbers_file2)
    
    if count_file1 == count_file2:
        print("The files contain the same set of numbers (with the same frequency).")
    else:
        print("The files do not contain the same set of numbers.")
        print(f"Number of numbers in {file1}: {len(numbers_file1)}")
        print(f"Number of numbers in {file2}: {len(numbers_file2)}")
        
        # Find differences
        numbers_in_file1_not_in_file2 = count_file1 - count_file2
        numbers_in_file2_not_in_file1 = count_file2 - count_file1
        
        if numbers_in_file1_not_in_file2:
            print(f"Numbers in {file1} but not in {file2}:")
            for number, count in numbers_in_file1_not_in_file2.items():
                print(f"Number {number} occurs {count} time(s)")
        
        if numbers_in_file2_not_in_file1:
            print(f"Numbers in {file2} but not in {file1}:")
            for number, count in numbers_in_file2_not_in_file1.items():
                print(f"Number {number} occurs {count} time(s)")

def main():
    parser = argparse.ArgumentParser(description="Compare if two files contain the same numbers.")
    parser.add_argument("file1", type=str, help="Path to the first file")
    parser.add_argument("file2", type=str, help="Path to the second file")
    
    args = parser.parse_args()
    
    compare_files(args.file1, args.file2)

if __name__ == "__main__":
    main()
