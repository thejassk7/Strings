print("Question 1: Polindrome Checker: Check whether a word is palindrome or not")
word=input("Write a word to check whether it is polindrome or not")
n=len(word)
new_word=''
i=0
while i<n:
    new_word[i]=word[-(i+1)]
    i=i+1
if new_word==word:
    print("The given word: ",word,"is in Polindrome.")
else:
    print("The given word: ",word,"is not polindrome.")
