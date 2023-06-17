# Reverse each word of a string

def reverse_words(Sentence):
    
    words = Sentence.split(" ")

    # reverse each word using ::-1
    new_word_list = [word[::-1] for word in words]
    
    # Joining the new list of words
    result_str = " ".join(new_word_list)
    return result_str

# Given String
my_str = "My Name is Kunjan"
print(reverse_words(my_str))
