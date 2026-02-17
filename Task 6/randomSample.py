import random
import statistics

data = [100, 200, 300, 400, 500]

sample = random.sample(data, 3)

print("Sample:", sample)
print("Mean:", statistics.mean(sample))
print("Standard Deviation:", statistics.stdev(sample))
