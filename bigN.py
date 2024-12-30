import numpy as np

# Generate a large population
population_size = 1000000
population = np.random.normal(loc=50, scale=10, size=population_size)
# print("population", population, len(population), type(population))

# Define sample size and number of samples
sample_size = 1000
num_samples = 1000

# Take samples and calculate their means
sample_means = [
    np.mean(np.random.choice(population, sample_size)) for _ in range(num_samples)
]
# print(len(np.unique(sample_means)), num_samples)

# Calculate the mean of the sample means
mean_of_sample_means = np.mean(sample_means)

# Calculate the mean of the population
population_mean = np.mean(population)

print(f"Mean of the population: {population_mean}")
print(f"Mean of the sample means: {mean_of_sample_means}")

# Calculate and print the difference between the population mean and the mean of the sample means
difference = population_mean - mean_of_sample_means
print(f"Difference: {difference}")
