def reverseStr(string):
    string = str(string)
    characters = list(string)
    characters.reverse()
    reversedString = ""
    for i in characters:
        reversedString += i
    return reversedString

