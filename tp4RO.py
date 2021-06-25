from random import *

print("Le résultat d'un lancement de dé: ",randint(1,6))
n=int(input("Entrer le nombre de lancement de dé: "))
print("Le résultat de n lancement de dé est: ")
liste=[randint(1,6) for i in range(n)]
print(liste)

def nbapp6():
    print("Le nombre d'apparition de 6 est: ",liste.count(6))

nbapp6()

k=0
l=list()
while 1:
    x=randint(1,6)
    l.append(x)
    if x==6:
        break
    else:
        k=k+1
print("La nouvelle liste générée est: ",l)
print("Le nombre de lancers avant obtenir le premier 6 est: ",k)

def tirage():
    n=int(input("Entrer le nombre de tirage: "))
    for i in range(n):
        piece=randint(1,2)
        if piece==1:
            print("pile")
        if piece==2:
            print("face")

tirage()

#c liste remplie par 1 chaque fois qu'on a une vecteur de la matrice stochastique
c=[] 

def vectstoc():
    s=0
    v=[]
    n=int(input("Entrer la taille du vecteur v: "))
    print("Entrer les composants de v: ")
    for i in range(n):
        x=float(input())
        v.append(x)
    print("Le vecteur v est: ",v)
    for i in range(n):
        s=s+v[i]
    if s==1:
        print("Le vecteur v est stochastique")
        c.append(1)
    else:
        print("Le vecteur v n'est pas stochastique")
vectstoc()

def matstoc():
    n=int(input("Entrer le nombre des lignes du matrice: "))
    for j in range(n):
        vectstoc()
    if sum(c)-1==n:
        print("Alors la matrice est stochastique")
    else:
        print("Alors la matrice n'est pas stochastique")
        
matstoc()

def tpuissancem():
    T = [ [1, 0, 0], [0, 0, 1], [0.5, 0.25, 0.25] ]
    n=len(T)
    C = [[0]*n for i in range(n)]
    m=int(input("Entrer le nombre des lignes du matrice: "))
    for l in range(m):
        for i in range(n):
            for j in range(n):
                for k in range(n):
                    C[i][j] += T[i][k] * T[k][j]
    print("T : ", T)
    print("T^m : ", C)

tpuissancem()        


