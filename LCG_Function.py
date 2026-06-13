import random
seed_list = [] 
binary_bit_list = [] 

def LCG(key_length):
    seed = random.randint(0, 4294967295)  # Kept within modulus limit
    a = 1664525
    c = 1013904223
    m = 4294967296 
    for i in range(key_length):
        seed = (a * seed + c) % m 
        
        # FIX: Shift right by 4 bits to escape the alternating even/odd trap
        binary_bit = (seed >> 31) % 2 
        
        seed_list.append(seed) 
        binary_bit_list.append(binary_bit) 
    return binary_bit_list

print(LCG(128))