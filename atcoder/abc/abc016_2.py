A, B, C = [int(_) for _ in input().split()]

if A + B == A - B == C:
    print('?')
elif A + B == C:
    print('+')
elif A - B == C:
    print('-')
else:
    print('!')