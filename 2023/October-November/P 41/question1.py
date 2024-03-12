# 1a
def IterativeVowels(Value):
    Total = 0
    LengthString = len(Value)
    FirstCharacter = ''

    for x in range(0, LengthString):
        FirstCharacter = Value[:1]
        if FirstCharacter == 'a' or FirstCharacter == 'e' or FirstCharacter == 'i' or FirstCharacter == 'o' or FirstCharacter == 'u': Total += 1

        Value = Value[1:]
    
    return Total

# 1b
def RecursiveVowels(Value):
    LengthString = len(Value)
    FirstCharacter = ''

    if len(Value) == 0:
        return 0
    else:
        FirstCharacter = Value[:1]
        if FirstCharacter == 'a' or FirstCharacter == 'e' or FirstCharacter == 'i' or FirstCharacter == 'o' or FirstCharacter == 'u': return RecursiveVowels(Value[1:]) + 1
        else:
            return RecursiveVowels(Value[1:])


# Main Program
print(IterativeVowels("house"))
print(RecursiveVowels("imagine"))