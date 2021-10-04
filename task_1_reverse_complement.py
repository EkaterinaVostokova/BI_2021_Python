#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Defining the possible functions
def transcribe(x):
    result = x.replace("T", "U")
    result1 = result.replace("t", "u")
    return result1


def reverse(x):
    result1 = x[::-1]
    return result1


def complement(x):
    result = []
    # in this case if neither t or u is present, it is considered as a DNA sequence
    if ("t" in x or "T" in x) and ("u" not in x and "U" not in x):
        # here the first element is complementary to the last one, etc.
        al = ["A", "a", "C", "c", "g", "G", "t", "T"]
        for element in x:
            result.append(al[len(al) - 1 - al.index(element)])
        return ("".join(result))
    elif ("t" not in x and "T" not in x) and ("u" not in x and "U" not in x):
        al = ["A", "a", "C", "c", "g", "G", "t", "T"]
        for element in x:
            result.append(al[len(al) - 1 - al.index(element)])
        return ("".join(result))
    elif ("u" in x or "U" in x) and ("t" not in x and "T" not in x):
        al = ["A", "a", "C", "c", "g", "G", "u", "U"]
        for element in x:
            result.append(al[len(al) - 1 - al.index(element)])
        return ("".join(result))
    
    
def reverse_complement(x):
    result = complement(x)
    return result[::-1]


# the program itself starts
command = ""
while command != "exit":
    command = input("Enter command: ")
    if command == "exit":
        print("Good luck")
    else:
        x = input("Enter sequence: ")
        lib = {"A", "T", "G", "C", "U", "a", "t", "g", "c", "u"}   # All available letters
        # if both U and T are present, it is also considered invalid alphabet
        while not lib.issuperset(x) or (("u" in x or "U" in x) and ("t" in x or "T" in x)):
            print("Invalid Alphabet, try again!")
            x = input("Enter sequence:")
        if command == "reverse":
            print(reverse(x))
        elif command == "transcribe":
            print(transcribe(x))
        elif command == "complement":
            print(complement(x))
        elif command == "reverse complement":
            print(reverse_complement(x))
        else:
            print("Unknown command")
