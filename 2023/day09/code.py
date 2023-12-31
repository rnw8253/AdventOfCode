import numpy as np

sensor_vars = []
for line in open("data.dat").read().split("\n"):
#for line in open("data.dat").read().split("\n"):
    sensor_vars.append(list(map(int,line.split())))


ext_var = []
ext_var2 = []
for variable in sensor_vars:
    vars = []
    vars.append(variable)
    while True:
        index = len(vars)-1
        new = [vars[index][i+1] - vars[index][i] for i in range(len(vars[index])-1) ]
        if all([ v == 0 for v in new]):
            break
        else:
            vars.append(new)
    new_val = 0
    for val in vars[::-1]:
        new_val += val[-1]
    ext_var.append(new_val)


    new_val = 0
    for val in vars[::-1]:
        new_val = val[0] - new_val
    ext_var2.append(new_val)

print(f"Part 1: {np.sum(ext_var)}")
print(f"Part 2: {np.sum(ext_var2)}")


