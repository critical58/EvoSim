class Phenotype:
    def __init__(self, trait: str, symbol: chr, descriptors: list): 
        self.trait: str = trait
        self.symbol: chr = symbol
        self.descriptors: list = descriptors

    def createGenotype(self, configuration: str):
        return Genotype(configuration, self.symbol, self.descriptors)

class Genotype:
    def __init__(self, geneticID: str, symbol: chr, descriptors: list):
        self.geneticID: str = geneticID
        self.symbol: chr = symbol
        self.descriptor: str = descriptors

    def getGeneticID(self):
        geneticSequence = "".join(
            self.symbol.upper() if int(digit) else self.symbol.lower() 
            for digit in self.geneticID
        )
        return geneticSequence
    
    def display(self):
        print(self.getGeneticID())


class Genome:
    def __init__(self, genotypes: list):
        self._genotypes: list = genotypes

    def display(self):
        for genotype in self._genotypes:
            genotype.display()
        print("".join(genotype.display())) 

    # NEEDS UPDATING, DONT USE
    def crossover(self, parent):
        offspring_attributes = {}
        for attribute in parent._attributes:
            # Averaging the traits of both parents
            value1 = self._attributes[attribute]
            value2 = parent._attributes[attribute]
            offspring_attributes[attribute] = (value1 + value2) / 2
        return Genome(offspring_attributes)

# Define Phenotypes used in simulation
speed = Phenotype("Speed", "s", ["Slow", "Fast"])
metabolism = Phenotype("Metabolism", "m", ["Slow Metabolism", "Fast Metabolism"])

parent1 = Genome([speed.createGenotype("10"), metabolism.createGenotype("00")])
parent2 = Genome([speed.createGenotype("10"), metabolism.createGenotype("11")])

print("Parent 1 Genome:")
parent1.display()
print("\nParent 2 Genome:")
parent2.display()

#offspring = Genome.crossover(parent1, parent2)
#print("\nOffspring Genome:")
#offspring.display_genome()