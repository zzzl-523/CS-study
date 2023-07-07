N = input()
nums = input().split(' ')
v = input()

cnt = 0

for num in nums:
    if num == v:
        cnt += 1

print(cnt)