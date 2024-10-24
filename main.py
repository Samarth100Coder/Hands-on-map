l1=[2,4,6,89,9]
l2=[23,98,90,21,4]
a=map(lambda x,y:x+y,l1,l2)
print(list(a))
def sq(n):
    return n*n
b=map(sq,l1)
print(list(b))