def pal(string,l,h):
    if l==h:
        return True
    if string[l]!=string[h]:
        return False
    return pal(string,l+1,h-1)
