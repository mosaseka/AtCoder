N = int(input())
S = str(input())
COUNT = 0

for i in range(N-2):
  if S[i] == "#" and S[i+2] == "#":
    COUNT += 1

print(COUNT)