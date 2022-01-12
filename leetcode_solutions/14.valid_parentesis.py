'''Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.'''


class Solution:
    def isValid(self, s: str) -> bool:
        coppie={
                '(':')',
                '{':'}',
                '[':']'
        }

        stack=[]                #una lista che verrà utilizzata come pila (l'ultimo elemento della lista è quello con priorità)

        if(len(s)%2==1):
            return False
        for i in s:
            #se è una parentesi di apertura (ovvero una chiave del dizionario)
            if i in coppie:
                print(i)
                stack.append(i)
            
            else:
                try:
                    j=stack.pop()
                    print (j)

                    if coppie[j]!=i:                #se l'ultima parentesi aperta non è chiusa da quella corrente, allora esci
                        return False
                except:
                    return False
        if len(stack)!=0:
            return False
        return True

def main():
    s=Solution()
    print(s.isValid("){"))
if __name__=="__main__":main()
                
            