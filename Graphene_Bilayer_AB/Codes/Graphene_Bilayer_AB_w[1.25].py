#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#%matplotlib

import numpy as np
import math
import random
#from mpl_toolkits import mplot3d
#import matplotlib.pyplot as plt
import scipy.linalg as la
from scipy.sparse import dia_matrix
from scipy.sparse.linalg import eigsh
from decimal import Decimal
#from mpmath import *


#seeds = np.loadtxt('/home/lucifer/IISER/Summer_2021/Seeds.txt')
seeds = np.loadtxt('/home/dintomonjoy/AA_AB/Graphene_Bilayer_AB/Seeds.txt')


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
    #ax.scatter3D(0, 0, 0, c = "black")
    #ax.view_init(90,-90)
    #plt.show()
    #print(cc)


    #Layer 2
    j=0
    z1=2
    while j<n1:
        constant = 2*a*j - 2*h
        i=0
        if j%2 == 0:
            x=l
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
            x=l
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
    xt1 = 0
    xt2 = 0
    #xt3 = 0
    #xt4 = 0
    
    seeding = seeds[counter]
    random.seed(seeding)
    #print(seeding)
    
    w = 1.25
    
    a1 = (1-w)
    b1 = (1+w)
    
    a2 = a1/10
    b2 = b1/10
    
    #a3 = a1/10
    #b3 = b1/10
    
    #a4 = a1/60
    #b4 = b1/60
   # __________________
    
    i = 0
    tim1=[]

    while i<21300:
        tim1.append(random.uniform(a1,b1))
        i=i+1
    
   # __________________
        
    i = 0
    tim2=[]

    while i<3600:
        tim2.append(random.uniform(a2,b2))
        i=i+1
        
   # __________________
        
    #i = 0
    #tim3=[]

    #while i<5251:
        #tim3.append(random.uniform(a3,b3))
        #i=i+1
        
   # __________________
        
    #i = 0
    #tim4=[]

    #while i<10501:
        #tim4.append(random.uniform(a4,b4))
        #i=i+1
        
   # __________________
    
    #intralayer t
    def hop1():
        global xt1
        numbers= list()
        #numbers.append(-1)
        #numbers.append(random.uniform(a1,b1))
        #numbers.append(random.uniform(0,1))
        #return numbers[random.randint(0,1)]
        #xt1 = xt1 + 1
        #return numbers[0]
        rt = tim1[xt1]
        xt1 = xt1 + 1
        return rt

    #intralayer t_o
    def hop2():
        global xt2
        numbers= list()
        #numbers.append(0.1)
        #numbers.append(random.uniform(a2,b2))
        #numbers.append(random.uniform(0,0.1))
        #return numbers[random.randint(0,1)]
        #xt1 = xt1 + 1
        #return numbers[0]
        rt = tim2[xt2]
        xt2 = xt2 + 1
        return rt

    #intralayer t3 non-dimer to non-dimer
    def hop3():
        #global xt3
        numbers= list()
        numbers.append(0)
        #numbers.append(random.uniform(a3,b3))
        #numbers.append(random.uniform(0,0.1))
        #return numbers[random.randint(0,1)]
        #xt1 = xt1 + 1
        return numbers[0]
        #rt = tim3[xt3]
        #xt3 = xt3 + 1
        #return rt

    #intralayer t4 nondimer to dimer
    def hop4():
        #global xt4
        numbers= list()
        numbers.append(0) #1/60th
        #numbers.append(random.uniform(a4,b4))
        #numbers.append(random.uniform(0.001667,0.01667))
        #return numbers[random.randint(0,1)]
        #xt1 = xt1 + 1
        return numbers[0]
        #rt = tim4[xt4]
        #xt4 = xt4 + 1
        #return rt


    #periodicity
    z=0
    tot = n1*n
    while z<n:
        t1=hop1()
        t2=hop2()
        i = z + (n1-1)*n
        #print(z,"---",i)
        if ((z%2)!=0):
            #print(i,"---",(z))
            H[i,(z)] = t1
            H[z,i] = t1
            H[(i+tot),(z+tot)] = t1
            H[(z+tot),(i+tot)] = t1
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


            #Non-dimer to dimer t4
            tupp = (x,y,(z+2))
            if tupp in cc:
                tup1a = (x,(y+a),(z+2))
                tup2a = ((x+l),(y-2*h),(z+2))
                tup3a = ((x-l),(y-2*h),(z+2))
                #print(tup1a,tup2a,tup3a)

                if tup1a in cc:
                    index = cc.index(tup1a)
                    #t=-1
                    #t = random.uniform(-1, math.exp(delta))
                    t = hop4()
                    #print(t)
                    H[i,index] = t
                    H[index,i] = t
                    #print(cc.index(tup1a))
                    #print(i)
                    #print(tup1a)

                if tup2a in cc:
                    index = cc.index(tup2a)
                    #t=-1
                    #t = random.uniform(-1, math.exp(delta))
                    t = hop4()
                    #print(t)
                    H[i,index] = t
                    H[index,i] = t
                    #print(cc.index(tup2a))
                    #print(i)
                    #print(tup2a)

                if tup3a in cc:
                    index = cc.index(tup3a)
                    #t=-1
                    #t = random.uniform(-1, math.exp(delta))
                    t = hop4()
                    #print(t)
                    H[i,index] = t
                    H[index,i] = t
                    #print(cc.index(tup3a))
                    #print(i)
                    #print(tup3a)

            #Non-dimer to non-dimer t3
            if z == 2:
                tup1b = (x,(y+a+2*h),(z-2))
                tup2b = ((x+l),(y+a-2*h),(z-2))
                tup3b = ((x-l),(y+a-2*h),(z-2))
                #print(tup1b,tup2b,tup3b)
                if tup1b in cc:
                    index = cc.index(tup1b)
                    #t=-1
                    #t = random.uniform(-1, math.exp(delta))
                    t = hop3()
                    #print(t)
                    H[i,index] = t
                    H[index,i] = t
                    #print(cc.index(tup1b))
                    #print(i)
                    #print(tup1b)

                if tup2b in cc:
                    index = cc.index(tup2b)
                    #t=-1
                    #t = random.uniform(-1, math.exp(delta))
                    t = hop3()
                    #print(t)
                    H[i,index] = t
                    H[index,i] = t
                    #print(cc.index(tup2b))
                    #print(i)
                    #print(tup2b)

                if tup3b in cc:
                    index = cc.index(tup3b)
                    #t=-1
                    #t = random.uniform(-1, math.exp(delta))
                    t = hop3()
                    #print(t)
                    H[i,index] = t
                    H[index,i] = t
                    #print(cc.index(tup3b))
                    #print(i)
                    #print(tup3b)



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

            #Non-dimer to dimer t4
            tupp = (x,y,(0))
            if tupp in cc:
                tup1a = (x,(y-a),0)
                tup2a = ((x+l),(y+2*h),0)
                tup3a = ((x-l),(y+2*h),0)
                #print(tup1a,tup2a,tup3a)

                if tup1a in cc:
                    index = cc.index(tup1a)
                    #t=-1
                    #t = random.uniform(-1, math.exp(delta))
                    t = hop4()
                    #print(t)
                    H[i,index] = t
                    H[index,i] = t
                    #print(cc.index(tup1a))
                    #print(i)
                    #print(tup1a)

                if tup2a in cc:
                    index = cc.index(tup2a)
                    #t=-1
                    #t = random.uniform(-1, math.exp(delta))
                    t = hop4()
                    #print(t)
                    H[i,index] = t
                    H[index,i] = t
                    #print(cc.index(tup2a))
                    #print(i)
                    #print(tup2a)

                if tup3a in cc:
                    index = cc.index(tup3a)
                    #t=-1
                    #t = random.uniform(-1, math.exp(delta))
                    t = hop4()
                    #print(t)
                    H[i,index] = t
                    H[index,i] = t
                    #print(cc.index(tup3a))
                    #print(i)
                    #print(tup3a)

        i=i+1

    #print(H)
    #print(cc)
    #Eigenvalues
    #mp.dps = 18

    #A = mp.matrix(H)

    #w,v= mp.eig(A)
    #print(w)
    W,V = la.eig(H)
    W.sort()
    #print(w)
    i=0
    x=[0]*len(W)
    #print(W)
    while i<len(W):
        tempo=Decimal(W[i].real)
        #print(d)
        x[i]=tempo
        i=i+1
    np.savetxt('/home/dintomonjoy/AA_AB/Graphene_Bilayer_AB/Energy_Eigenvalues_w[1.25]/Energy_Eigenvalues'+str(counter)+'.txt',W.real,fmt='%.54e')
    #print(xt1)
    #print(xt2)
    #print(xt3)
    #print(xt4)
    #print(W)
    counter = counter + 1




