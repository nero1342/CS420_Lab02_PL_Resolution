class KnowledgeBase:
    def __init__(self):
        self.clauses = []
        
    def add_clause(self, clause, form):
        c = Clause(clause, form)
        if form == 1:
            c.negate() 
        
        self.clauses.append(c) 
