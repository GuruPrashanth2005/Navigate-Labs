import statistics

runs = [0.85, 0.87, 0.83, 0.88]

print("Average Accuracy:", statistics.mean(runs))
print("Variance:", statistics.variance(runs))
