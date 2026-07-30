from scipy.stats import norm
probability = norm.cdf(85, loc=70, scale=10)
print("Probability:", probability)
