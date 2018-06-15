
def recursive_sol(str1, str2, len1, len2):
    if len1 ==0 or len2 == 0:
        return 0
    if str1[len1-1] == str2[len2-1]:
        return 1 + recursive_sol(str1[0:len1-1], str2[0:len2-1], len1-1,len2-1)

    else:
        return max(recursive_sol(str1[0:len1-1], str2[0:len2], len1-1,len2),recursive_sol(str1[0:len1], str2[0:len2-1], len1,len2-1))








str1 = "AGGTAB"
len1 = len(str1)
str2 = "GXTXAYB"
len2 = len(str2)

print(recursive_sol(str1,str2,len1,len2))