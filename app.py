from flask import Flask, request, jsonify

app = Flask(__name__)


def mono_punnett(parent1, parent2):
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

  return offspring1, offspring2, offspring3, offspring4


def genotypic_ratio(offspring1, offspring2, offspring3, offspring4):
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
    geno_ratio = "1"
  elif homozygous_dom == heterozygous or heterozygous == homozygous_rec:
    geno_ratio = "1 : 1"
  else:
   geno_ratio = "1 : 2 : 1"

  return geno_ratio


def phenotypic_ratio(offspring1, offspring2, offspring3, offspring4):
  offspring_arr = [offspring1, offspring2, offspring3, offspring4]

  dominant_traits = 0
  recessive_traits = 0

  for genotype in offspring_arr:
    if genotype[0].isupper():
      dominant_traits += 1
    elif genotype[0].islower():
      recessive_traits += 1

  if 4 in [dominant_traits, recessive_traits]:
    pheno_ratio = "1"
  elif dominant_traits == recessive_traits:
    pheno_ratio = "1 : 1"
  else:
    pheno_ratio = "3 : 1"
  
  return pheno_ratio

@app.route('/', methods=['POST'])
def calculate_punnett():
    data = request.get_json()
    if not data or 'parent1' not in data or 'parent2' not in data:
        return jsonify({'error': 'Please provide both parent1 and parent2 genotypes'}), 400
    parent1 = data['parent1']
    parent2 = data['parent2']
    
    # Calculate the Punnett square
    offspring1, offspring2, offspring3, offspring4 = mono_punnett(parent1, parent2)
    
    # Calculate ratios
    geno_ratio = genotypic_ratio(offspring1, offspring2, offspring3, offspring4)
    pheno_ratio = phenotypic_ratio(offspring1, offspring2, offspring3, offspring4)
    
    # Create a JSON response with all requested data
    response = {
        'offspring1': offspring1,
        'offspring2': offspring2,
        'offspring3': offspring3,
        'offspring4': offspring4,
        'geno_ratio': geno_ratio,
        'pheno_ratio': pheno_ratio
    }
    
    return jsonify(response)


if __name__ == '__main__':
    app.run(debug=True)