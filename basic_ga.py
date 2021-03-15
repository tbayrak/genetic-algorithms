import matplotlib.pyplot as plt 
import random


def form_chromosome(genes, value, fitness_value):
    return {"genes": genes, "value":value, "fitness_value":fitness_value}

  
def calculate_value(genes):
  return sum(genes)


def calculate_fitness_value(value):
  return abs(target_value - value)


def calculate_avg_fitness_value(population):

  total_fitness_value = 0
  for chromosome in population:
    total_fitness_value += chromosome["fitness_value"]

  avg_fitness_value = total_fitness_value / len(population)  

  return avg_fitness_value


def mutation(chromosome):
    new_genes = chromosome["genes"].copy()
    mutated_genes = random.sample(range(1, 100), 3)
    new_genes[:3] = mutated_genes
    new_value = calculate_value(new_genes)    
    new_fitness_value = calculate_fitness_value(new_value)

    new_chromosome = form_chromosome(new_genes, new_value, new_fitness_value)

    return new_chromosome


def cross_over(chrom_01, chrom_02):
    
    genes_01 = chrom_01["genes"].copy()
    genes_02 = chrom_02["genes"].copy()

    temp_genes = genes_01[:3]
    genes_01[:3] = genes_02[-3:]
    genes_02[-3:] = temp_genes    
    
    value_01 = calculate_value(genes_01)    
    fitness_value_01 = calculate_fitness_value(value_01)

    value_02 = calculate_value(genes_02)    
    fitness_value_02 = calculate_fitness_value(value_02)

    new_chromosome_01 = form_chromosome(genes_01, value_01, fitness_value_01)
    new_chromosome_02 = form_chromosome(genes_02, value_02, fitness_value_02)

    return new_chromosome_01, new_chromosome_02
    

number_of_iterations = 1000
target_value = 100
population_size = 30
population = []

# populasyonu olustur
for i in range(0, population_size):
  genes = random.sample(range(1, 100), 5)
  value = calculate_value(genes)
  fitness_value = calculate_fitness_value(value)

  chromosome = form_chromosome(genes, value, fitness_value)
  population.append(chromosome)

population = sorted(population, key=lambda k: k['fitness_value'], reverse=False)         

min_fitness_list = []
avg_fitness_list = []
max_fitness_list = []

for i in range(0, number_of_iterations):
    
    # rastgele caprazlama ve mutasyon indisleri olusturuldu
    cross_over_indexes = random.sample(range(0, population_size), 2)
    mutation_index = random.sample(range(0, population_size), 1)[0]
    
    new_chromosome_01, new_chromosome_02 = cross_over(population[cross_over_indexes[0]], population[cross_over_indexes[1]])
    new_chromosome_03 = mutation(population[mutation_index])
    
    population.append(new_chromosome_01)
    population.append(new_chromosome_02)
    population.append(new_chromosome_03)
    
    population = sorted(population, key=lambda k: k['fitness_value'], reverse=False)         
    
    # en zayif 3 tanesi elendi
    population = population[:population_size]

    min_fitness_value = population[0]["fitness_value"] 
    min_fitness_list.append(min_fitness_value)
    avg_fitness_list.append(calculate_avg_fitness_value(population))
    max_fitness_list.append(population[population_size - 1]["fitness_value"])

    if (min_fitness_value == 0):
        break


print(str(i+1) + ". min fitness : " + str(min_fitness_value))
print(population[0])
print("--")

plt.plot(min_fitness_list, label = "En Küçük")    
plt.plot(avg_fitness_list, label = "Ortalama")    
plt.plot(max_fitness_list, label="En Büyük")    
plt.xlabel("İterasyon Sayısı")
plt.ylabel("Uygunluk Değeri")
plt.title('Çaprazlama ve Mutasyon')

plt.legend()
plt.show()

