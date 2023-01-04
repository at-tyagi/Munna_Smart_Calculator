response=['Welcome to smart calculator (Munna)','Enter your Maths query','My name is Munna','Thanks for using with me ','Sorry ,this is  beyond my ability']
def taking_num_from_text(string):
    L=[]
    for word in string.split(' '):
        try:
            L.append(float(word))
        except ValueError:
            pass
    return L
def lcm(a,b):
    L=a if a>b else b
    while L<=a*b:
        if L%a==0 and L%b==0:
            return L
        L+=1
 
def hcf(a,b):
    H=a if a<b else b
    while H>=1:
        if a%H==0 and b%H==0:
            return H
        H-=1
 
def add(a,b):
    return a+b
 
def sub(a,b):
    return a-b
 
def mul(a,b):
    return a*b
 
def div(a,b):
    return a/b
 
def mod(a,b):
    return a%b

def end():
    print(response[3])
    exit()
  
def myname():
    print(response[2])
def sorry():
    print(response[4])

operations={'ADD':add,'PLUS':add,'SUM':add,'ADDITION':add,
            'SUB':sub,'SUBTRACT':sub, 'MINUS':sub,
            'DIFFERENCE':sub,'LCM':lcm,'HCF':hcf,
            'PRODUCT':mul, 'MULTIPLY':mul,'MULTIPLICATION':mul,
            'DIVISION':div,'MOD':mod,'REMAINDER'
            :mod,'MODULAS':mod}
commands={'NAME':myname,'EXIT':end,'END':end,'CLOSE':end}
