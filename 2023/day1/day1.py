import math
import regex as re

sum = 0
counter = 0

def txt2num(val):
    match val:
        case 'one':
            return str(1)
        case 'two':
            return str(2)
        case 'three':
            return str(3)
        case 'four':
            return str(4)
        case 'five':
            return str(5)
        case 'six':
            return str(6)
        case 'seven':
            return str(7)
        case 'eight':
            return str(8)
        case 'nine':
            return str(9)
        case _:
            return val

with open("./input1.txt") as f:
    for line in f.read().splitlines():
        #print(line)
        line = line.lower()

        values = re.findall(r'[0-9]|one|two|three|four|five|six|seven|eight|nine', line, overlapped=True) 

        #print(values)

        values = [txt2num(x) for x in values]

        if 'oneight' in values:
            idx = values.index('oneight')
            values[idx] = '1'
            values.insert(idx + 1, '8')
            print("Found")

        if 'eightwo' in values:
            idx = values.index("eightwo")
            values[idx] = '8'
            values.insert(idx + 1, '2')
            print("Found")

        lineVal = int(values[0] + values[-1])

        print(f"Line {counter}: {line}\tVals: {values}\tLineVal: {lineVal}\tRunning: {sum}")
        
        sum += lineVal
        counter += 1
        if counter > 10000:
            break

print(f"Sum: {sum}")



