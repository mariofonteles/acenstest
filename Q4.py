import random       '''para gerar os valores aleatorios dos vetores'''
vetor1=[]
vetor2=[]
vetor3=[]
for i in xrange(0,10):
    vetor1.insert(i,random.randint(1,100))
    vetor2.insert(i,random.randint(1,100))
for i in xrange(0, 20):
    vetor3.append(vetor1[i])
    vetor3.append(vetor2[i])
    if i==9:
        break
print ("vetor 1: %s" %vetor1)
print ("vetor 2: %s" %vetor2)
print ("vetor 3: %s" %vetor3)
