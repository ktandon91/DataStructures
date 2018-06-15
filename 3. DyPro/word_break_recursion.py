
def dictionary_check(word):
    dictionary_ = ["i","mobile","samsung","sam","sung",
                            "man","mango","icecream","and",
                             "go","i","like","ice","cream"]

    for each_word in dictionary_:
        if each_word == word:
            return True

    return False


def recursive_sol(input_string):
    #Base case
    if len(input_string) == 0:
        return True

    for i in range(1,len(input_string)+1):
        if dictionary_check(input_string[:i]) and recursive_sol(input_string[i:]):
            return True

    return False


#print(recursive_sol("hiilikesamsung"))
print(recursive_sol(""))