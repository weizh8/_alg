import random

def f(x): return x**2

def hill_climbing(start_x, step_size=0.1, iter=100):
    current_x = start_x
    for _ in range(iter):
        
        next_x_left = current_x - step_size
        next_x_right = current_x + step_size
        
        
        best_x = min([current_x, next_x_left, next_x_right], key=f)
        
        if best_x == current_x:
            break
        current_x = best_x
    return current_x

print(f"Hill Climbing Result: {hill_climbing(10)}")
