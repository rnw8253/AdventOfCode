class HASH:
    def __init__(self):
        pass

    def ascii(self, character):
        return int(ord(character))


    def hashAlgorithm(self, inputStr):
        value = 0
        for ch in inputStr:
            value += self.ascii(ch)
            value  = value*17 % 256
        return value


class LensBoxes(HASH):
    def __init__(self, instructions):
        self.instructions = instructions
        self.boxes = [[] for _ in range(256)]
        self.focal_lengths = {}
        
    def followInstructions(self):
        for instruction in self.instructions:
            if "=" in instruction:
                label, focal_length = instruction.split("=")
                focal_length = int(focal_length)
                box_index = self.hashAlgorithm(label)
                if label not in self.boxes[box_index]:
                    self.boxes[box_index].append(label)
                self.focal_lengths[label] = focal_length
            else:
                label = instruction[:-1]
                box_index = self.hashAlgorithm(label)
                if label in self.boxes[box_index]:
                    self.boxes[box_index].remove(label)

    def focusPower(self):
        power = 0
        for box_number, box in enumerate(self.boxes, 1):
            for lens_slot, label in enumerate(box, 1):
                power += box_number * lens_slot * self.focal_lengths[label]
        return power
                    
    def show(self):
        print(self.boxes)
        print(self.focal_lengths)
        
h = HASH()


fname = 'test.dat'
print("Sum of the hash algorithm values is: %s" %(sum(map(h.hashAlgorithm, open(fname).read().split(',')))))
b = LensBoxes(open(fname).read().split(","))
b.followInstructions()
print(f"Focus power of this lens configuration is: {b.focusPower()}")

fname = 'data.dat'
print("Sum of the hash algorithm values is: %s" %(sum(map(h.hashAlgorithm, open(fname).read().split(',')))))
b = LensBoxes(open(fname).read().split(","))
b.followInstructions()
print(f"Focus power of this lens configuration is: {b.focusPower()}")
