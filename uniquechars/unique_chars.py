# Create a function called `unique_characters` that takes a string as parameter
# and returns a list with the unique letters of the given string
# Create basic unit tests for it with at least 3 different test cases
# Should print out:
# ["n", "g", "r", "m"]


def unique_characters(string):
    unique = []
    for char in string:
        if char in unique:
            pass
        else:
            unique.append(char)
    return unique


print(unique_characters("anagram"))
