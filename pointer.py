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
        return self.Next_p

    def __le__(self, v): ## a <= b
        a = int(list(map(int, self.Next_p.keys()))[0])
        for i in self.copy_mem_p:
            if int(list(map(int, i.keys()))[0]) == a:
                i[a] = v

    def __sub__(self, slice_number):
        i = int(self.num - slice_number)
        self.num = i
        a = int(list(map(int, self.copy_mem_p[0].keys()))[0])
        if i < a:
            box = {z: '-0x'+str(-(z)) for z in range(i, a)}
            box = [{i[0]: i[1]} for i in box.items()]
            self.copy_mem_p = box + self.copy_mem_p
            self.Next_p = self.copy_mem_p[0]
        else:
            for j in self.copy_mem_p:
                if int(list(map(int, j.keys()))[0]) == i:
                    self.Next_p = j
        return self.Next_p

    def pop(self):
        a = int(list(map(int, self.Next_p.keys()))[0])
        for i in self.copy_mem_p:
            if int(list(map(int, i.keys()))[0]) == a:
                b = i[a]; i[a] = '0x'+str(a) if a >= 0 else '-0x'+str(a)
                return b

    def __gt__(self, ver): ## x>y calls x.__gt__(y)
        x = self.copy_mem_p if ver == 'mp' else (
            self.Next_p if ver == 'np' else (
                self.num if ver == 'N' else 'error : '+ver
            )
        )
        print(x)