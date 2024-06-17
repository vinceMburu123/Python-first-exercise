def sort_words_by_length(words):
    # Use the sort method with key=len to sort the words by their length
    words.sort(key=len)
    return words

# Example usage
words_list = ["Berries", "Pineapple", "cherry", "dates", "fig", "grape"]
sorted_list = sort_words_by_length(words_list)
print(f"Words sorted by length: {sorted_list}")

