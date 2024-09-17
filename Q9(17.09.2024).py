def all_elements_equal(lst):
    return all(x == lst[0] for x in lst)
def comman(word_list):
    a = ""
    while(True):
        comman_word = []
        for i in word_list:
            if len(i) <= len(a):
                return a
            word = i[0:len(a)+1]
            comman_word.append(word)
        if all_elements_equal(comman_word):
            a = comman_word[0]
        else:
            break
    return a
word_list = input("Input:").strip().split(",")
prefix  = comman(word_list)
print("Output: ",prefix)