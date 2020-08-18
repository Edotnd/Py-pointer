class P:
    def __init__(self, mem_p, num=0):
        self.mem_p = mem_p
        self.origin_file = mem_p
        self.Next_P = {num : self.mem_p[num]}
        self.num = num
        self.mem_init_n = 0

    def __add__(self, slice_number=0):
        i = int(self.num + slice_number)
        j =  i-(len(self.origin_file)-1) if len(self.origin_file)-1 < i else 0
        self.mem_init_n += j - 1
        self.mem_p += ['0x'+str(z) for z in range(self.mem_init_n, j+self.mem_init_n)]
        self.Next_P = {i : self.mem_p[i]}
        self.num = int([i for i, j in self.Next_P.items()][0])

    def __le__(self, v):  ### a <= b
        self.mem_p[self.num] = v

    def __sub__(self, slice_number=0):
        i = int(self.num - slice_number)
        if i < 0:
            self.mem_p = ['-0x'+str(-z) for z in range(i, 0)]+self.mem_p
            self.Next_P = {0 : self.mem_p[0]}
            self.num = 0
        else:
            self.num -= slice_number
            self.Next_P = {self.num : self.mem_p[self.num]}

listx = [11, 23, 42, 423, 5, 75]

p1 = P(listx)
