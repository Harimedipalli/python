# 1. String Manipulation
# Q1: Reverse words in a string

# def reverse_words(s: str) -> str:
#     pass
# Example:
# Input: "hello world"
# Output: "world hello"



# Q2: Check if two strings are rotations of each other

# def are_rotations(s1: str, s2: str) -> bool:
#     pass
# Example:
# Input: "abcd", "dabc"
# Output: True



# Q3: Find all permutations of a given string
# python
# Copy
# Edit
# from itertools import permutations
#
# def string_permutations(s: str) -> list:
#     pass
# Example:
# Input: "abc"
# Output: ["abc", "acb", "bac", "bca", "cab", "cba"]
#
# Q4: Check if a string contains only digits
# python
# Copy
# Edit
# def is_digit_string(s: str) -> bool:
#     pass
# Q5: Replace spaces with '%20' in a string (URL Encoding)
# python
# Copy
# Edit
# def urlify(s: str) -> str:
#     pass
# Example:
# Input: "hello world"
# Output: "hello%20world"
#
# 2. List & Array Manipulation
# Q6: Find the intersection of two lists
# python
# Copy
# Edit
# def list_intersection(list1: list, list2: list) -> list:
#     pass
# Example:
# Input: [1, 2, 3, 4], [2, 3, 5, 6]
# Output: [2, 3]
#
# Q7: Remove duplicates from a list without using set()
# python
# Copy
# Edit
# def remove_duplicates(arr: list) -> list:
#     pass
# Q8: Rotate an array left by k positions
# python
# Copy
# Edit
# def rotate_left(arr: list, k: int) -> list:
#     pass
# Q9: Find the subarray with the maximum sum (Kadane’s Algorithm)
# python
# Copy
# Edit
# def max_subarray_sum(arr: list) -> int:
#     pass
# Q10: Find the first duplicate element in a list
# python
# Copy
# Edit
# def first_duplicate(arr: list) -> int:
#     pass
# 3. Dictionary & Set Problems
# Q11: Find the word frequency in a given sentence
# python
# Copy
# Edit
# def word_frequency(sentence: str) -> dict:
#     pass
# Q12: Check if two strings are anagrams using a dictionary
# python
# Copy
# Edit
# def are_anagrams_dict(s1: str, s2: str) -> bool:
#     pass
# Q13: Find the common keys in two dictionaries
# python
# Copy
# Edit
# def common_keys(dict1: dict, dict2: dict) -> list:
#     pass
# Q14: Convert a list of tuples into a dictionary
# python
# Copy
# Edit
# def list_to_dict(pairs: list) -> dict:
#     pass
# 4. Number Problems
# Q15: Count the number of digits in a number
# python
# Copy
# Edit
# def count_digits(n: int) -> int:
#     pass
# Q16: Find the sum of all digits in a number
# python
# Copy
# Edit
# def sum_of_digits(n: int) -> int:
#     pass
# Q17: Find all prime numbers in a range
# python
# Copy
# Edit
# def primes_in_range(start: int, end: int) -> list:
#     pass
# Q18: Find the square root of a number without using math.sqrt()
# python
# Copy
# Edit
# def sqrt(n: int) -> float:
#     pass
# Q19: Check if a number is a palindrome
# python
# Copy
# Edit
# def is_palindrome_number(n: int) -> bool:
#     pass
# 5. Sorting & Searching
# Q20: Implement selection sort
# python
# Copy
# Edit
# def selection_sort(arr: list) -> list:
#     pass
# Q21: Find the kth smallest element in an array
# python
# Copy
# Edit
# def kth_smallest(arr: list, k: int) -> int:
#     pass
# Q22: Implement a linear search algorithm
# python
# Copy
# Edit
# def linear_search(arr: list, target: int) -> int:
#     pass
# Q23: Find the missing number in a list using XOR
# python
# Copy
# Edit
# def missing_number_xor(arr: list, n: int) -> int:
#     pass
# 6. Recursion Problems
# Q24: Find the nth Fibonacci number using recursion
# python
# Copy
# Edit
# def fibonacci_recursive(n: int) -> int:
#     pass
# Q25: Calculate the power of a number using recursion
# python
# Copy
# Edit
# def power_recursive(x: int, y: int) -> int:
#     pass
# Q26: Implement recursive binary search
# python
# Copy
# Edit
# def binary_search_recursive(arr: list, target: int, left: int, right: int) -> int:
#     pass
# 7. File Handling
# Q27: Count the number of words in a text file
# python
# Copy
# Edit
# def count_words(filename: str) -> int:
#     pass
# Q28: Write data to a file and then read it back
# python
# Copy
# Edit
# def write_and_read_file(filename: str, data: str):
#     pass
# Q29: Find the longest word in a file
# python
# Copy
# Edit
# def longest_word_in_file(filename: str) -> str:
#     pass
# 8. OS & Automation
# Q30: Check if a file exists in a given directory
# python
# Copy
# Edit
# import os
#
# def file_exists(directory: str, filename: str) -> bool:
#     pass
# Q31: Delete all .log files from a directory
# python
# Copy
# Edit
# import os
#
# def delete_log_files(directory: str):
#     pass
# Q32: Zip all files in a directory
# python
# Copy
# Edit
# import shutil
#
# def zip_directory(source_dir: str, zip_name: str):
#     pass
# 9. Multi-threading & Concurrency
# Q33: Run a function in multiple threads
# python
# Copy
# Edit
# import threading
#
# def run_threads():
#     pass
# Q34: Use a queue for inter-thread communication
# python
# Copy
# Edit
# import queue
#
# def producer(q):
#     pass
#
# def consumer(q):
#     pass
# 10. Web Scraping & APIs
# Q35: Extract all links from a webpage using requests and BeautifulSoup
# python
# Copy
# Edit
# import requests
# from bs4 import BeautifulSoup
#
# def extract_links(url: str) -> list:
#     pass
# Q36: Fetch data from a REST API and process JSON response
# python
# Copy
# Edit
# import requests
#
# def fetch_api_data(api_url: str) -> dict:
#     pass
# Final Thoughts
# ✅ Covers all fundamental Python concepts
# ✅ Questions are practical, not just theoretical
# ✅ No tricky algorithms—perfect for automation & scripting
#
# If you want solutions or explanations for any of these, let me know! 🚀
#
#
#
#
#
# You said:
# I want without using built in methos coding question later I will compare those with whether any easy way to write using built inmethods or not
# ChatGPT said:
# Got it! Below are Python problem-solving questions that require manual implementation without using built-in methods (like sort(), reverse(), max(), etc.). Later, you can compare with built-in approaches for efficiency.
#
# 1. String Manipulation (Without Built-in Methods)
# Q1: Reverse a string manually
# python
# Copy
# Edit
# def reverse_string(s: str) -> str:
#     pass
# Compare with: s[::-1]
#
# Q2: Convert lowercase to uppercase and vice versa (without .lower() or .upper())
# python
# Copy
# Edit
# def swap_case(s: str) -> str:
#     pass
# Compare with: s.swapcase()
#
# Q3: Check if a string is a palindrome (without using [::-1] or reversed())
# python
# Copy
# Edit
# def is_palindrome(s: str) -> bool:
#     pass
# Q4: Find the length of a string without using len()
# python
# Copy
# Edit
# def string_length(s: str) -> int:
#     pass
# Q5: Count occurrences of a character in a string without .count()
# python
# Copy
# Edit
# def char_count(s: str, char: str) -> int:
#     pass

# 2. List & Array Problems (Without Built-in Methods)
# Q6: Find the maximum element in a list without max()

# def find_max(arr: list) -> int:
#     pass
""" Completed """

# Q7: Find the minimum element in a list without min()

# def find_min(arr: list) -> int:
#     pass

""" Completed """

# Q8: Reverse a list manually (without [::-1] or reversed())
# python
# Copy
# Edit
# def reverse_list(arr: list) -> list:
#     pass
# Q9: Sort a list using bubble sort (without sort())
# python
# Copy
# Edit
# def bubble_sort(arr: list) -> list:
#     pass
# Q10: Find the sum of elements in a list without sum()
# python
# Copy
# Edit
# def list_sum(arr: list) -> int:
#     pass
# 3. Dictionary & Set Problems (Without Built-in Methods)
# Q11: Count word frequency in a string manually
# python
# Copy
# Edit
# def word_frequency(s: str) -> dict:
#     pass
# Q12: Find common elements between two lists without set()
# python
# Copy
# Edit
# def list_intersection(list1: list, list2: list) -> list:
#     pass
# Q13: Merge two dictionaries without using update()
# python
# Copy
# Edit
# def merge_dicts(d1: dict, d2: dict) -> dict:
#     pass
# Q14: Find the first non-repeating character in a string (without collections.Counter)
# python
# Copy
# Edit
# def first_unique_char(s: str) -> str:
#     pass
# 4. Number Problems (Without Built-in Methods)
# Q15: Find factorial using recursion (without math.factorial())
# python
# Copy
# Edit
# def factorial(n: int) -> int:
#     pass
# Q16: Find the nth Fibonacci number (without memoization or lru_cache)
# python
# Copy
# Edit
# def fibonacci(n: int) -> int:
#     pass
# Q17: Check if a number is prime (without math.sqrt() or isprime())
# python
# Copy
# Edit
# def is_prime(n: int) -> bool:
#     pass
# Q18: Find the Greatest Common Divisor (GCD) without math.gcd()
# python
# Copy
# Edit
# def gcd(a: int, b: int) -> int:
#     pass
# 5. Searching & Sorting (Without Built-in Methods)
# Q19: Implement linear search
# python
# Copy
# Edit
# def linear_search(arr: list, target: int) -> int:
#     pass
# Q20: Implement binary search (without bisect or index())
# python
# Copy
# Edit
# def binary_search(arr: list, target: int) -> int:
#     pass
# Q21: Implement insertion sort
# python
# Copy
# Edit
# def insertion_sort(arr: list) -> list:
#     pass
# 6. Recursion Problems (Without Built-in Methods)
# Q22: Reverse a string using recursion
# python
# Copy
# Edit
# def reverse_recursive(s: str) -> str:
#     pass
# Q23: Find power of a number without ** or math.pow()
# python
# Copy
# Edit
# def power(x: int, y: int) -> int:
#     pass
# Q24: Sum of digits of a number recursively
# python
# Copy
# Edit
# def sum_of_digits(n: int) -> int:
#     pass
# 7. File Handling (Without Built-in Methods)
# Q25: Count the number of lines in a file manually
# python
# Copy
# Edit
# def count_lines(filename: str) -> int:
#     pass
# Q26: Read a file without readlines()
# python
# Copy
# Edit
# def read_file(filename: str):
#     pass
# 8. OS & Automation (Without Built-in Methods)
# Q27: List all files in a directory without os.listdir()
# python
# Copy
# Edit
# def list_files(directory: str) -> list:
#     pass
# Q28: Check if a file exists manually
# python
# Copy
# Edit
# def file_exists(filepath: str) -> bool:
#     pass
# 9. Multi-threading & Concurrency (Without Built-in Methods)
# Q29: Implement a thread that prints numbers
# python
# Copy
# Edit
# import threading
#
# def print_numbers():
#     pass
# Q30: Implement a producer-consumer model using queue
# python
# Copy
# Edit
# import queue
#
# def producer(q):
#     pass
#
# def consumer(q):
#     pass