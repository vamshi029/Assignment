def MaxReducedString(s):
    
    stack = []
    length=len(s)-1
    index=0
    stack.append(s[index])
    index+=1
    while(index <= length):
        peek = stack[-1]
        if peek == s[index]:
            stack.pop()
        else:
            stack.append(s[index])
        index+=1
    return ''.join(stack)

s = 'abccba'
print(MaxReducedString(s))
