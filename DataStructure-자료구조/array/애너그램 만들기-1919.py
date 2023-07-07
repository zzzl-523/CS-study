# 순서를 바꿔서 같아지려면 같은 알파벳을 가지기만 하면 된다
import sys
wordA, wordB = [input() for _ in range(2)]

cnt = 0
total = 0
wordA_len = len(wordA)
wordB_len = len(wordB)

# 검사할 때 중복은 제거해야 한다
for alpha in wordA:
    if alpha in wordB:
        cnt += 1
        wordB = wordB.replace(alpha, '')
total = wordA_len - cnt

cnt = 0
for alpha in wordB:
    if alpha in wordA:
        cnt += 1
        wordA = wordA.replace(alpha, '')
total += wordB_len - cnt

print(total)