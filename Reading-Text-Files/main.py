# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}

def read_file_content(filename):
    # [assignment] Add your code here 
    with open('story.txt') as f:
        text = f.read()
    return text

def count_words():
    text = read_file_content("./story.txt")
    # [assignment] Add your code here
    splited_text = text.split()
    word_count = {}
    for word in splited_text:
        word_count[word] = splited_text.count(word)
    return word_count
print(count_words())
