strs = ["flower","flow","flight"]
result = ''

for i in range(len(strs[0])):
    c = strs[0][i]
    for word in strs:
        if i >= len(word) or word[i] != c:
            print(result)
            exit()
    
    result += c
    b = '"' + result + '"'
print(b)