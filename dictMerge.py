
def dictMerge(dict1, dict2):
    dictComplete = {}
    for key,value in dict1.items():
        if key in dict2.keys():
            dictComplete[key] = [dict1[key], dict2[key]]
            dict2.pop(key)
        else:
            dictComplete[key] = value

    for key, value in dict2.items():
        dictComplete[key] = value
    return dictComplete


print(dictMerge({"a":1, "b":2, "c":3}, {"a":1, "e":2, "i":3}))
