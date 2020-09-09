import random as rnd

class DNA:
    def __init__(self, gene_length):
        self.gene_length = gene_length
        self.genes = []
        self.fitness = 0.0

        for i in range(gene_length):
            self.genes.append(self.newChar())

    def newChar(self):
        c = round(rnd.randint(63, 122))
        if c == 63:
            c = 32
        if c == 64:
            c = 46
        return chr(int(c))

    def getPhrase(self):
        return "".join(self.genes)

    def calcFitness(self, target):
        score = 0
        for i in range(len(target)):
            if self.genes[i] == target[i]:
                score+=1

        self.fitness = score / float(len(target))


    def crossover(self, other_dna):
        child = DNA(self.gene_length)
        mid_point = rnd.randint(0, self.gene_length)

        for i in range(0, self.gene_length):
            if i < mid_point:
                child.genes[i] = other_dna.genes[i]
            else:
                child.genes[i] = self.genes[i]

        return child


    def mutate(self, rate):
        for i in range(self.gene_length):
            num = rnd.random()
            if num < rate:
                self.genes[i] = self.newChar()
