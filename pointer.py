class P:
    # virtual Pointer in PYTHON
    def __init__(self, mem_p, num=0):
        self.mem_p = mem_p
        if type(self.mem_p) != list:
            self.mem_p = [self.mem_p]
        self.num = num
        self.Next_P = {num : self.mem_p[num]}
        self.origin_len = len(mem_p)
        self.sub_len = 0
        

    def __add__(self, slice_number=0):
        i = int(self.num + slice_number)
        if i > len(self.mem_p)-1:
            self.mem_p += ['0x'+str(z+self.sub_len) for z in range(len(self.mem_p)-self.origin_len, i-self.origin_len+1)]
            self.Next_P = {len(self.mem_p)-1 : self.mem_p[-1]}
            self.num = len(self.mem_p)-1
        else:
            self.num = slice_number
            self.Next_P = {self.num : self.mem_p[self.num]}

    def __le__(self, v):  ### a <= b
        self.mem_p[self.num] = v
        self.Next_P = {self.num : self.mem_p[self.num]}

    def __sub__(self, slice_number=0):
        i = int(self.num-slice_number)
        if i < 0:
            self.mem_p = ['-0x'+str(-z) for z in range(i+1, self.sub_len+1)] + self.mem_p
            self.sub_len = i
            self.Next_P = {0 : self.mem_p[0]}
        else:
            pass
            

