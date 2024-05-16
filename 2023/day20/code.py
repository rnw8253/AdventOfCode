from collections import deque
import numpy as np

class Module:
    def __init__(self, name, modType, outputs):
        self.name = name
        self.modType = modType
        self.outputs = outputs
        if modType == "%":
            self.memory = "off"
        else:
            self.memory = {}

    def __repr__(self):
        return self.name + "{type=" + self.modType + ", outputs=" + ",".join(self.outputs) + ",memory=" + str(self.memory)  + "}"
    
class CommunicationModule:
    def __init__(self, fname):
        self.modules = {}
        for line in open(fname).read().splitlines():
            inputs, destinations = line.split(" -> ")
            outputs = destinations.split(", ")
            if inputs == "broadcaster":
                self.modules[inputs] = Module(inputs, inputs, outputs)
            else:
                modType = inputs[0]
                label = inputs[1:]
                self.modules[label] = Module(label, modType, outputs)

        for label, module in self.modules.items():
            for output in module.outputs:
                if output in self.modules and self.modules[output].modType == "&":
                    self.modules[output].memory[label] = "low"
                
        #print(self.modules)

    def pushButton(self):
        low_count = 1
        high_count = 0
        q = deque([("broadcaster", x, "low") for x in self.modules["broadcaster"].outputs])
        while q:
            origin, target, pulse = q.popleft()
            if pulse == "low":
                low_count += 1
            else:
                high_count += 1
            # Do nothing if target is output
            if target in self.modules:
                module = self.modules[target]
                if module.modType == "%":
                    if pulse == "low":
                        module.memory = "on" if module.memory == "off" else "off"
                        outgoing = "high" if module.memory == "on" else "low"
                        for output in module.outputs:
                            q.append((module.name, output, outgoing))
                elif module.modType == "&":
                    module.memory[origin] = pulse
                    outgoing = "low" if all(x == "high" for x in module.memory.values()) else "high"
                    for output in module.outputs:
                        q.append((module.name, output, outgoing))
 
        return int(high_count), int(low_count)

    def pulsesAfterXPresses(self, x):
        total = [0,0]
        for _ in range(1000):
            high, low =  self.pushButton()
            total[0] += high
            total[1] += low
        print(int(total[0]*total[1]))



            
C = CommunicationModule('test2.dat')
C.pulsesAfterXPresses(1000)

C = CommunicationModule('test.dat')
C.pulsesAfterXPresses(1000)

C = CommunicationModule('data.dat')
C.pulsesAfterXPresses(1000)

