def solve22():
    alphabet=['"',"A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    S=0
    f = open('p022_names.txt', 'r')
    txt=f.read()
    txt=txt.split(",")
    txt=sorted(txt)
    for i in range(len(txt)):
        nom=txt[i]
        s=0
        for lettre in nom:
            for j in range(len(alphabet)):
                if lettre==alphabet[j]:
                    s+=j
                    break
        S+=(i+1)*s
    return(S)

print(solve22())