listx = [11, 23, 42, 423, 5, 75]

class P:
    def __init__(self, mem_p, num=0):
        self.mem_p = mem_p
        self.Next_P = {num : self.mem_p[num]}
        self.num = num
        self.mem_init_n = 0
    def __add__(self, slice_number=0):
        i = int(self.num + slice_number)
        j =  i-(len(listx)-1) if len(listx)-1 < i else 0
        self.mem_init_n += j - 1
        self.mem_p += ['0x'+str(z) for z in range(self.mem_init_n, j+self.mem_init_n)]
        self.Next_P = {i : self.mem_p[i]}
        self.num = int([i for i, j in self.Next_P.items()][0])

p1 = P(listx)
print(p1.Next_P)


