# -*- coding: utf-8 -*-
"""BitVectorDemo.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1NoLVEBqkvrHwoYoEuxX0BeJvaJ5MtVrA
"""

"""pip install BitVector"""


"""Tables"""
import random

from BitVector import *
Sbox = (
    0x63, 0x7C, 0x77, 0x7B, 0xF2, 0x6B, 0x6F, 0xC5, 0x30, 0x01, 0x67, 0x2B, 0xFE, 0xD7, 0xAB, 0x76,
    0xCA, 0x82, 0xC9, 0x7D, 0xFA, 0x59, 0x47, 0xF0, 0xAD, 0xD4, 0xA2, 0xAF, 0x9C, 0xA4, 0x72, 0xC0,
    0xB7, 0xFD, 0x93, 0x26, 0x36, 0x3F, 0xF7, 0xCC, 0x34, 0xA5, 0xE5, 0xF1, 0x71, 0xD8, 0x31, 0x15,
    0x04, 0xC7, 0x23, 0xC3, 0x18, 0x96, 0x05, 0x9A, 0x07, 0x12, 0x80, 0xE2, 0xEB, 0x27, 0xB2, 0x75,
    0x09, 0x83, 0x2C, 0x1A, 0x1B, 0x6E, 0x5A, 0xA0, 0x52, 0x3B, 0xD6, 0xB3, 0x29, 0xE3, 0x2F, 0x84,
    0x53, 0xD1, 0x00, 0xED, 0x20, 0xFC, 0xB1, 0x5B, 0x6A, 0xCB, 0xBE, 0x39, 0x4A, 0x4C, 0x58, 0xCF,
    0xD0, 0xEF, 0xAA, 0xFB, 0x43, 0x4D, 0x33, 0x85, 0x45, 0xF9, 0x02, 0x7F, 0x50, 0x3C, 0x9F, 0xA8,
    0x51, 0xA3, 0x40, 0x8F, 0x92, 0x9D, 0x38, 0xF5, 0xBC, 0xB6, 0xDA, 0x21, 0x10, 0xFF, 0xF3, 0xD2,
    0xCD, 0x0C, 0x13, 0xEC, 0x5F, 0x97, 0x44, 0x17, 0xC4, 0xA7, 0x7E, 0x3D, 0x64, 0x5D, 0x19, 0x73,
    0x60, 0x81, 0x4F, 0xDC, 0x22, 0x2A, 0x90, 0x88, 0x46, 0xEE, 0xB8, 0x14, 0xDE, 0x5E, 0x0B, 0xDB,
    0xE0, 0x32, 0x3A, 0x0A, 0x49, 0x06, 0x24, 0x5C, 0xC2, 0xD3, 0xAC, 0x62, 0x91, 0x95, 0xE4, 0x79,
    0xE7, 0xC8, 0x37, 0x6D, 0x8D, 0xD5, 0x4E, 0xA9, 0x6C, 0x56, 0xF4, 0xEA, 0x65, 0x7A, 0xAE, 0x08,
    0xBA, 0x78, 0x25, 0x2E, 0x1C, 0xA6, 0xB4, 0xC6, 0xE8, 0xDD, 0x74, 0x1F, 0x4B, 0xBD, 0x8B, 0x8A,
    0x70, 0x3E, 0xB5, 0x66, 0x48, 0x03, 0xF6, 0x0E, 0x61, 0x35, 0x57, 0xB9, 0x86, 0xC1, 0x1D, 0x9E,
    0xE1, 0xF8, 0x98, 0x11, 0x69, 0xD9, 0x8E, 0x94, 0x9B, 0x1E, 0x87, 0xE9, 0xCE, 0x55, 0x28, 0xDF,
    0x8C, 0xA1, 0x89, 0x0D, 0xBF, 0xE6, 0x42, 0x68, 0x41, 0x99, 0x2D, 0x0F, 0xB0, 0x54, 0xBB, 0x16,
)

InvSbox = (
    0x52, 0x09, 0x6A, 0xD5, 0x30, 0x36, 0xA5, 0x38, 0xBF, 0x40, 0xA3, 0x9E, 0x81, 0xF3, 0xD7, 0xFB,
    0x7C, 0xE3, 0x39, 0x82, 0x9B, 0x2F, 0xFF, 0x87, 0x34, 0x8E, 0x43, 0x44, 0xC4, 0xDE, 0xE9, 0xCB,
    0x54, 0x7B, 0x94, 0x32, 0xA6, 0xC2, 0x23, 0x3D, 0xEE, 0x4C, 0x95, 0x0B, 0x42, 0xFA, 0xC3, 0x4E,
    0x08, 0x2E, 0xA1, 0x66, 0x28, 0xD9, 0x24, 0xB2, 0x76, 0x5B, 0xA2, 0x49, 0x6D, 0x8B, 0xD1, 0x25,
    0x72, 0xF8, 0xF6, 0x64, 0x86, 0x68, 0x98, 0x16, 0xD4, 0xA4, 0x5C, 0xCC, 0x5D, 0x65, 0xB6, 0x92,
    0x6C, 0x70, 0x48, 0x50, 0xFD, 0xED, 0xB9, 0xDA, 0x5E, 0x15, 0x46, 0x57, 0xA7, 0x8D, 0x9D, 0x84,
    0x90, 0xD8, 0xAB, 0x00, 0x8C, 0xBC, 0xD3, 0x0A, 0xF7, 0xE4, 0x58, 0x05, 0xB8, 0xB3, 0x45, 0x06,
    0xD0, 0x2C, 0x1E, 0x8F, 0xCA, 0x3F, 0x0F, 0x02, 0xC1, 0xAF, 0xBD, 0x03, 0x01, 0x13, 0x8A, 0x6B,
    0x3A, 0x91, 0x11, 0x41, 0x4F, 0x67, 0xDC, 0xEA, 0x97, 0xF2, 0xCF, 0xCE, 0xF0, 0xB4, 0xE6, 0x73,
    0x96, 0xAC, 0x74, 0x22, 0xE7, 0xAD, 0x35, 0x85, 0xE2, 0xF9, 0x37, 0xE8, 0x1C, 0x75, 0xDF, 0x6E,
    0x47, 0xF1, 0x1A, 0x71, 0x1D, 0x29, 0xC5, 0x89, 0x6F, 0xB7, 0x62, 0x0E, 0xAA, 0x18, 0xBE, 0x1B,
    0xFC, 0x56, 0x3E, 0x4B, 0xC6, 0xD2, 0x79, 0x20, 0x9A, 0xDB, 0xC0, 0xFE, 0x78, 0xCD, 0x5A, 0xF4,
    0x1F, 0xDD, 0xA8, 0x33, 0x88, 0x07, 0xC7, 0x31, 0xB1, 0x12, 0x10, 0x59, 0x27, 0x80, 0xEC, 0x5F,
    0x60, 0x51, 0x7F, 0xA9, 0x19, 0xB5, 0x4A, 0x0D, 0x2D, 0xE5, 0x7A, 0x9F, 0x93, 0xC9, 0x9C, 0xEF,
    0xA0, 0xE0, 0x3B, 0x4D, 0xAE, 0x2A, 0xF5, 0xB0, 0xC8, 0xEB, 0xBB, 0x3C, 0x83, 0x53, 0x99, 0x61,
    0x17, 0x2B, 0x04, 0x7E, 0xBA, 0x77, 0xD6, 0x26, 0xE1, 0x69, 0x14, 0x63, 0x55, 0x21, 0x0C, 0x7D,
)

Mixer = [
    [BitVector(hexstring="02"), BitVector(hexstring="03"), BitVector(hexstring="01"), BitVector(hexstring="01")],
    [BitVector(hexstring="01"), BitVector(hexstring="02"), BitVector(hexstring="03"), BitVector(hexstring="01")],
    [BitVector(hexstring="01"), BitVector(hexstring="01"), BitVector(hexstring="02"), BitVector(hexstring="03")],
    [BitVector(hexstring="03"), BitVector(hexstring="01"), BitVector(hexstring="01"), BitVector(hexstring="02")]
]

InvMixer = [
    [BitVector(hexstring="0E"), BitVector(hexstring="0B"), BitVector(hexstring="0D"), BitVector(hexstring="09")],
    [BitVector(hexstring="09"), BitVector(hexstring="0E"), BitVector(hexstring="0B"), BitVector(hexstring="0D")],
    [BitVector(hexstring="0D"), BitVector(hexstring="09"), BitVector(hexstring="0E"), BitVector(hexstring="0B")],
    [BitVector(hexstring="0B"), BitVector(hexstring="0D"), BitVector(hexstring="09"), BitVector(hexstring="0E")]
]

# b = BitVector(hexstring="4E")
# int_val = b.intValue()
# s = Sbox[int_val]
# s = BitVector(intVal=s, size=8)
# print(s.get_bitvector_in_hex())

# AES_modulus = BitVector(bitstring='100011011')

# bv1 = BitVector(hexstring="02")
# bv2 = BitVector(hexstring="63")
# bv3 = bv1 ^ bv2
# bv3 = bv1.gf_multiply_modular(bv2, AES_modulus, 8)
# print(bv3)

rc = ["00" , "01" , "02" , "04" , "08" , "10" , "20" , "40" , "80" , "1B" , "36" , "6C"]
fixed = [['02','03','01','01'],['01','02','03','01'],['01','01','02','03'],['03','01','01','02']]
inv_fixed = [['0e','0b','0d','09'],['09','0e','0b','0d'],['0d','09','0e','0b'],['0b','0d','09','0e']]


def list_to_str(list):
    str = ""
    for i in range(0 , len(list)):
        str += list[i]
    return str

def str_to_list(str):
    list = []
    for i in range(0 , len(str)):
        list.append(str[i])
    return list

def make_list(key):
    text = []
    for i in range(0 , len(key)):
        text.append(key[i])
    return char_to_hex(text)

def iv_generator():
    list = ['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f']
    iv = []
    while len(iv) < 16:
        i = random.randint(0,15)
        j = random.randint(0,15)
        s = list[i] + list[j]
        iv.append(s)
    return iv


def divide_string_into_chunks(input_string, chunk_size=16):
    num_chunks = (len(input_string) + chunk_size - 1) // chunk_size
    chunks = [input_string[i * chunk_size: (i + 1) * chunk_size] for i in range(num_chunks)]
    chunks = [chunk.ljust(chunk_size) for chunk in chunks]
    return chunks


def char_to_hex(key):
    text = []
    for i in range(0 , len(key)):
        c = key[i]
        b = BitVector(intVal=ord(c) , size=8)
        text.append(b.get_bitvector_in_hex())
    return text

def convert_to_mat(key):
    w = []
    for i in range(0 ,len(key) , 4):
        t = []
        for j in range(i , i + 4):
            c = key[j]
            b = BitVector(intVal=ord(c) , size=8)
            t.append(b.get_bitvector_in_hex())
        w.append(t)
    return w


def convert_to_cipher_mat(key):
    w = []
    for i in range(0 ,len(key) , 4):
        t = []
        for j in range(i , i + 4):
            c = key[j]
            t.append(c)
        w.append(t)
    return w


def reverse_w(w):
    n = len(w)
    m = len(w[0])
    t = []
    for i in range(0 , n):
        d = []
        for j in range(0 , m):
            d.append(0)
        t.append(d)
    j = 40
    for i in range(0 , 44 , 4):
        #print(i , j)
        for k in range(0 , 4):
            t[i + k] = w[j + k]
        j = j - 4
    return t


def left_shift(list , offset):
    offset %= len(list)
    list = list[offset:] + list[:offset]
    return list


def right_shift(list , offset):
    offset %= len(list)
    list = list[-offset:] + list[:-offset]
    return list


def byte_substitution(tt):
    b = BitVector(hexstring=tt)
    int_val = b.intValue()
    s = Sbox[int_val]
    s = BitVector(intVal=s, size=8)
    return s


def inv_byte_substitution(tt):
    b = BitVector(hexstring=tt)
    int_val = b.intValue()
    s = InvSbox[int_val]
    s = BitVector(intVal=s, size=8)
    return s


def g(list , i):
    t = left_shift(list[-1] , 1)
    ans = []
    for tt in t:
        s = byte_substitution(tt)
        ans.append(s.get_bitvector_in_hex())
    a = BitVector(hexstring=rc[i])
    b = BitVector(hexstring=ans[0])
    c = a ^ b
    ans[0] = c.get_bitvector_in_hex()
    return ans


def xor_str(list1 , list2):
    list = ""
    for i in range(0 , len(list1)):
        a = BitVector(hexstring=list1[i])
        b = BitVector(hexstring=list2[i])
        c = a ^ b
        list += c.get_bitvector_in_hex()
    print("hoga " , list)
    return list


def xor(list1 , list2):
    list = []
    for i in range(0 , len(list1)):
        a = BitVector(hexstring=list1[i])
        b = BitVector(hexstring=list2[i])
        c = a ^ b
        list.append(c.get_bitvector_in_hex())
    return list


def addRoundKey(w , gw , ix):
    t = []
    for i in range(0 , 4):
        list1 = w[len(w) - (4 - i)]
        if i == 0:
            list2 = gw[-1]
            t.append(xor(list1 , list2))
        else:
            list2 = t[-1]
            t.append(xor(list1 , list2))
    for tt in t:
        w.append(tt)
    gw.append(g(w , ix))


def convert_row_to_column(mat):
    n = len(mat)
    m = len(mat[0])
    w = []
    for j in range(0 , m):
        t = []
        for i in range(0 , n):
            t.append(mat[i][j])
        w.append(t)

    return w


def add_mat(m1 , m2):
    w = []
    for i in range(0, len(m1)):
        t = []
        for j in range(0 , len(m1[0])):
            a = BitVector(hexstring=m1[i][j])
            b = BitVector(hexstring=m2[i][j])
            c = a ^ b
            t.append(c.get_bitvector_in_hex())
        w.append(t)
    return w


def something(mat1 , mat2 , ix):
    for i in range(0 , len(mat1)):
        for j in range(0 , len(mat1[0])):
            k = mat1[i][j]
            k = byte_substitution(k)
            mat1[i][j] = k.get_bitvector_in_hex()
    for i in range(0 , len(mat1)):
        t = mat1[i]
        t = left_shift(t , i)
        mat1[i] = t
    if ix != 10:
        mix_col = []
        AES_modulus = BitVector(bitstring='100011011')
        for i in range(0,4):
            t = []
            for j in range(0,4):
                c = BitVector(hexstring="00")
                for k in range(0 , 4):
                    a = BitVector(hexstring=fixed[i][k])
                    b = BitVector(hexstring=mat1[k][j])
                    d = a.gf_multiply_modular(b, AES_modulus, 8)
                    c = c ^ d
                t.append(c.get_bitvector_in_hex())
            mix_col.append(t)
        return add_mat(mix_col , mat2)
    else:
        return add_mat(mat1 , mat2)
    

def some(w , prev):
    gggg = []
    dddd = [prev[0] , prev[1] , prev[2] , prev[3]]
    dddd = convert_row_to_column(dddd)
    eeee = [w[0] , w[1] , w[2] , w[3]]
    eeee = convert_row_to_column(eeee)
    gggg.append(add_mat(dddd , eeee))
    for i in range(1 , 11):
        mat1 = []
        mat2 = gggg[-1]
        for j in range(4 * i , 4 * i + 4):
            mat1.append(w[j])
        state_mat = mat2
        roundkey = convert_row_to_column(mat1)
        gggg.append(something(state_mat , roundkey , i))
    return gggg[-1]


def aes_encryption(key , text , xval):
    w = []
    prev = []
    text = xor(text , xval)

    w = convert_to_cipher_mat(key)
    prev = convert_to_cipher_mat(text)

    gw = []
    gw.append(g(w , 1))


    for i in range (2 , 12):
        addRoundKey(w , gw , i)

    cipher_array = some(w , prev)
    cipher = []
    for i in range(0 , len(cipher_array)):
        for j in range(0 , len(cipher_array[0])):
            cipher.append(cipher_array[j][i])
    return cipher


def inv_something(mat1 , mat2 , ix):
    for i in range(0 , len(mat1)):
        t = mat1[i]
        t = right_shift(t , i)
        mat1[i] = t
    for i in range(0 , len(mat1)):
        for j in range(0 , len(mat1[0])):
            k = mat1[i][j]
            k = inv_byte_substitution(k)
            mat1[i][j] = k.get_bitvector_in_hex()
    mat1 = add_mat(mat1 , mat2)
    if ix == 10:
        return mat1
    else:
        mix_col = []
        AES_modulus = BitVector(bitstring='100011011')
        for i in range(0,4):
            t = []
            for j in range(0,4):
                c = BitVector(hexstring="00")
                for k in range(0 , 4):
                    a = BitVector(hexstring=inv_fixed[i][k])
                    b = BitVector(hexstring=mat1[k][j])
                    d = a.gf_multiply_modular(b, AES_modulus, 8)
                    c = c ^ d
                t.append(c.get_bitvector_in_hex())
            mix_col.append(t)
        return mix_col


def inv_some(w , prev):
    gggg = []
    dddd = [prev[0] , prev[1] , prev[2] , prev[3]]
    dddd = convert_row_to_column(dddd)
    eeee = [w[0] , w[1] , w[2] , w[3]]
    eeee = convert_row_to_column(eeee)
    gggg.append(add_mat(dddd , eeee))
    for i in range(1 , 11):
        mat1 = []
        mat2 = gggg[-1]
        for j in range(4 * i , 4 * i + 4):
            mat1.append(w[j])
        state_mat = mat2
        roundkey = convert_row_to_column(mat1)
        gggg.append(inv_something(state_mat , roundkey , i))
    return gggg[-1]


def aes_decryption(key , text , xval):
    w = []
    prev = []
    

    w = convert_to_cipher_mat(key)
    prev = convert_to_cipher_mat(text)


    gw = []
    gw.append(g(w , 1))


    for i in range (2 , 12):
        addRoundKey(w , gw , i)

    w = reverse_w(w)

    cipher_array = inv_some(w , prev)
    cipher = []
    for i in range(0 , len(cipher_array)):
        for j in range(0 , len(cipher_array[0])):
            cipher.append(cipher_array[j][i])
    cipher = xor(cipher , xval)
    return cipher


# print(iv)

def cbc_encrypt(key , text , aiv):
    key_list = str_to_list(key)
    text_list = divide_string_into_chunks(text)
    cipher_texts = []
    iv = []
    for i in range(0 , len(aiv)):
        a = aiv[i]
        iv.append(a)
    for i in range(0 , len(text_list)):
        if i == 0:
            cipher_list = aes_encryption(key_list , char_to_hex(text_list[0]) , iv)
            cipher_texts.append(cipher_list)
        else:
            cipher_list = aes_encryption(key_list , char_to_hex(text_list[i]) , cipher_texts[-1])
            cipher_texts.append(cipher_list)
    return cipher_texts

def cbc_decrypt(key , text , aiv):
    key_list = str_to_list(key)
    plain_texts = []
    cipher_texts = []
    iv = []
    for i in range(0 , len(aiv) , 2):
        a = aiv[i]
        b = aiv[i + 1]
        c = a + b
        iv.append(c)
    for t in text :
        l = []
        for i in range(0 , len(t) , 2):
            a = t[i]
            b = t[i + 1]
            c = t[i] + t[i + 1]
            l.append(c)
        cipher_texts.append(l)
    for i in range(0 , len(cipher_texts)):
        if i == 0:
            plain_text = aes_decryption(key_list , cipher_texts[i] , iv)
            plain_texts.append(plain_text)
        else:
            plain_text = aes_decryption(key_list , cipher_texts[i] , cipher_texts[i - 1])
            plain_texts.append(plain_text)
    strlist = []
    for i in plain_texts:
        txt = list_to_str(i)
        strlist.append(''.join([chr(int(''.join(c), 16)) for c in zip(txt[0::2],txt[1::2])]))
    return strlist

