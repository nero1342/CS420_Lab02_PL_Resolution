from Solver import Solver
from Clause import Clause 

class PLResolution(Solver):
    def __init__(self, kb, alpha, output_path):
        super().__init__(kb, alpha, output_path)
        pass

    def solve(self):
        print("PL Resolution")
        while True:
            self.reset_new_clauses() 
            for clause_1 in self.kb.clauses:
                for clause_2 in self.kb.clauses:
                    if clause_1 == clause_2:
                        break 
                    newClause = self.resolve(clause_1, clause_2)
                    if (newClause in self.kb.clauses or newClause in self.newClauses or newClause.is_tautology()):
                        continue 
                    self.newClauses.append(newClause)
            self.print_new_clauses() 
            self.kb.clauses.extend(self.newClauses)
            if self.is_finished():
                return 
    
    def resolve(self, c1, c2):
        self.numResolve += 1
        set1 = set(c1.literals)
        ret = []
        n_pairs = 0
        for x in c2.literals:
            if -x in set1:
                set1.remove(-x) 
                n_pairs += 1
            else:
                ret.append(x)
        for x in set1:
            ret.append(x)
            
        if n_pairs != 1:
            return c1

        ret_clause = Clause()
        ret = sorted(ret, key=abs)
        ret_clause.literals = ret

        #print(c1.to_string(), c2.to_string(), ret , ret_clause.to_string())
        return ret_clause