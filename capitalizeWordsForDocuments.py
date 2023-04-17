x = open("text.txt", "r")

#list of string elements
s = str(x.read()).split()

#for each word in a
cat = ""
for word in s:
    cat = cat + word.capitalize() + " "

print(cat)
