from scipy.stats import t

# Given data
sample_mean = 6.5
population_mean = 6
sample_std = 1.2
sample_size = 50

# Calculate the t-statistic for the one-sample t-test
t_stat = (sample_mean - population_mean) / (sample_std / (sample_size ** 0.5))

# Degrees of freedom
df = sample_size - 1

# Calculate the one-tailed p-value
p_value = 1 - t.cdf(t_stat, df=df)

print("T-statistic:", t_stat)
print("P-value:", p_value)
