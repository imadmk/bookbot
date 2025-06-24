from stats import get_num_words, get_char_count, get_sorted_char_count
import sys

def get_book_text(filepath):
  with open(filepath) as f:
    return f.read()

def main():
  if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

  texts = get_book_text(sys.argv[1])
  words_count = get_num_words(texts)
  char_count = get_char_count(texts)
  char_count_sorted = get_sorted_char_count(char_count)
  print("============ BOOKBOT ============")
  print(f"Analyzing book found at {sys.argv[1]}...")
  print("----------- Word Count ----------")
  print(f"Found {words_count} total words")
  print("--------- Character Count -------")
  for char in char_count_sorted:
    print(f"{char["char"]}: {char["num"]}")
  print("============= END ===============")
main()