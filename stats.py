def get_num_words(text):
  words = text.split()
  return len(words)

def get_char_count(text):
  char_dict = {}
  for char in text.lower():
    if char in char_dict:
      char_dict[char] += 1
    else:
      char_dict[char] = 1
  return char_dict

def sort_on(element):
  return element["num"]

def get_sorted_char_count(char_count_dict):
  char_count_sorted_list = []
  for char in char_count_dict:
    if char.isalpha():
      char_count_sorted_list.append({
      "char": char,
      "num": char_count_dict[char]
    })

  char_count_sorted_list.sort(key=sort_on, reverse=True)
  return char_count_sorted_list