import random as r

class GeneticEntity:
    def __init__(self, symbol: chr, descriptors: list):
        self.symbol = symbol
        self.descriptors = descriptors

    def getGeneticSequence(self, geneticID: str):
        return "".join(
            self.symbol.upper() if int(digit) else self.symbol.lower() 
            for digit in geneticID
        )

class Phenotype(GeneticEntity):
    def __init__(self, trait: str, symbol: chr, descriptors: list):
        super().__init__(symbol, descriptors)
        self.trait = trait

    def createGenotype(self, configuration: str):
        return Genotype(configuration, self.symbol, self.descriptors)

class Genotype(GeneticEntity):
    def __init__(self, geneticID: str, symbol: chr, descriptors: list):
        super().__init__(symbol, descriptors)
        self.geneticID = geneticID

    def getGeneticID(self):
        return self.getGeneticSequence(self.geneticID)

    def display(self):
        print(self.getGeneticID())

class Genome:
    def __init__(self, genotypes: list, phenotypes: list):
        self._genotypes = genotypes
        self._phenotypes = phenotypes

    def display(self):
        for genotype in self._genotypes:
            genotype.display()

    def normaliseID(self, geneticID: str):
        return "10" if geneticID == "01" else geneticID

    def crossover(self, parent):
        child_genetic_ids = [
            r.choice([self.normaliseID(allele1 + allele2) 
            for allele1 in self._genotypes[element].geneticID 
            for allele2 in parent._genotypes[element].geneticID]) 
            for element in range(len(self._genotypes))
        ]

        child_genotypes = [
            self._phenotypes[element].createGenotype(child_genetic_ids[element]) 
            for element in range(len(self._genotypes))
        ]

        return Genome(child_genotypes, self._phenotypes)

# Define Phenotypes used in simulation
speed = Phenotype("Speed", "s", ["Slow", "Fast"])
metabolism = Phenotype("Metabolism", "m", ["Slow Metabolism", "Fast Metabolism"])
bravado = Phenotype("Bravado", "b", ["Timid", "Courageous"])

phenotypes = [speed, metabolism, bravado]

# Add these to parents
parent1 = Genome([
    speed.createGenotype("10"), 
    metabolism.createGenotype("00"), 
    bravado.createGenotype("10"),
], phenotypes)

parent2 = Genome([
    speed.createGenotype("10"), 
    metabolism.createGenotype("11"), 
    bravado.createGenotype("00")
], phenotypes)

child1 = parent1.crossover(parent2)

print("Parent 1 Genome:")
parent1.display()
print("\nParent 2 Genome:")
parent2.display()

print("\nChild Genome:")
child1.display()
