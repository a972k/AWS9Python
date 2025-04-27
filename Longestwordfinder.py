def longest_word(words : list[str]):
    if not words:
        return None
 
    longest = max(words, key=len)
    return longest

list_of_words = ["apple", "banana", "cherry", "blueberry", "strawberry"]
longest = longest_word(list_of_words)   
print(f"The longest word is: {longest}")