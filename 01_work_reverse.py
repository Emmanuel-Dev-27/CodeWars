# Write a function that takes in a string of one or more words, and returns the same string, but with all words that have five or more letters reversed (just like the name of this kata). Strings passed in will consist of only letters and spaces. Spaces will be included only when more than one word is present.

# Examples:

# "Hey fellow warriors"  --> "Hey wollef sroirraw" 
# "This is a test        --> "This is a test" 
# "This is another test" --> "This is rehtona test"

def spin_words(sentence):
  words = sentence.split()
  for i in range(len(words)):
    if len(words[i]) >= 5:
      words[i] = words[i][::-1]
  return ' '.join(words)

# Test Cases
print(spin_words("Hey fellow warriors"))  # "Hey wollef sroirraw"
print(spin_words("This is a test"))        # "This is a test"
print(spin_words("This is another test"))  # "This is rehtona test"