registers = dict()

def getRegisterValue(name):
    try:
        return registers[name]
    except KeyError:
        registers[name] = 0
        return 0

def applyTest(name, comparison, cmpVal):
    return eval('getRegisterValue(\'%s\') %s %d' % (name, comparison, int(cmpVal)))

def applyInstruction(target, operator, val):
    if operator == 'dec':
        val *= -1
    newVal = getRegisterValue(target) + val
    registers[target] = newVal

f = open("input.txt", "r")
for line in f:
    instr, condition = line.split('if')
    name = condition.strip().split()[0]
    comparison = condition.strip().split()[1]
    cmpVal = condition.strip().split()[2]
    if applyTest(name, comparison, cmpVal):
        target = instr.strip().split()[0]
        operator = instr.strip().split()[1]
        val = int(instr.strip().split()[2])
        applyInstruction(target, operator, val)

largest = 0
for k in registers.keys():
    if registers[k] > largest:
        largest = registers[k]

print largest

