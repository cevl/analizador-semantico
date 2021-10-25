import analizador_sintactico as sintac
import re

identifier = sintac.identifier
symbol_table = sintac.symbol_table
print(identifier)
print(symbol_table)

sp = []


with open('tokens.json', 'r') as openfile:
    program = json.load(openfile)
    
        count = 0
    for line in program:
        sp.append([])
        count += 1
        print('Line# ', count, '\n')
        
        for token in line:
            if token in identifier.keys():
                sp[count-1].append(token)