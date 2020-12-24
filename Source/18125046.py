import argparse
from KnowledgeBase import KnowledgeBase
from Clause import Clause
from PLResolution import PLResolution
from DP import DP 

def input(input_path):
    with open(input_path, "r") as f:
        alpha = f.readline().strip()
        n = int(f.readline().strip())
        clauses = []
        for i in range(n):
            clause = f.readline().strip()
            print(clause)
            clauses.append(clause)
    return alpha, clauses 

def solve(alpha, clauses, output_path, mode):
    kb = KnowledgeBase()
    for clause in clauses:
        kb.add_clause(clause=clause, form=0)
    #alpha = Clause(alpha, form= 1)
    if mode == 'p':
        solver = PLResolution(kb, alpha, output_path) 
    elif mode == 'd':
        solver = DP(kb, alpha, output_path) 
    else:
        assert(-1)
    solver.solve()

if __name__ == "__main__":
    parser = argparse.ArgumentParser() 
    parser.add_argument('--inp', default="input.txt", help="Path of input file")
    parser.add_argument('--out', default="output.txt", help="Path of output file")
    parser.add_argument('--mode', default="p", help="p/d (PL-Resolution/David-Putnam)")
    args = parser.parse_args()
    
    input_path = args.inp 
    output_path = args.out
    mode = args.mode
    alpha, clauses = input(input_path)
    solve(alpha, clauses, output_path, mode)