from Stack import Stack
def delimiter(x):
    s=Stack()
    for token in x:
        if token in "{([":
            s.push(token)
        elif token in "}])":
            if s.isEmpty():
                return False
            else:
                left=s.pop()
                if (token=="}" and left!="{") or\
                (token=="]" and left!="[") or\
                (token==")" and left!="("):
                    return False
    return s.isEmpty()

print(delimiter("{{[]}}"))
                

    
