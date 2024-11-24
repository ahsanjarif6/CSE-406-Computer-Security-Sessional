import math
import random
import libnum
from BitVector import *
import time

def is_quadratic_residue(n, p):
	if n % p == 0:
		return True
	return pow(n, (p - 1)//2, p) == 1
	

def tonelli_shanks(p, n): 
	if n % p == 0:
		return 0

	if not is_quadratic_residue(n, p):
		
		return None
	else:
		your_name = 0


	if p % 4 == 3:
		return pow(n, (p + 1)//4, p)
	
	Q = p - 1
	S = 0
	while Q % 2 == 0:
		S += 1
		Q //= 2

	z = 2
	while is_quadratic_residue(z, p):
		z += 1

	M = S
	c = pow(z, Q, p)
	t = pow(n, Q, p)
	R = pow(n, (Q + 1)//2, p)

	
	while t != 1:

		i = 0
		temp = t 
		while temp != 1:
			i += 1
			temp = (temp * temp) % p
		
		pow2 = 2 ** (M - i - 1)
		b = pow(c, pow2, p)
		M = i
		c = (b * b) % p
		t = (t * b * b) % p
		R = (R * b) % p

	return R


def get_y_value_elliptic_curve(p, a, b, x):
	n = (x * x * x + a * x + b) % p
	return tonelli_shanks(p, n)

	




def extended_gcd(a, b):
    if a == 0:
        return b, 0, 1
    else:
        g, x, y = extended_gcd(b % a, a)
        return g, y - (b // a) * x, x

def modinv(a, m):
    g, x, y = extended_gcd(a, m)
    if g != 1:
        # return 0
        raise ValueError("Modular inverse does not exist")
    else:
        return x % m


def mod(a , b):
	m = a % b
	if m < 0:
		if b < 0:
			m = m - b
		else:
			m = m + b
	return m

def genP():
    return libnum.generate_prime(128)

def genAB(p):
    while True:
        a = random.randint(1 , p - 1)
        b = random.randint(1 , p - 1)
        if (4 * a * a * a + 27 * b * b) % p != 0:
            return a , b

def genK(e):
    ka = random.randint(1 , e - 1)
    return ka

def genE(p):
    E = p + 1 - 2 * math.ceil(math.sqrt(p))
    return E

def point_doubling(x1 , y1 , a , b , p):
    s = mod(mod(3 * x1 * x1 + a , p) * modinv(mod(2 * y1 , p) , p) , p)
    x3 = mod(s * s - 2 * x1 , p)
    y3 = mod(s * (x1 - x3) - y1 , p)
    return x3 , y3

def point_addition(x1 , y1 , x2 , y2 , a , b , p):
    s = mod(mod(y2-y1 , p) * modinv(mod(x2 - x1 , p) , p) , p)
    x3 = mod(mod(s * s , p) - x1 - x2 , p)
    y3 = mod(mod(s * (x1 - x3) , p) - y1 , p)
    return x3 , y3
    


def makeG(a , b , p):
	while True:
		x = random.randint(1 , p - 1)
		y = get_y_value_elliptic_curve(p , a , b , x)
		if y == None:
			continue
		return x , y



def double_and_add(x , y , scalar , a , b , p):
	x1 = x
	y1 = y
	d = BitVector(intVal=scalar)
	for i in range(1 , len(d)):
		x1 , y1 = point_doubling(x1 , y1 ,a , b, p)
		if d[i] == 1:
			x1 , y1 = point_addition(x1 , y1 , x , y ,a , b, p)
	return x1 , y1


def showtime():
    p = genP()
    a,b = genAB(p)
    g = makeG(a,b,p)
    e = genE(p)
    ka = genK(e)
    kb = genK(e)
    start_time = time.process_time()
    A = double_and_add(g[0] , g[1] , ka , a , b , p)
    end_time = time.process_time()
    elapsed_time1 = end_time - start_time
    start_time = time.process_time()
    B = double_and_add(g[0] , g[1] , ka , a , b , p)
    end_time = time.process_time()
    elapsed_time2 = end_time - start_time
    start_time = time.process_time()
    R = double_and_add(A[0] , A[1] , kb , a , b , p)
    end_time = time.process_time()
    elapsed_time3 = end_time - start_time
    return elapsed_time1 , elapsed_time2 , elapsed_time3