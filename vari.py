data = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
frequency = {x: data.count(x) for x in set(data)}
cumulative_frequency = {}
cumulative_sum = 0
for key in sorted(frequency.keys()):
 cumulative_sum += frequency[key]
 cumulative_frequency[key] = cumulative_sum
print(f"Frequency: {frequency}")
print(f"Cumulative Frequency: {cumulative_frequency}")
count = len(data)
proportion = {k: v / count for k, v in frequency.items()}
rate = {k: (v / count) * 100 for k, v in frequency.items()}
print(f"Count: {count}")
print(f"Proportion: {proportion}")
print(f"Rate: {rate}")

import statistics
mean = statistics.mean(data)
median = statistics.median(data)
mode = statistics.mode(data)
print(f"Mean: {mean}, Median: {median}, Mode: {mode}")

range_val = max(data) - min(data)
variance = statistics.variance(data)
std_deviation = statistics.stdev(data)
print(f"Range: {range_val}, Variance: {variance}, Standard Deviation: {std_deviation}")

z_scores = [(x - mean) / std_deviation for x in data]
print(f"Z-Scores: {z_scores}")