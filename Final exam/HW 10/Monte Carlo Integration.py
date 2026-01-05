import random

def monte_carlo_n_dim(func, bounds, iterations=100000):
    n = len(bounds)
    total_val = 0
    
    # Calculate the n-dimensional volume (hypervolume)
    volume = 1.0
    for low, high in bounds:
        volume *= (high - low)
    
    for _ in range(iterations):
        # Generate a random point within the bounds
        point = [random.uniform(low, high) for low, high in bounds]
        total_val += func(point)
        
    average_height = total_val / iterations
    return volume * average_height
