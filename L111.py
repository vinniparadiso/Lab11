#Lab11
#Author: Vincenza Paradiso and Saerin Bong

def my_get_method(h, key, value):
    if key in h:
        return h[key]
    else:
        return value


h = {"dog":2, "cat":1, "goat":1, "cow":3}
print(my_get_method(h, "dog", 4))


h = {"dog":2, "cat":1, "goat":1, "cow":3}
a=  h.get("dog", 4)
print("a is this guy: ", a)
