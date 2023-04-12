# Lab11
# Author: Vincenza Paradiso and Saerin Bong

name = ["Anspach", "Grace",
"Berlage","Bethany",
"Bong","Saerin",
"Busk","Olivia",
"Eafon","Breanna",
"Faye Gallaway","Gabrielle",
"Hoffman","Rosemary",
"Nixon","Emily",
"O'Roark","Katherine",
"Paradiso","Vincenza",
"Stephenson","Sarah",
"Dockery","Krista"]

def histogram(word):
    d = dict()
    for char in word:
        # val = d[char]
        if char[0] not in d:
            d[char[0]] = [char]
        else:
            d[char[0]].append(char)
    return d

a= histogram(name)
print (a)

# lastname=[::2]
# b=histogram(lastname)
# print(b)
