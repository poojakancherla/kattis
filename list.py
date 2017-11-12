lic=input().split()
word1=""
for x in lic:
    if x==" ":
        pass
    else:
        word1+=x
word=''.join(x for x in word1 if x.isalpha())
print(word)
file = open('words.txt', 'r')
if w
for line in file.readlines():
