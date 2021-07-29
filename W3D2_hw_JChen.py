'''
Exercise 1: Reverse the list below using in place algorithm.
'''
words = ['this' , 'is', 'a', 'sentence', '.']

def reverseWords(word_list, x, y):
    word_list[x], word_list[y] = word_list[y], word_list[x]
    return word_list

for n in range(len(words)//2):
    reversedWords = reverseWords(words, n, len(words)-1-n)

print(reversedWords)



'''
Exercise 2: Create a function that counts how many distinct words are in the string below,
then outputs a dictionary with the words as the key and the value as the amount of times that
word appears in the string.
Should output:
{'a': 5,
'abstract': 1,
'an': 3,
'array': 2, ... etc...
'''
a_text = 'In computing, a hash table hash map is a data structure which implements an associative array abstract data type, a structure that can map keys to values. A hash table uses a hash function to compute an index into an array of buckets or slots from which the desired value can be found'

def distinctWords(input_text):
    output_text = {}
    input_text = input_text.lower().split()
    input_text.sort()
    for index in range(len(input_text)):
        if input_text[index] not in output_text:
            output_text[input_text[index]] = 1
        else:
            output_text[input_text[index]] += 1
    return output_text

print(distinctWords(a_text))



'''
Exercise 3: Write a program to implement a Linear Search Algorithm. Also in a comment, write the
Time Complexity of the following algorithm.
Hint: Linear Searching will require searching a list for a given number.
'''
def linearSearch(input_list, target):
    for index in range(len(input_list)):
        if target == input_list[index]:
            return print(f'Your searched word, "{target}", is {index+1} words from the beginning')

list1 = [1,1,1,1,1,1,1,2,3,4,5,6,7]
linearSearch(list1, 7)
print(len(list1))