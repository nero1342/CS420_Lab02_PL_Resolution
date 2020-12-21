from KnowledgeBase import KnowledgeBase, Clause
from PLResolution import PLResolution
import argparse

def input(input_path):
    with open(input_path, "r") as f:
        alpha = f.readline() 
        n = int(f.readline())
        clauses = []
        for i in range(n):
            clause = f.readline()
            clauses.append(clause)
    return alpha, clauses 

def solve(alpha, clauses, output_path, mode):
    kb = KnowledgeBase()
    for clause in clauses:
        kb.add_clause(clause=clause, form=0)

    if mode == 'p':
        solver = PLResolution(output_path) 
    elif mode == 'd':
        solver = DPLL(output_path) 
    else:
        assert(-1)

if __name__ == "__main__":
    parser = argparse.ArgumentParser() 
    parser.add_argument('--inp', default="input.txt", help="Path of input file")
    parser.add_argument('--out', default="output.txt", help="Path of output file")
    parser.add_argument('--mode', default="p", help="p/d (PL-Resolution/David-Putnam)")
    args = parser.parse_args()
    
    clause = "-A AND B"
    c = Clause(clause, 1)
    print(c.literals, c.form)
    c.negate()
    print(c.literals, c.form)
    print(c.to_string())

    d = Clause("-B OR A", 0) 
    if c == d:
        print("Equal")