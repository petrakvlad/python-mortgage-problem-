class Dict_hash(object):
    def __init__(self, num_buckets):
        self.num_buckets = num_buckets
        self.buckets = []
        for i in range(num_buckets):
            self.buckets.append([])

    def print(self):
        print(self.buckets)
    
    def add_keyval(self, key, vallue):
        number = self.buckets[key%self.num_buckets]
        for n in range(len(number)):
            if number[n][0] == key:
                number[n][1] = vallue
                return
        number.append([key, vallue])

    def get_value(self, key):

        buck = self.buckets[key%self.num_buckets]
        for each in buck:
            if each[0] == key:
                return each[1]
        return None
    

        



inst = Dict_hash(5)
inst.print()
inst.add_keyval(3, "valera")
inst.print()
inst.add_keyval(4, "kola")
inst.print()
inst.add_keyval(3, "artemi")
inst.print()
n = inst.get_value(3)
print(n)

