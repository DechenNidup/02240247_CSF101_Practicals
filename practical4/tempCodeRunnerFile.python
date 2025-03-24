import re
from collections import Counter

def read_file(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
        return ""

def count_lines(content):
    return len(content.split('\n'))

def count_words(content):
    words = re.findall(r'\b\w+\b', content.lower())
    return len(words)

def most_common_word(content):
    words = re.findall(r'\b\w+\b', content.lower())
    word_counts = Counter(words)
    return word_counts.most_common(1)[0] if word_counts else ("", 0)

def average_word_length(content):
    words = re.findall(r'\b\w+\b', content)
    if not words:
        return 0
    total_length = sum(len(word) for word in words)
    return total_length / len(words)

def count_unique_words(content):
    words = re.findall(r'\b\w+\b', content.lower())
    return len(set(words))

def longest_word(content):
    words = re.findall(r'\b\w+\b', content)
    return max(words, key=len) if words else ""

def count_specific_word(content, target_word):
    words = re.findall(r'\b\w+\b', content.lower())
    return words.count(target_word.lower())

def percentage_longer_than_average(content):
    words = re.findall(r'\b\w+\b', content)
    if not words:
        return 0
    avg_length = average_word_length(content)
    longer_words = [word for word in words if len(word) > avg_length]
    return (len(longer_words) / len(words)) * 100

def analyze_text(filename):
    content = read_file(filename)
    if not content:
        return
    
    num_lines = count_lines(content)
    num_words = count_words(content)
    common_word, count = most_common_word(content)
    avg_length = average_word_length(content)
    unique_count = count_unique_words(content)
    long_word = longest_word(content)
    percentage_longer = percentage_longer_than_average(content)
    
    print(f"File: {filename}")
    print(f"Number of lines: {num_lines}")
    print(f"Number of words: {num_words}")
    print(f"Most common word: '{common_word}' (appears {count} times)")
    print(f"Average word length: {avg_length:.2f} characters")
    print(f"Number of unique words: {unique_count}")
    print(f"Longest word: {long_word}")
    print(f"Percentage of words longer than average length: {percentage_longer:.2f}%")
    
    word_to_count = input("Enter a word to count its occurrences: ").strip()
    if word_to_count:
        word_count = count_specific_word(content, word_to_count)
        print(f"Occurrences of '{word_to_count}': {word_count}")
    else:
        print("No word entered.")

# Run the analysis
analyze_text('sample.txt')
