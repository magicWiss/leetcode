#Given an unsorted integer array nums, return the smallest missing positive integer.

#You must implement an algorithm that runs in O(n) time and uses constant extra space

#COMPLEXITY O(n)

#Idea->Dato l'input si eliminano tutti i numeri negativi (si ricerca il valore positivo più piccolo)
# in quanto il valore da ricercare è presente in un range da (1...len(input)+1) limitiamo la ricerca a questi numeri
#IDEA 1->trasformare l'input (lista) in un hashset e iterare da i=1 fino a len(input)+1 cercando quale elemento manca
#PROBLEMA 1->richiede memoria extra 

#IDEA 2->manipolo l'input nel seguente modo: 
# 1.itero per tutto l'array non ordinato;
#2. per ogni elemento prendo il suo valore assoluto e verifico che è nel range (1...len(input)+1)
#3. se è compreso allora, se positivo rendo negativo il valore nella posizione val-1 
#       in questo modo è possibile vedere se un generico elemento j è presente o meno
#       j è presente nell'input se l'elemento in posizone j-1 è negativo
#           3.1 se l'elemento in posizone val-1 è 0 allora lo trasogformo in -len(input)+1
#FINE MANIPOLAZIONE
#4.per tutti i numeri k compresi in (1...len(input)+1):
# verifico se input[k-1] è positivo:
#           se positivo allora non era presente nell'input originale
#           se negativo o zero era presente in qunto variato in fase di manipolazione
#se tutti negativi allora resstituisco len(inpuit)+1
class Solution:
    def firstMissingPositive(self, I):

        #eliminazione dei valori negativi
        for i in range(len(I)):
            if I[i]<0:
                I[i]=0
        
        #maniplazione input
        for i in range(len(I)):
            val=abs(I[i])
            #se val è compreso nel range (1... len(I)+1)
            if 1<= val <= len(I):
                if(I[val-1])>0:
                    I[val-1]*=-1
            #se 0 allora lo setto a -len(I)+1
                elif I[val-1]==0:
                    I[val-1]=-1*(len(I)+1)
        
        #ricerca output

        for i in range (1, len(I)+1):

            if I[i-1]>=0:
                return i
        return len(I)+1