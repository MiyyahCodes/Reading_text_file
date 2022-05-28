# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}
import string

def read_file_content(filename):
    text_file = open(filename)
    text = text_file.read()
    return text

def count_words():
    text = read_file_content("./story.txt")
    text = text.strip()
    text = text.translate(text.maketrans("", "", string.punctuation))
    words = text.lower().split()
    
    count = {}
    for word in words:
        if word in count:
            count[word] = count[word] + 1
        else:
            count[word] = 1
    return count
            
print(count_words())