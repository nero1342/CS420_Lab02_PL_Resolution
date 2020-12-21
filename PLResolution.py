from Solver import Solver

class PLResolution(Solver):
    def __init__(self):
        super().__init() 
        pass

    def solve(self):
        while True:
            self.reset_new_clauses() 
            for clause_1 in kb.clauses:
                for clause_2 in kb.clauses:
                    if clause1 == clause_2:
                        break 
                    newClause = clause_1.resolve_with(clause_2)
                    if (newClause in kb.clauses or newClause in self.newClauses or newClause.is_tautology()):
                        continue 
                    self.newClauses.append(newClause)
            self.print_new_clauses() 
            kb.clauses.extend(self.newClauses)
            if self.is_finished():
                return 
            