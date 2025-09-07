def get_num_words(text):
    return len(text.split())

def char_count(text):
    text = text.lower()
    return {char: text.count(char) for char in text if char.isalpha()}

def sort_char_count(char_count):
    return sorted(char_count.items(), key=lambda x: x[1], reverse=True)