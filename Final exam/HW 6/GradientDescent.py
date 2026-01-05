def df(x): return 2*x

def gradient_descent(start_x, learning_rate=0.1, iter=100):
    current_x = start_x
    for _ in range(iter):
        gradient = df(current_x)
        
        current_x = current_x - (learning_rate * gradient)
    return current_x

print(f"Gradient Descent Result: {gradient_descent(10)}")
