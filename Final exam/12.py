import numpy as np

def cross_entropy(p, q):
    # Adding a small epsilon to avoid log(0)
    return -np.sum(p * np.log2(q + 1e-12))

def verify_minimization():
    # Target distribution p
    p = np.array([1/2, 1/4, 1/4])
    
    # Initialize weights w randomly (these generate our q)
    w = np.array([0.1, 0.1, 0.1]) 
    
    learning_rate = 0.1
    epochs = 1000
    
    print(f"Target p: {p}")
    print(f"Initial Entropy H(p): {cross_entropy(p, p):.4f}\n")

    for i in range(epochs):
        # 1. Forward pass: Convert weights to probability q (Softmax)
        exps = np.exp(w)
        q = exps / np.sum(exps)
        
        # 2. Calculate Gradient
        # The gradient of Cross Entropy with respect to the weights w_i
        # simplifies beautifully to: grad = q - p
        grad = q - p
        
        # 3. Update weights
        w = w - learning_rate * grad
        
        if i % 200 == 0:
            current_loss = cross_entropy(p, q)
            print(f"Iteration {i}: q = {q}, Loss = {current_loss:.4f}")

    final_exps = np.exp(w)
    final_q = final_exps / np.sum(final_exps)
    print(f"\nFinal optimized q: {final_q}")
    print(f"Difference (q - p): {final_q - p}")

verify_minimization()
