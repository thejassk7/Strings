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
print("Question 2: Character Frequency Map: Counts the occurances of each character in a string")
word=input("Write a word to count occurance of each character in a string.")
word=word.upper()
n=len(word)
i=0
a=0
b=0
c=0
d=0
e=0
f=0
g=0
h=0
i1=0
j=0
k=0
l=0
m=0
n=0
o=0
p=0
q=0
r=0
s=0
t=0
u=0
v=0
w=0
x=0
y=0
z=0
while i<n:
    if word[i]=='A':
        a=a+1
        i=i+1
    elif word[i]=='B':
        b=b+1
        i=i+1
    elif word[i]=='C':
        c=c+1
        i=i+1
    elif word[i]=='D':
        d=d+1
        i=i+1
    elif word[i]=='E':
        e=e+1
        i=i+1
    elif word[i]=='F':
        f=f+1
        i=i+1
    elif word[i]=='G':
        g=g+1
        i=i+1
    elif word[i]=='H':
        m=m+1
        i=i+1
    elif word[i]=='I':
        i1=i1+1
        i=i+1
    elif word[i]=='J':
        j=j+1
        i=i+1
    elif word[i]=='K':
        k=k+1
        i=i+1
    elif word[i]=='L':
        l=l+1
        i=i+1
    elif word[i]=='M':
        m=m+1
        i=i+1
    elif word[i]=='N':
        n=n+1
        i=i+1
    elif word[i]=='O':
        o=o+1
        i=i+1
    elif word[i]=='P':
        p=p+1
        i=i+1
    elif word[i]=='Q':
        q=q+1
        i=i+1
    elif word[i]=='R':
        r=r+1
        i=i+1
     