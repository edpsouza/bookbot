def get_num_words(text: str):
    words = text.split()
    # return the number of words in the text
    return len(words)


def get_num_chars(text: str):
    # asign text to lowercase
    text = text.lower()
    chars = {}
    # for each character in text, if character is in chars, increment its value by 1, else add it to chars with value 1
    for c in text:
        if c in chars:
            chars[c] += 1
        else:
            chars[c] = 1
    return chars


def sort_on(items):
    return items["num"]


def sort_chars(counts):
    sorted_list= []
    # for each character and its count in counts, add a dictionary with keys "char" and "num" to items
    for ch, n in counts.items():
        sorted_list.append({"char": ch, "num": n})
    # sort items in reverse order based on the value of "num" key using sort_on function
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list
