#Lab11
#Author: Vincenza Paradiso and Saerin Bong

name = {"Anspach":"Grace",
"Berlage":"Bethany",
"Bong":"Saerin",
"Busk":"Olivia",
"Eafon":"Breanna",
"Faye Gallaway":"Gabrielle",
"Hoffman":"Rosemary",
"Nixon":"Emily",
"O'Roark":"Katherine",
"Paradiso":"Vincenza",
"Stephenson":"Sarah",
"Dockery":"Krista"}


freq_dict = {}
for first_name in name.values():
    if first_name in freq_dict:
        freq_dict[first_name] += 1
    else:
        freq_dict[first_name] = 1

print(freq_dict)
