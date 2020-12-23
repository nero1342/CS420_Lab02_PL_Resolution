
class Clause:
    def __init__(self, clause=None, form=0):
        # form = 0: CNF, 1: DNF
        self.form = form
        if form == 0: 
            self.literals = self.split2literals(clause, " OR ")
        else:
            self.literals = self.split2literals(clause, " AND ")
    
    def __eq__(self, other):
        return set(self.literals) == set(other.literals) 

    def split2literals(self, clause, key):
        if clause is None:
            return []
        lst = clause.split(key)
        return [self.literal2int(x) for x in lst]

    def literal2int(self, x):
        if x[0] == '-':
            assert(len(x) == 2)
            return -(ord(x[1]) - ord('A') + 1)
        else:
            assert(len(x) == 1)
            return ord(x[0]) - ord('A') + 1
        
    def int2literal(self, x):
        ch = ''
        if (x < 0):
            ch = '-'
            x = -x;    
        return ch + chr(x + ord('A') - 1)

    def negate(self):
        self.form = 1 - self.form  
        for i in range(len(self.literals)):
            self.literals[i] *= -1
    
    def to_string(self):
        if (len(self.literals) == 0):
            return "{}"
        st = self.int2literal(self.literals[0])
        link = " OR "
        for i in range(len(self.literals) - 1):
            st = st + link + self.int2literal(self.literals[i + 1])
        return st 
    
    def is_tautology(self):
        s = set([abs(x) for x in self.literals])
        return len(s) < len(self.literals)

    def contains(self, literal):
        return literal in self.literals