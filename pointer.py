class P:
    # virtual Pointer in PYTHON
    def __init__(self, mem_p, num=0):
        self.mem_p = mem_p
        self.copy_mem_p = []
        if type(self.mem_p) != list:
            self.mem_p = list(mem_p)
        for i, mem_p_v in enumerate(self.mem_p):
            self.copy_mem_p.append({i: mem_p_v})
        self.num = num
        self.Next_p = self.copy_mem_p[num]
        
    def __add__(self, slice_number):
        i = int(self.num + slice_number)
        self.num = i
        if i > len(self.copy_mem_p)-1:
            a = int(list(map(int, self.copy_mem_p[-1].keys()))[0])
            box = {a+i+1: '0x'+str(a+i+1) for i in range(i-len(self.mem_p)+1)}
            box = [{i[0]: i[1]} for i in box.items()]
            self.copy_mem_p += box
            self.Next_p = self.copy_mem_p[-1]
        else:
            self.Next_p = self.copy_mem_p[i] 

        print(self.num)
        
        # print(self.copy_mem_p)
        # print(self.Next_p)

    def __le__(self, v): ## a <= b
        a = int(list(map(int, self.Next_p.keys()))[0])
        for i in self.copy_mem_p:
            if str(list(map(int, i.keys()))).find(str(a)) == 1:
                i[a] = v
        print(self.copy_mem_p)

    def __sub__(self, slice_number):
        pass

p1 = P([1, 2, 3, 4, 33])
p1 + 3
p1 <= 0
p1 + 7
p1 <= 88
        
