from Population import Population

target = "Abduelah Hajjar"
population_num = 1000
mutation_rate = 0.01

population = Population(target, mutation_rate, population_num)

while(not population.finished):
    # Will stop the loop if it found the target
    population.evaluate()

    # Will calculate the fitness for each DNA (Individual)
    population.calcFitness()

    # Will print the best fitness for each generation
    population.printBest()

    population.naturalSelection()

    population.generate()



