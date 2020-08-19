import pointer as P0

p1 = P0.P([1, 2, 3, 4])
p1+1; p1<=99
print(p1.copy_mem_p)
p1-3; p1<=12
print(p1.copy_mem_p)
print(p1.num)
p1-3
p1<=99999
print(p1.copy_mem_p)