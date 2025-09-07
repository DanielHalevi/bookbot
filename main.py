from stats import get_num_words, char_count, sort_char_count
import sys
def get_book_text(filepath):
    with open(filepath, 'r') as file:
        return file.read()

def main():
    print("============ BOOKBOT ============")
    print(f"Analyzing book at path: {sys.argv[1]}")
    book_text = get_book_text(sys.argv[1])
    print("----------- Word Count ----------")
    print(f"Found {get_num_words(book_text)} total words")
    print("----------- Character Count ----------")
    count = char_count(book_text)
    for char, count in sort_char_count(count):
        print(f"{char}: {count}")
    print("============= END ===============")
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        main()