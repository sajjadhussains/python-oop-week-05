def check_anagram(str1,str2):
    if len(str1)!=len(str2):
        return False
    else:
        length=len(str1)
        for i in range(length):
            if str1[i] not in str2:
                return False
        return True
    
def find_anagrams(list_0f_words):
    words=list_0f_words
    list_of_anagrams=[]
    same_anagram=[]
    already_in_anagram_index=[0 for _ in range(len(words))]
    for i in range(len(words)):
        if already_in_anagram_index[i]!=1:
                same_anagram.append(words[i])
                already_in_anagram_index[i]=1
        else:
            continue
        for j in range(1,len(words)):
            if already_in_anagram_index[j]==1:
                continue
            elif check_anagram(words[i],words[j])==True:
                same_anagram.append(words[j])
                already_in_anagram_index[j]=1 
        list_of_anagrams.append(same_anagram)
        same_anagram=[]
    return list_of_anagrams
        

result=find_anagrams(['eat', 'ate', 'done', 'tea', 'soup', 'node'])
print(result)

