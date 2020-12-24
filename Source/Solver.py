
class Solver:
    def __init__(self, kb, alpha, output_path):
        self.f = open(output_path, "w")
        
        self.kb = kb 
        
        self.kb.add_clause(alpha, 1) 

        self.newClauses = []
    
        self.numResolve = 0

    def reset_new_clauses(self):
        self.newClauses = [] 

    def print_new_clauses(self):
        print(len(self.newClauses), file = self.f) 
        for clause in self.newClauses:
            print(clause.to_string(), file = self.f)
    
    def is_finished(self):
        for clause in self.newClauses:
            if len(clause.literals) == 0:
                print("YES", file = self.f) 
                print("Total resolve: ", self.numResolve)
                return True 
        if len(self.newClauses) == 0:
            print("NO", file = self.f) 
            print("Total resolve: ", self.numResolve)
            return True 
        return False 

    