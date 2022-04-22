def towersofhanoi(n, src, temp, dest):
    if n >= 1:
        towersofhanoi(n-1, src, temp, dest)
        print("move ", src, "to ", dest)
        towersofhanoi(n-1, temp, dest, src),
