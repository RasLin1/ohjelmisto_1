import random

short_loop_counter = 0 
short_num_list = []
while  short_loop_counter < 3:
    temp_var = random.randint(1, 9)
    short_num_list.append(temp_var)
    short_loop_counter += 1


long_loop_counter = 0 
long_num_list = []
while  long_loop_counter < 4:
    temp_var = random.randint(1, 6)
    long_num_list.append(temp_var)
    long_loop_counter += 1

print(f"Lyhyt numero sarja: {short_num_list}")
print(f"Pitkä numero sarja: {long_num_list}")
