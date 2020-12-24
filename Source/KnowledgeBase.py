from Clause import Clause
class KnowledgeBase:
    def __init__(self):
        self.clauses = []
        
    def add_clause(self, clause, form = 0):
        print(clause, form)
        c = Clause(clause, form)
        print("Clause ", c.to_string()) 
        if form == 1:
            c.negate() 
            clauses = [Clause(c.int2literal(x)) for x in c.literals]
            print("Hello")
            for clause in clauses:
                self.clauses.append(clause)
                print(clause.to_string())
            print("End hello")
        else:
            self.clauses.append(c) 
