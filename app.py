print("Type dominant alleles first:")
parent1 = input("Genotype of parent 1: ")
parent2 = input("Genotype of parent 2: ")

parent1gamete1 = parent1[0]
parent1gamete2 = parent1[1]
parent2gamete1 = parent2[0]
parent2gamete2 = parent2[1]

def combine_alleles(alleleX, alleleY):
  if alleleX.isupper():
    offspring = alleleX + alleleY
    return offspring
  elif alleleY.isupper():
    offspring = alleleY + alleleX
    return offspring
  else:
    offspring = alleleX + alleleY
    return offspring

offspring1 = combine_alleles(parent1gamete1, parent2gamete1)
offspring2 = combine_alleles(parent1gamete2, parent2gamete1)
offspring3 = combine_alleles(parent1gamete1, parent2gamete2)
offspring4 = combine_alleles(parent1gamete2, parent2gamete2)

print()
print("   ", parent1gamete1, "   ", parent1gamete2)
print("  -----------")
print(parent2gamete1, "|", offspring1, "|", offspring2, "|")
print("  -----" + "|" + "-----")
print(parent2gamete2, "|", offspring3, "|", offspring4, "|")
print("  -----------")


# Calculating genotypic ratio
offspring_arr = [offspring1, offspring2, offspring3, offspring4]
homozygous_dom = 0
heterozygous = 0
homozygous_rec = 0

for genotype in offspring_arr:
  if genotype[0].isupper() and genotype[1].isupper():
    homozygous_dom += 1
  elif genotype[0].isupper() and genotype[1].islower():
    heterozygous += 1
  elif genotype[0].islower() and genotype[1].islower():
    homozygous_rec += 1

if 4 in [homozygous_dom, heterozygous, homozygous_rec]:
    ratio = "1"
elif homozygous_dom == heterozygous or heterozygous == homozygous_rec:
  ratio = "1 : 1"
else:
  ratio = "1 : 2 : 1"

print(f"genotypic ratio: {ratio}")


# Calculating phenotypic ratio
dominant_traits = 0
recessive_traits = 0

for genotype in offspring_arr:
  if genotype[0].isupper():
    dominant_traits += 1
  elif genotype[0].islower():
    recessive_traits += 1

if 4 in [dominant_traits, recessive_traits]:
  ratio = "1"
elif dominant_traits == recessive_traits:
  ratio = "1 : 1"
else:
  ratio = "3 : 1"

print(f"phenotypic ratio: {ratio}")