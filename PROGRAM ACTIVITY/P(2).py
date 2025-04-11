def word_count_with_frequency(Sentence):
 words = Sentence.split()
 total_words = len(words)
 word_frequency = {}
 for word in words:
   word = word.lower().strip(",.!?;")
   word_frequency[word] = word_frequency.get(word, 0) + 1
return total_words, word_frequency

# Example usage
Sentence = "This is a test. This test is simple!"
total_frequency = word_count_with_frequency(Sentence)
print (f"total word count: {total}")
print (f"word frequency": frequency)
