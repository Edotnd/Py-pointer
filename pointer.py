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
            for j in self.copy_mem_p:
                if int(list(map(int, j.keys()))[0]) == i:
                    self.Next_p = j
        print(self.num, self.Next_p) 

        # print(self.num)
        
        # print(self.copy_mem_p)
        # print(self.Next_p)

    def __le__(self, v): ## a <= b
        a = int(list(map(int, self.Next_p.keys()))[0])
        for i in self.copy_mem_p:
            if int(list(map(int, i.keys()))[0]) == a:
                i[a] = v
        # print(self.copy_mem_p)

    def __sub__(self, slice_number):
        i = int(self.num - slice_number)
        self.num = i
        if i < 0:
            a = int(list(map(int, self.copy_mem_p[0].keys()))[0])
            box = {a+z: '-0x'+str(-(a+z)) for z in range(i, a)}
            box = [{i[0]: i[1]} for i in box.items()]
            self.copy_mem_p = box + self.copy_mem_p
            # print(self.copy_mem_p)
            self.Next_p = self.copy_mem_p[0]
        else:
            for j in self.copy_mem_p:
                if int(list(map(int, j.keys()))[0]) == i:
                    self.Next_p = j
        print(self.num, self.Next_p)
        # print(self.copy_mem_p)
        # print(self.Next_p)
        # print(self.num)

p1 = P([1, 2, 3, 4, 33])
p1 + 3
p1 <= 7
p1 - 7
p1 <= 8
p1 + 6
p1 <= 9999
print(p1.copy_mem_p)