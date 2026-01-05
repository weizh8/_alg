## Comparison and Implementation

This section evaluates the performance and theoretical trade-offs between the **Recursive N-Dimensional Riemannian** method and the **Monte Carlo** integration method.

### 1. Methodology Comparison

| Feature | Riemannian Integration | Monte Carlo Integration |
| :--- | :--- | :--- |
| **Approach** | Deterministic (Regular Grid) | Probabilistic (Random Sampling) |
| **Complexity** | Exponential $O(S^n)$ | Independent of $n$ (Fixed Iterations) |
| **Accuracy** | Very high for low dimensions | Improves with samples $1/\sqrt{N}$ |
| **Use Case** | Low-dimensional spaces ($n \le 4$) | High-dimensional spaces ($n > 4$) |

---

### 2. Implementation & Testing

To verify the algorithms, we use a standard test function $f(x_1, x_2, ..., x_n) = \sum x_i$ with integration bounds $[0, 1]$ for all dimensions. For $n=3$, the analytical solution is **1.5**.

#### Python Test Script:
```python
def test_function(args):
    """Simple test function: f(x, y, z) = x + y + z"""
    return sum(args)

# Problem Definition: 3 Dimensions, all bounds [0, 1]
bounds = [(0, 1)] * 3

# 1. Riemannian Execution
# With 20 steps per dimension, total = 20^3 = 8,000 evaluations
res_riemann = riemann_n_dim(test_function, bounds, steps=20)

# 2. Monte Carlo Execution
# Using 100,000 random samples
res_mc = monte_carlo_n_dim(test_function, bounds, iterations=100000)

print(f"Analytical Result: 1.5")
print(f"Riemann Result:    {res_riemann:.5f}")
print(f"Monte Carlo Result: {res_mc:.5f}")
