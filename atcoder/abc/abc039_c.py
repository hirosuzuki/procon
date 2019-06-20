S = input()

ktbl = "WBWBWWBWBWBW" * 3
ttbl = (
    "Do", "Do#", "Re", "Re#", "Mi", "Fa", "Fa#", "So", "So#", "La", "La#", "Si"
)

i = ktbl.index(S)

result = ttbl[i]

print(result)
