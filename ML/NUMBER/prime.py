

def crible(n):
    if( not(isinstance(n,int))):
        raise Exception('argument errors','the parameter ' + str(n) + " is not an integer")

    prime_list = [0,0] + [ 1 for i in range(n-1)] # + (1 - np.zeros(n-1))

    for i in range(2,len(prime_list)):
        if (prime_list[i]):
            for j in range(i*i,n,i):
                prime_list[j] = 0

    return prime_list


def decompoNbaseB(n,b=10):
    if( not(isinstance(n,int))):
        raise Exception('argument errors','the parameter ' + str(n) + " is not an integer")
    if( not(isinstance(b,int))):
        raise Exception('argument errors','the parameter ' + str(b) + " is not an integer")

    exp = 0

    while( n >= b**exp):
        exp = exp +1


    chiffre=[]

    for i in range(exp-1,-1,-1):
        rest = n%(b**i)
        chiffre.append(int((n-rest)/(b**i)))
        n = rest

    return chiffre
