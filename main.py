def main():
    book_path = "books/frankenstein.txt"
    frankenstein = read_book(book_path)

    # read and print frankenstein.txt to console
    print("Main text: \n" + frankenstein)

    # get word count for frankenstein.txt
    print("Word count: \n" + str(count_words(frankenstein)) + "\n")

    # get character counts for frankenstein.txt
    chars = count_chars(frankenstein)
    print(chars)
    print("Character count (sorted): \n" + str(chars))

    # get pretty character report
    print(char_report(chars, book_path))

def read_book(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
        return file_contents

def count_words(book_text):
    return len(book_text.split())

def count_chars(book_text):
    chars = {}
    for char in book_text:
        lchar = char.lower()
        if lchar not in chars:
            chars[lchar] = {"name": lchar, "num": 1}
        else:
            chars[lchar]["num"] += 1
    
    return list(chars.values())

def sort_on(dict):
    return dict["num"]

def char_report(char_dict, path):
    char_dict.sort(reverse=True, key=sort_on)

    report = "--- Begin report of " + path + " ---\n"
    for char in char_dict:
        if char["name"].isalpha():
            report += "The \'" + char["name"] + "\' character was found " + str(char["num"]) + " times.\n"
    
    report += "--- End report ---"
    return report


main()