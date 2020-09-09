import random as rnd
from DNA import DNA

class Population:
    def __init__(self, target, mutationRate, popmax):
        self.target = target
        self.mutationRate = mutationRate
        self.popmax = popmax
        self.generation = 0
        self.matingPool = []
        self.population = []
        self.finished = False
        self.got = ""

        for i in range(popmax):
            self.population.append(DNA(len(target)))

    def calcFitness(self):
        for dna in self.population:
            dna.calcFitness(self.target)

    def naturalSelection(self):
        self.matingPool = []
        maxFitness = 0
        for dna in self.population:
            if dna.fitness > maxFitness:
                maxFitness = dna.fitness

        fitness = 0
        for dna in self.population:
            if maxFitness != 0:
                fitness = dna.fitness / maxFitness
            n = int(round(fitness * 100))
            for i in range(n):
                self.matingPool.append(dna)
                
    def generate(self):
        if len(self.matingPool) != 0:
            for i in range(len(self.population)):
                a = rnd.randint(0, len(self.matingPool) - 1)
                b = rnd.randint(0, len(self.matingPool) - 1)
                dna_A = self.matingPool[a]
                dna_B = self.matingPool[b]

                new_dna = dna_A.crossover(dna_B)

                new_dna.mutate(self.mutationRate)

                self.population[i] = new_dna

        self.generation+=1

    def evaluate(self):
        for dna in self.population:
            if dna.getPhrase() == self.target:
                self.finished = True
                self.got = dna.getPhrase()


    def printPop(self):
        arr = []
        for dna in self.population:
            arr.append(dna.getPhrase())
        print(arr)

    def printBest(self):
        maxFit = 0
        dd = None
        for dna in self.population:
            if dna.fitness > maxFit:
                maxFit = dna.fitness
                dd = dna
        print(self.generation, maxFit, dd.getPhrase())

        

