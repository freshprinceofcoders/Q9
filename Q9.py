import math
for first_num in range(1,1000000):
    for second_num in range(first_num+1, 1000):
        c_square = first_num**2 + second_num**2
        c = math.sqrt(c_square)
        if c_square == first_num**2 + second_num**2:
            if c + first_num + second_num == 1000:
                print(int(first_num*second_num*c))
        
    