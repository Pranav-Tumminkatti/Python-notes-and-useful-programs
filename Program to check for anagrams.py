#An anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.
def anagrams(s1,s2):
    anagram = False
    if (s1 == s2) or (s1 in s2) or (s2 in s1) or (len(s1) != len(s2)):
        anagram = False
    else:
        lst_1 = []
        for i in s1.lower():
            lst_1.append(i)

        dict_1 = {}
        for x in lst_1:
            if x not in dict_1:
                dict_1[x] = 1
            else:
                dict_1[x] = dict_1[x] + 1
        lst_2 = []
        for i in s2.lower():
            lst_2.append(i)

        dict_2 = {}
        for x in lst_2:
            if x not in dict_2:
                dict_2[x] = 1
            else:
                dict_2[x] = dict_2[x] + 1
                
        if dict_1 == dict_2:
            anagram = True
        else:
            anagram = False

    return anagram
    




