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
        h=h+1
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
    elif word[i]=='S':
        s=s+1
        i=i+1
    elif word[i]=='T':
        t=t+1
        i=i+1
    elif word[i]=='U':
        u=u+1
        i=i+1
    elif word[i]=='W':
        w=w+1
        i=i+1
    elif word[i]=='X':
        x=x+1
        i=i+1
    elif word[i]=='Y':
        y=y+1
        i=i+1
    elif word[i]=='Z':
        z=z+1
        i=i+1
    else:
        print("Input Invalid")
        exit
    if a>0:
        print("The character a has come: ",a,"times.")
    if b>0:
        print("The character b has come: ",b,"times.")
    if c>0:
        print("The character c has come: ",c,"times.")
    if d>0:
        print("The character d has come: ",d,"times.")
    if e>0:
        print("The character e has come: ",e,"times.")
    if f>0:
        print("The charater f has come: ",f,"times.")
    if g>0:
        print("The character g has come: ",g,"times.")
    if h>0:
        print("The character h has come: ",h,"times.")
    if i>0:
        print("The character i has come: ",i,"times.")
    if j>0:
        print("The character j has come: ",j,"times.")
    if k>0:
        print("The character k has come: ",k,"times.")
    if l>0:
        print("The character l has come: ",l,"times.")
    if m>0:
        print("The character m has come: ",m,"times.")
    if n>0:
        print("The character n has come: ",n,"times.")
    if o>0:
        print("The character o has come: ",o,"times.")
    if p>0:
        print("The character p has come: ",p,"times.")
    if q>0:
        print("The character q has come: ",q,"times.")
    if r>0:
        print("The character r has come: ",r,"times.")
    if s>0:
        print("The character s has come: ",s,"times.")
    if t>0:
        print("The character t has come: ",t,"times.")
    if u>0:
        print("The character u has come: ",u,"times.")
    if v>0:
        print("The character v has come: ",v,"times.")
    if w>0:
        print("The character w has come: ",w,"times.")
    if x>0:
        print("The character x has come: ",x,"times.")
    if y>0:
        print("The character y has come: ",y,"times.")
    if z>0:
        print("The character z has come: ",z,"times.")
print("Question 3: String encoding: Perform basic string compression using the counts of repeated characters.")
word=input("Enter a word to perform basic string compression using the counts of repeated characters")
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
i=0
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
    if word[i]=='B':
        b=b+1
        i=i+1
    if word[i]=='C':
        c=c+1
        i=i+1
    if word[i]=='D':
        d=d+1
        i=i+1
    if word[i]=='E':
        e=e+1
        i=i+1
    if word[i]=='F':
        f=f+1
        i=i+1
    if word[i]=='G':
        g=g+1
        i=i+1
    if word[i]=='H':
        h=h+1
        i=i+1
    if word[i]=='I':
        i1=i1+1
        i=i+1
    if word[i]=='J':
        j=j+1
        i=i+1
    if word[i]=='K':
        k=k+1
        i=i+1
    if word[i]=='L':
        l=l+1
        i=i+1
    if word[i]=='M':
        m=m+1
        i=i+1
    if word[i]=='N':
        n=n+1
        i=i+1
    if word[i]=='O':
        o=o+1
        i=i+1
    if word[i]=='P':
        p=p+1
        i=i+1
    if word[i]=='Q':
        q=q+1
        i=i+1
    if word[i]=='R':
        r=r+1
        i=i+1
    if word[i]=='S':
        s=s+1
        i=i+1
    if word[i]=='T':
        t=t+1
        i=i+1
    if word[i]=='U':
        u=u+1
        i=i+1
    if word[i]=='V':
        v=v+1
        i=i+1
    if word[i]=='W':
        w=w+1
        i=i+1
    if word[i]=='X':
        x=x+1
        i=i+1
    if word[i]=='Z':
        z=z+1
        i=i+1
    print("a",a,"b",b,"c",c,"d",d,"f",f,"g",g,"h",h,"i",i,"j",j,"k",k,"l",l,"m",m,"n",n,"o",o,"p",p,"q",q,"r",r,"s",s,"t",t,"u",u,"v",v,"w",w,"x",x,"y",y,"z",z)
print("Question 4: Word Reverser: Reverse the order of the words while keeping the characters within the words in the correct order.")
sentence=input("Enter the sentence that needs to reverse the order of the words while keeping the characters within the words in the correct order.")
words=sentence.split()
reversed_words=words[::-1]
result=''.join(reversed_words)
print(result)
print("Question 5: Validating an anagram: Determines if they are anagrams of each other or not")
word1=input("Enter First word: ")
word2=input("Enter Second word: ")    
n1=len(word1)
n2=len(word2)
if n1!=n2:
    print("The given pair of words are not anagram")
    exit
i=0,j=0
while i<n:
    count=0
    while j<n:
        if word1[i].upper()==word[j].upper():
            count=count+1
        j=j+1
    if count==0:
        print("The given pair of words are not anagram")
        exit
    i=i+1
if count>0:
    print("The given pair of words are anagram")
        
            
               
        