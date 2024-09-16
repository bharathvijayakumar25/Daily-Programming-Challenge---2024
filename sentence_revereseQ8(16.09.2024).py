sentence = input("Sentence :").strip()
sentence = [x for x in sentence.split(" ")]
sentence = [s for s in sentence if s] 
print(sentence)
for i in range(len(sentence)-1,-1,-1):
    print(sentence[i],end=" ")
