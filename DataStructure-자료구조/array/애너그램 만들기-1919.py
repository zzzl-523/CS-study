# 순서를 바꿔서 같아지려면 같은 알파벳을 가지기만 하면 된다
import sys
wordA, wordB = [input() for _ in range(2)]

cnt = 0
total = 0

# 검사할 때 중복은 제거해야 한다
tmp_a = wordA
tmp_b = wordB

for alpha in wordA:
    if alpha in tmp_b:
        cnt += 1
        tmp_b = tmp_b.replace(alpha, '', 1)
totalA = len(wordA) - cnt

cnt = 0
for alpha in wordB:
    if alpha in tmp_a:
        cnt += 1
        tmp_a = tmp_a.replace(alpha, '', 1)
totalB = len(wordB) - cnt

print(totalA + totalB)