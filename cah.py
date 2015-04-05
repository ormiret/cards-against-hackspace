STA_F= "/home/ormiret/cah/statements.txt"
ANS_F= "/home/ormiret/cah/answers.txt"
import random

def rand_line(filename):
    with open(filename) as f:
        lines = f.readlines()
    return random.choice(lines).strip()

def statement():
    return rand_line(STA_F)

def answer():
    return rand_line(ANS_F)

def fill_statement():
    statement = rand_line(STA_F)
    if not "<blank>" in statement:
        return statement + " " + rand_line(ANS_F)
    while "<blank>" in statement:
        statement = statement.replace("<blank>", rand_line(ANS_F), 1)
    return statement

if __name__=="__main__":
    print fill_statement()
