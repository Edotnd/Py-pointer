listx = [11, 23, 42, 423, 5, 75]

class P:
    def __init__(self, mem_p, num=0):
        self.mem_p = mem_p
        self.Next_P = self.mem_p[num]
    def __add__(self, slice_number):
        i = self.mem_p.index(self.Next_P) + slice_number
        j =  i-(len(listx)-1) if len(listx)-1 < i else 0
        self.mem_p += ['0x'+str(z) for z in range(j)]
        self.Next_P = self.mem_p[i]

p1 = P(listx)
print(p1.mem_p)
print(p1.Next_P)
p1+7
print(p1.mem_p)