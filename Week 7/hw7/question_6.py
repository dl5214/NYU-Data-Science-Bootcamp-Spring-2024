from scipy.stats import t

# Given data for two groups
mean_A = 75
std_A = 8
size_A = 25
mean_B = 78
std_B = 7
size_B = 30

# Compute Welch's t-statistic
t_stat = (mean_A - mean_B) / (((std_A**2 / size_A) + (std_B**2 / size_B))**0.5)

# Compute degrees of freedom for Welch's test
df = (((std_A**2 / size_A) + (std_B**2 / size_B))**2) / \
     ((std_A**4 / (size_A**2 * (size_A - 1))) + (std_B**4 / (size_B**2 * (size_B - 1))))

# Calculate the two-tailed p-value
p_value = 2 * (1 - t.cdf(abs(t_stat), df=df))

print("T-statistic:", t_stat)
print("P-value:", p_value)
print("Degrees of Freedom:", df)
