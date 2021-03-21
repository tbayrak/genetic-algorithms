import numpy
import pygad
import matplotlib.pyplot
import numpy
from PIL import Image 
import imageio

def chromosome_to_image(chromosome, img_shape):
    return numpy.reshape(chromosome, img_shape)


def image_to_chromosome(image):
    img_shape = image.shape
    return numpy.reshape(image, img_shape[0] * img_shape[1] * img_shape[2])


def calculate_fitness(solution):
    fitness = numpy.sum(numpy.abs(target_chromosome - solution))
    fitness = numpy.sum(target_chromosome) - fitness
    return fitness

# jpg uzantili herhangi bir dosya verilebilir
original_img = imageio.imread('tea.jpg')
original_img = numpy.asarray(original_img/255, dtype=numpy.float)
target_chromosome = image_to_chromosome(original_img)

# caprazlama & mutasyon buyuklukleri ve yapilma ihtimalleri parametrelerle ayarlanabilir
ga_model = pygad.GA(num_generations=100, num_parents_mating=10, fitness_func=calculate_fitness, sol_per_pop=20, num_genes=original_img.size, init_range_low=0.0, init_range_high=1.0, mutation_percent_genes=0.01, random_mutation_min_val=0.0, random_mutation_max_val=1.0)

ga_model.run()
ga_model.plot_result()
result, result_fitness, _ = ga_model.best_solution()

print("En iyi uygunlık değeri :" + str(result_fitness))
print("En iyi değer indisi: " + str(ga_model.best_solution_generation))

generated_image = chromosome_to_image(result, original_img.shape)
matplotlib.pyplot.imshow(generated_image)
matplotlib.pyplot.show()
