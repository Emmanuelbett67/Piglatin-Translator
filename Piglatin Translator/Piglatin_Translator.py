print ('Welcome to the Pig Latin Translator!')
#first rule of piglatin adding ay at the end
pyg = 'ay'

# word from the user
original = input('Enter a word:') 

#control flow
if len(original) > 0 and original.isalpha(): # just to make sure the user has entered a string and the string doesn't contain non-letter characters
  word = original.lower() #turn the word to lower case
  first = word[0] #extract the first letter
  new_word = word + first + pyg #second rule of piglatin 
  new_word = new_word[1:len(new_word)]
  print(new_word)
else:
  print ('empty')


