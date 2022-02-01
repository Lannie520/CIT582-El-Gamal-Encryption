import random
from params import p
from params import g

def keygen():
    sk = random.randint(1, p)
    # print("sk=", sk)
    pk = pow(g, sk, p)
    # print("pk=", pk)
    return pk, sk

def encrypt(pk, m):
    r = random.randint(1, p)

    #g^r % p
    c1 = pow(g, r, p)
    #print("c1=",c1)

    #(pk^r)*m % p
    c2 = pow(pow(pk, r, p)*pow(m, 1, p), 1, p)
    # print ("c2=",c2)
    return [c1, c2]

def decrypt(sk, c):
    #Formula: m = c2/c1^-1 mod p
    m = pow(c[1] * pow(pow(c[0], sk, p), -1, p), 1, p)
    return m

# def main():

#    message = 1234567890987654321
#    print("message=", message)
#   pk, sk = keygen()
#   c = encrypt(pk, message)
#   print("Decrypted as above", decrypt(sk, c))

# if __name__ == '__main__':
#    main()

