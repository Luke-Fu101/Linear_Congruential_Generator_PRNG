import random
key_length = 128 
seed_list = [] 
binary_bit_list = [] 

def LCG():
    seed = random.randint(0, 65535) # Kept within modulus limit
    a = 1664525
    c = 1013904223
    m = 4294967296
    for i in range(key_length):
        seed = (a * seed + c) % m 
        
        # FIX: Shift right by 4 bits to escape the alternating even/odd trap
        binary_bit = (seed >> 31) % 2 
        
        seed_list.append(seed) 
        binary_bit_list.append(binary_bit) 
        print(binary_bit)
    return binary_bit_list

LCG()