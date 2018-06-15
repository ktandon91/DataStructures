def dictionaryContains(word):
    words = ["mobile","samsung","sam","sung",
                            "man","mango","icecream","and",
                             "go","i","like","ice","cream"]

    for i in range(0,len(words)):
        if words[i] == word:
            return True
    return False

def wordBreak(input_string):
    size = len(input_string)

    #Base Case
    if size==0:
        return True

    for i in range(1, size+1):
        if dictionaryContains(input_string[0:i]) and wordBreak(input_string[i:size]):
            return True
    return False


if  wordBreak("ilikemango"):
    print("Yes")
else :
    print("No")
