## Not my code!!! 
# got hella confused and still dont get this puzzle XD 
#  code belongs to u/fiavolo on reddit
#  https://www.reddit.com/r/adventofcode/comments/3vr4m4/comment/cxqejzx/?utm_source=share&utm_medium=web2x&context=3
with open('2015/Day_07/data.txt') as file:
    inputs = file.read().strip().split('\n')

wires = {}
gates = []

def resolve(input):
    if str.isdigit(input):
        return int(input)
    if input == 'b':
        return 16076
    return wires.get(input)

class Gate:
    def __init__(self, command, inputs, output):
        self.command = command
        self.inputs = inputs
        self.output = output
        self.executed = False

    def has_inputs(self, wires):
        return all(resolve(input) is not None for input in self.inputs)

    def __str__(self):
        return self.command + ' [' + ' '.join(self.inputs) + '] ' + self.output

    def execute(self, wires):
        if not self.executed:
            if self.command == '->':
                wires[self.output] = resolve(self.inputs[0])
            if self.command == 'NOT':
                wires[self.output] = ~ resolve(self.inputs[0]) + 65536
            if self.command == 'AND':
                wires[self.output] = resolve(self.inputs[0]) & resolve(self.inputs[1])
            if self.command == 'OR':
                wires[self.output] = resolve(self.inputs[0]) | resolve(self.inputs[1])
            if self.command == 'LSHIFT':
                wires[self.output] = resolve(self.inputs[0]) << resolve(self.inputs[1])
            if self.command == 'RSHIFT':
                wires[self.output] = resolve(self.inputs[0]) >> resolve(self.inputs[1])
            self.executed = True
        else:
            raise Exception('Gate has already been executed')


for input in inputs:
    args = input.split()

    if args[1] == '->':
        command = '->'
        inputs = [args[0]]
        output = args[2]
    elif args[0] == 'NOT':
        command = 'NOT'
        inputs = [args[1]]
        output = args[3]
    elif args[1] in ['AND', 'OR', 'LSHIFT', 'RSHIFT']:
        command = args[1]
        output = args[4]
        inputs = [args[0], args[2]]
    else:
        raise Exception('Invalid input: {}'.format(input))
    gates.append(Gate(command, inputs, output))


while len(gates) > 0:
    gate = gates.pop(0)
    if gate.has_inputs(wires):
        gate.execute(wires)
    else:
        gates.append(gate)

print (wires['a'])