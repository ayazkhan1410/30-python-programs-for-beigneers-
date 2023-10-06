'''Day 5 of '30 days of 30
   Programs challenege '''
def word_count(word_list):
    #there's an empty dictionary called count
    count = {}
    #It goes through each word in the given list of words.
    for word in word_list:
         #This checks if the current word is already
         # a key in the count dictionary.
        if word in count:
             #it means we've seen it before.
             # So, count[word] += 1
            count[word]+=1
        else:
            #If the word is not in the dictionary 
            # (it's new)
            count[word]=1
    return count
    
txt = input('Enter Words : ')
print(word_count(txt))