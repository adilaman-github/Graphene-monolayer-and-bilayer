#%matplotlib

import numpy as np
import math
import random
#from mpl_toolkits import mplot3d
#import matplotlib.pyplot as plt
import scipy.linalg as la
from scipy.sparse import dia_matrix
from scipy.sparse.linalg import eigsh
#from mpmath import *


#seeds = np.loadtxt('/home/lucifer/IISER/Summer_2021/Seeds.txt')
seeds = np.loadtxt('/home/dintomonjoy/AA_AB/Graphene_Bilayer_AA/Seeds.txt')

counter = 0
sample_number = 100

while counter < sample_number:
    
    a = 2 #length of the hexagon
    n = 60 #number of linear sites
    n1 = 60 #number of layers

    #z = math.pi/3

    #h = round(math.cos(z)*a,5)
    #l = round(math.sin(z)*a,5)

    h=1
    l=2

    x=0 #x axis counter
    cc =[] #particle position

    color_index=[]

    #Graphing

    #fig = plt.figure(figsize = (10, 10))
    #ax = plt.axes(projection ="3d")
    #ax.set_xlabel('X-axis')
    #ax.set_ylabel('Y-axis')
    #ax.set_zlabel('Z-axis')

    #plt.grid(True, linewidth = "0.5")

    #Layer 1
    j=0
    z1=0
    while j<n1:
        constant = 2*a*j
        i=0
        if j%2 == 0:
            x=0
            while i<n:
                if i%2 == 0:
                    p = 1
                    color = 'b'
                else:
                    p = -1
                    color = 'r'
                #print(p)
                y = constant + p*h #y axis
                #ax.scatter3D(x, y, z1, c=color)
                cc.append((x,y,z1))
                color_index.append(color)
                x = x + l
                i=i+1
        else:
            x=0
            while i<n:
                if i%2 == 0:
                    p = -1
                    color = 'r'
                else:
                    p = 1
                    color = 'b'
                #print(p)
                y = constant + p*h #y axis
                #ax.scatter3D(x, y, z1, c = color)
                #print(x,y)
                cc.append((x,y,z1))
                color_index.append(color)
                x = x + l
                i=i+1       
        j=j+1
    #plt.show()
    #print(cc)


    #Layer 2
    j=0
    z1=2
    while j<n1:
        constant = 2*a*j
        i=0
        if j%2 == 0:
            x=0
            while i<n:
                if i%2 == 0:
                    p = 1
                    color = 'b'
                else:
                    p = -1
                    color = 'r'
                #print(p)
                y = constant + p*h #y axis
                #ax.scatter3D(x, y, z1, c=color)
                cc.append((x,y,z1))
                color_index.append(color)
                x = x + l
                i=i+1
        else:
            x=0
            while i<n:
                if i%2 == 0:
                    p = -1
                    color = 'r'
                else:
                    p = 1
                    color = 'b'
                #print(p)
                y = constant + p*h #y axis
                #ax.scatter3D(x, y, z1, c = color)
                #print(x,y)
                cc.append((x,y,z1))
                color_index.append(color)
                x = x + l
                i=i+1       
        j=j+1

    #ax.scatter3D(0, 0, 0, c = "black")
    #ax.view_init(90,-90)
    #plt.show()
    #print(cc)

    length=len(cc)
    #Initialization of Hamiltonian
    Hrow = length
    Hcol = length
    H = np.zeros([Hrow, Hcol]) #Initialize the H matrix
    #print(H)
    #print(length)



    #Random number
    xt1=0
    xt2=0

    seeding = seeds[counter]
    random.seed(seeding)
    #print(seeding)
    
    w = 0.75

    a1 = (1-w)
    b1 = (1+w)

    a2 = a1/10
    b2 = b1/10

    # __________________
    
    i = 0
    tim1=[]

    while i<21360:
        tim1.append(random.uniform(a1,b1))
        i=i+1
    
   # __________________
        
    i = 0
    tim2=[]

    while i<7200:
        tim2.append(random.uniform(a2,b2))
        i=i+1
        
   # __________________

    

    #Nearest neighbour t
    def hop1():
        global xt1
        numbers = list()
        #numbers.append(-1)
        #numbers.append(random.uniform(0.1,1.9))
        #numbers.append(random.uniform(0.1,1))
        #return numbers[random.randint(0,1)]
        #tim2.append(numbers[0])
        #return numbers[0]
        rt = tim1[xt1]
        xt1 = xt1 + 1
        return rt

    #Next nearest neighbour t
    def hop2():
        #global xt2
        #numbers = list()
        #power = -1
        #numbers.append(0)
        #numbers.append(10**power)
        #numbers.append(random.uniform(0.1,1.9))
        #numbers.append(random.uniform(0.1,1))
        #return numbers[random.randint(0,1)]
        #tim2.append(numbers[0])
        #return numbers[0]
        rt = tim2[xt2]
        xt2 = xt2 + 1
        return rt


    #periodicity
    z=0
    tot = n1*n
    while z<n:
        t1=hop1()
        t2=hop1()
        i = z + (n1-1)*n
        #print(z,"---",i)
        if ((z%2)!=0):
            #print(i,"---",(z))
            H[i,(z)] = t1
            H[z,i] = t1
            H[(i+tot),(z+tot)] = t2
            H[(z+tot),(i+tot)] = t2
        z=z+1
    #print(H)


    i=0
    while i<length:

        if color_index[i] == 'r':
            x,y,z = cc[i]
            tup1 = (x,(y-a),z)
            tup2 = ((x+l),(y+2*h),z)
            tup3 = ((x-l),(y+2*h),z)
            tup4 = (x,y,(z+2))
            tup5 = (x,y,(z-2))

            if tup1 in cc:
                index = cc.index(tup1)
                #t=-1
                #t = random.uniform(-1, math.exp(delta))
                t = hop1()
                #print(t)
                H[i,index] = t
                H[index,i] = t
                #print(cc.index(tup1))
                #print(i)
                #print(tup1)
                #print("***")
            if tup2 in cc:
                index = cc.index(tup2)
                #t=-1
                #t = random.uniform(-1, math.exp(delta))
                t = hop1()
                #print(t)
                H[i,index] = t
                H[index,i] = t
                #print(cc.index(tup1))
                #print(i)
                #print(tup2)
                #print("***")
            if tup3 in cc:
                index = cc.index(tup3)
                #t=-1
                #t = random.uniform(-1, math.exp(delta))
                t = hop1()
                #print(t)
                H[i,index] = t
                H[index,i] = t
                #print(cc.index(tup1))
                #print(i)
                #print(tup3)
                #print("***")
            if tup4 in cc:
                index = cc.index(tup4)
                #t=-1
                #t = random.uniform(-1, math.exp(delta))
                t = hop2()
                #print(t)
                H[i,index] = t
                H[index,i] = t
                #print(cc.index(tup1))
                #print(i)
                #print(tup4)
                #print("***")
            if tup5 in cc:
                index = cc.index(tup5)
                #t=-1
                #t = random.uniform(-1, math.exp(delta))
                t = hop2()
                #print(t)
                H[i,index] = t
                H[index,i] = t
                #print(cc.index(tup1))
                #print(i)
                #print(tup5)
                #print("***")
            #print("\n")


        if color_index[i] == 'b':
            x,y,z = cc[i]
            tup1 = (x,(y+a),z)
            tup2 = ((x+l),(y-2*h),z)
            tup3 = ((x-l),(y-2*h),z)
            tup4 = (x,y,(z+2))
            tup5 = (x,y,(z-2))

            if tup1 in cc:
                index = cc.index(tup1)
                #t=-1
                #t = random.uniform(-1, math.exp(delta))
                t = hop1()
                #print(t)
                H[i,index] = t
                H[index,i] = t
                #print(cc.index(tup1))
                #print(i)
                #print(tup1)
                #print("***")
            if tup2 in cc:
                index = cc.index(tup2)
                #t=-1
                #t = random.uniform(-1, math.exp(delta))
                t = hop1()
                #print(t)
                H[i,index] = t
                H[index,i] = t
                #print(cc.index(tup1))
                #print(i)
                #print(tup2)
                #print("***")
            if tup3 in cc:
                index = cc.index(tup3)
                #t=-1
                #t = random.uniform(-1, math.exp(delta))
                t = hop1()
                #print(t)
                H[i,index] = t
                H[index,i] = t
                #print(cc.index(tup1))
                #print(i)
                #print(tup3)
                #print("***")
            if tup4 in cc:
                index = cc.index(tup4)
                #t=-1
                #t = random.uniform(-1, math.exp(delta))
                t = hop2()
                #print(t)
                H[i,index] = t
                H[index,i] = t
                #print(cc.index(tup1))
                #print(i)
                #print(tup4)
                #print("***")
            if tup5 in cc:
                index = cc.index(tup5)
                #t=-1
                #t = random.uniform(-1, math.exp(delta))
                t = hop2()
                #print(t)
                H[i,index] = t
                H[index,i] = t
                #print(cc.index(tup1))
                #print(i)
                #print(tup5)
                #print("***")
            #print("\n")


        i=i+1

    #print(H)


    #Eigenvalues
    #mp.dps = 18

    #A = mp.matrix(H)

    #w,v= mp.eig(A)
    #print(w)
    W,v = la.eig(H)
    W.sort()

    while i<len(W):
            tempo=Decimal(W[i].real)
            #print(d)
            x[i]=tempo
            i=i+1


    np.savetxt('/home/dintomonjoy/AA_AB/Graphene_Bilayer_AA/Energy_Eigenvalues_w[0.75]/Energy_Eigenvalues'+str(counter)+'.txt',W.real,fmt='%.54e')
    #np.savetxt('/home/lucifer/IISER/Summer_2021/Hamiltoninan_Bilayer_AA'+str(length)+'.txt',H, fmt='%.1e')
    
    
    counter = counter + 1

    
