from random import randint
def y():
    a=randint(1,100)
    if a<=25:
        x=2
    elif a<=64:
        x=-2
    else:
        x=4
    return x #retourne une valeur qui suit la loi de proba du complement de cours n°1 du chapitre 11
def var():
    s=0
    for i in range(50):
        s=s+y()
    return s # retourne l'addition de 50 valeur de y()
def liste():
    l=[]
    for i in range(10000):
        l.append(var())
    return l # retourne une liste contenant 10k termes de var()a chaque terme
l=liste()
p=0
for i in range (len(l)) :
    if l[i]==10:
        p=p+1
print(p)# écrit le nombre de fois ou l'on rencontre le nombnre 10 dans la liste de 10k terme