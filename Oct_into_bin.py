# 10进制转2进制
def oct_into_bin_func_1(m:int):
    a=0
    i=0
    n=abs(m)
    x,y=n // 2, n % 2

    while x!=0 :

        a+=10**i*y

        i+=1
        n=x

        x,y=n // 2, n % 2

    a+=10**i*y
    if m<0:
        a=-1*a

    return a

def real_bin_func_2(n:int):
    if n>=0:
        b=bin(n).removeprefix('0b')
        
    else:
        b=bin(n).removeprefix('-0b')
        b=int(b)*(-1)
    return int(b)

if __name__=="__main__":
    print(oct_into_bin_func_1(-90))
    print(real_bin_func_2(-90))




  