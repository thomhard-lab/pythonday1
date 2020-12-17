#!/usr/bin/env python
# coding: utf-8

# In[4]:


import numpy as np

#Membuat Matriks 3x4
a=np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
#Menampilkan Matriks 3x4
print(a)


# In[14]:


#Membuat Matriks Baru
#np.array()
#np.zeros()
#np.ones()
#np.empty()
#np.arange()

b=np.zeros(5)
c=np.ones(2)
print(b,c)


# In[15]:


#Membuat Matriks Identitas
d=np.identity(3)
print(d)


# In[27]:


#Membuat 3-Matriks 2x4
#Multidimensional Matrix
e=np.array([[[0,1,2,3],
             [4,5,6,7]],
            [[0,1,2,3],
             [4,5,6,7]],
            [[0,1,2,3],
             [4,5,6,7]]])
print(e)


# In[28]:


#Banyaknya Matriks yang ada di dalam List (a)
e.ndim


# In[29]:


#Banyaknya Titik yang ada didalam matriks (n=a*b*c)
e.size


# In[30]:


#Bentuk matriks yang ada (a x b x c)
e.shape


# In[43]:


#Reshape Matriks 
a=np.arange(10)
#Matriks Linear 1x10
print('Matriks Linear 1x10 :\n')
print(a)

#Merubah Matriks a menjadi 5x2
b=a.reshape(5,2)
print('Matriks 2D 5x2 :\n')
print(b)

c=np.arange(60)
print('Matriks Linear 1x60 :\n')
print(c)

d=c.reshape(5,12)
print('Matriks 2D 5x12 :\n')
print(d)

e=c.reshape(5,2,6)
print('Matriks 3D 5x2x6 :\n')
print(e)

f=c.reshape(5,2,2,3)
print('Matriks 4D 5x2x2x3 :\n')
print(f)


# In[65]:


#PR
a=6
b=6
peta=np.arange(a,b)
for i in range (a):
    peta.vstack(np.zeros(a))
    
print(peta)
    


# In[56]:


#Indexing dan Slicing 
data=np.array([1,2,3,4,5,6])

#Mengambil Semua Data
print(data)
#Mngambil Data Index 0/Pertama
print(data[0])
#Mengambil Data Index 1
print(data[1])
#Mengambil Data dari Index 0/Pertama Sebanyak 4
print(data[0:4])
#Mengambil Data dari Index 1 sampai terakhir
print(data[1:])
#Mengambil Data dari akhir sebanyak 5
print(data[-5:])


# In[70]:


#Memfilter Array
#Quality Control (misalkan)
data=np.array([1,2,3,4,5,6])
two_up=(data >= 2)
print(data[two_up])
print(data[data>=4])

divisible_by_2=data[data%2==0]
print(divisible_by_2)


# In[71]:


#Memfilter Array
#Quality Control (misalkan)
data=np.array([1,2,3,4,5,6])
data=data*5
two_up=(data >= 2)
print(data[two_up])
print(data[data>=4])

divisible_by_2=data[data%2==0]
print(divisible_by_2)


# In[75]:


#Fungsi Agregasi (seperti fungsi excel)
data=np.array([1,2,3,4,5,6])
data=data*5
print(data)
print(data.sum())
print(data.max())


# In[79]:


#Fungsi Agregasi (seperti fungsi excel)
data=np.array([1,2,3,4,5,6])
data=data*5
print(data)
print(data.sum())
print(data.max())
print(np.random.random((3,2)))


# In[85]:


#Transposing da
#Reshape Matriks 
a=np.arange(10)
#Matriks Linear 1x10
print('Matriks Linear 1x10 :\n')
print(a)

#Merubah Matriks a menjadi 5x2
b=a.reshape(5,2)
print('Matriks 2D 5x2 :\n')
print(b)

print('Transpose Matriks 2x5 :\n')
print(b.T)
print('Flatten Matriks :\n')
print(b.flatten())
print('Ravel Matriks (Hemat Memory Komputer) :\n')
print(b.ravel())


# In[90]:


#Working with Math Formulas
#((1/n)(sigma(Y1-Y2)^2)
observed=np.array([1,2,3,4,5,6])
prediction=np.array([3,5,8,9,11,12])
n=6

error=(1/n) * np.sum(np.square(observed-prediction))
print(observed-prediction)
print(np.square(observed-prediction))
print(np.sum(np.square(observed-prediction)))
print(error)


# In[ ]:




