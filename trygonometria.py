def sin(x):
    if x==90:
        return 1
    elif x==60:
        return (3 ** (0.5))/2
    elif x==45:
        return (2 ** (0.5))/2
    elif x==30:
        return 0.5
    elif x==0:
        return 0
    else: 
        return False

def cos(x):
    if x==90:
        return 0
    elif x==60:
        return 0.5
    elif x==45:
        return (2 ** (0.5))/2
    elif x==30:
        return (3 ** (0.5))/2
    elif x==0:
        return 1
    else:
        return False

print(sin(45))
print(cos(45))
