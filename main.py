def main():
    book_path = "./books/frankenstein.txt"
    report_count(book_path)



def get_book_text(path):
    with open(path) as f:
        return f.read()


def count_words(book_text):
    return len(book_text.split())


def count_characters(book_text):
    count = {}
    for char in book_text.lower():
        if char not in count:
            count[char] = 0
        count[char] += 1
    return count


def report_count(path):
    book_text = get_book_text(path)
    word_count = count_words(book_text)
    
    character_count = count_characters(book_text)
    letters = []

    for key in character_count:
        if key.isalpha():
            letters.append({'character': key, 'count': character_count[key]})

    def sort_on(dict):
        return dict['count']

    letters.sort(reverse=True, key=sort_on)

    print(f"--- Begin report of {path} ---")
    print(f"{word_count} words found in the document\n\n")
    for letter in letters:
        print(f"The '{letter['character']}' character was found {letter['count']} times")
    
    print("--- End report ---")


main()
