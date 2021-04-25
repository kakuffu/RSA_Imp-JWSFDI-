try:
   input = raw_input
except NameError:
   pass
try:
   chr = unichr
except NameError:
   pass
#Extended Eucledian   
p=int(input('Enter prime p: '))
q=int(input('Enter prime q: '))
print("Choosen primes:")
print("p =", p, ", q =", q)
n=p*q
print("n = p * q = " + str(n) + "\n")
phi=(p-1)*(q-1)
print("Euler's function (totient) [phi(n)]:", phi)
def gcd(a, b):
    while b != 0:
        c = a % b
        a = b
        b = c
    return a
#Modular Inverse
def modinv(x, mod):
    return pow(x, mod - 2, mod)
def coprimes(a):
    l = [x for x in range(2, a) 
    if gcd(a, x) == 1 
    and modinv(x, phi) != x]
    return l
print("Choose an e from a below coprimes array:\n")
print(str(coprimes(phi)), "\n")
e=int(input())
d=modinv(e,phi)
print("Your public key is a pair of numbers (e=" + str(e) + ", n=" + str(n) + ").\n")
print("Your private key is a pair of numbers (d=" + str(d) + ", n=" + str(n) + ").\n")
def encrypt_block(m):
    c = modinv(m**e, n)
    if c == None: print('No modular multiplicative inverse for block ' + str(m) + '.')
    return c
def decrypt_block(c):
    m = modinv(c**d, n)
    if m == None: print('No modular multiplicative inverse for block ' + str(c) + '.')
    return m
def encrypt_string(s):
    return ''.join(str(chr(encrypt_block(ord(x)))) for x in s)
def decrypt_string(s):
    return ''.join(str(chr(decrypt_block(ord(x)))) for x in s)
s = input("Enter a message to encrypt: ")
print("\nPlain message: " + s + "\n")
enc = encrypt_string(s)
print("Encrypted message: " + enc + "\n")
dec = decrypt_string(enc)
print("Decrypted message: " + dec + "\n")
