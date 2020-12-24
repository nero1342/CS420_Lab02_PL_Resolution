from Solver import Solver
from Clause import Clause

class DP(Solver):
    def __init__(self, kb, alpha, output_path):
        super().__init__(kb, alpha, output_path)
        pass

    def solve(self):
        vocab = set([abs(x) for clause in self.kb.clauses for x in clause.literals])
        print("David-Putman procedure")
        for x in vocab:
            print("Resolve x = {}".format(chr(x + 64)))
            newKb = []
            clauses_contain_x = []
            clauses_contain_minus_x = []
            self.reset_new_clauses() 
            for clause in self.kb.clauses:
                self.numResolve += 2
                val_x = 0
                if clause.contains(x):
                    val_x = x
                    clauses_contain_x.append(clause) 
                if clause.contains(-x):
                    val_x = -x 
                    clauses_contain_minus_x.append(clause)
                if val_x == 0:
                    self.newClauses.append(clause)
            for clause_1 in clauses_contain_x:
                for clause_2 in clauses_contain_minus_x:
                    if clause_1 == clause_2:
                        continue  
                    newClause = self.resolve(clause_1, clause_2, x)
                    if newClause in self.kb.clauses or newClause in self.newClauses or newClause.is_tautology():
                        continue 
                    self.newClauses.append(newClause)
            self.print_new_clauses() 
            self.kb.clauses= []
            self.kb.clauses.extend(self.newClauses)
            if self.is_finished():
                return 
        self.reset_new_clauses() 
        if self.is_finished():
            return 
    def resolve(self, c1, c2, literal):
        self.numResolve += 1
        ret = []
        ret.extend(c1.literals)
        ret.extend(c2.literals) 
        ret.remove(literal)
        ret.remove(-literal)
        ret_clause = Clause()
        ret_clause.literals = list(set(ret)) 

        print(c1.to_string(), c2.to_string(), ret_clause.to_string(), literal)
        return ret_clause