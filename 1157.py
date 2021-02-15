words= input().upper()
alphabet = list(set(words))

cnt_li = []
for i in alphabet:
    cnt = words.count(i)
    cnt_li.append(cnt)

if cnt_li.count(max(cnt_li)) > 1:
    print('?')
else:
    result = alphabet[cnt_li.index(max(cnt_li))]
    print(result)
