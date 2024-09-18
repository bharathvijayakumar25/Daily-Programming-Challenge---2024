def anagram(strings):
    fin_gram = []
    words = [] 
    for i in range(len(strings)):
        if strings[i] not in words:  
            anagram_group = []
            for j in range(len(strings)):
                if sorted(strings[i]) == sorted(strings[j]):  
                    if strings[j] not in anagram_group: 
                        anagram_group.append(strings[j])
                        words.append(strings[j])
            if anagram_group not in fin_gram: 
                fin_gram.append(anagram_group)
    return fin_gram
strings = [list(x) for x in input("Input: ").split(",")]
fin_gram = anagram(strings)
result = []
for sublist in fin_gram:
    temp_list = []
    for letter_list in sublist:
        word = ''.join(letter_list)
        temp_list.append(word)
    result.append(temp_list)
print("Output:",result)