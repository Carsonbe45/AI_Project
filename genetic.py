from random import choices, randint, randrange, random, sample
from typing import List, Optional, Callable, Tuple

Genome = List[int]
Population = List[Genome]
PopulateFunc = Callable[[], Population]
FitnessFunc = Callable[[Genome], int]
SelectionFunc = Callable[[Population, FitnessFunc], Tuple[Genome, Genome]]
CrossoverFunc = Callable[[Genome, Genome], Tuple[Genome, Genome]]
MutationFunc = Callable[[Genome], Genome]
PrinterFunc = Callable[[Population, int, FitnessFunc], None]

# generates a genome of length 'length' given by the argument, 
# 'choices' from 'random' module chooses 'length' values from 
# an array of given options (0 and 1)
def generate_genome(length: int) -> Genome:
  return choices([0, 1], k=length)

# generates a population of genomes, size determines number of members
# of population, genome_length determines... genome length
def generate_population(size: int, genome_length: int) -> Population:
  return [generate_genome(genome_length) for _ in range(size)]

#
def single_point_crossover(a: Genome, b: Genome) -> Tuple[Genome, Genome]:
  if len(a) != len(b):
    raise ValueError("Given genomes must be of same length")
  
  # avoids unnecessary crossover if genome sizes are smaller than 2
  length = len(a)
  if length < 2:
    return a, b
  
  # p is a random int between 1 and the length of the genomes
  # combines a from index 0 to p and b from p to the end
  # and vice versa
  p = randint(1, length - 1)
  return a[0:p] + b[p:], b[0:p] + a[p:]