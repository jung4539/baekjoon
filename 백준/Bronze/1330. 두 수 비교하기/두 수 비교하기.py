A, B = map(int, input().split())
result = 0
if A > B:
    result = ">"
elif A < B:
    result = "<"
elif A == B:
    result = "=="
print(result)