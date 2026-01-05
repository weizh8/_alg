# Optimization Algorithms Implementation

This repository contains the implementation of various optimization algorithms to find the minimum value of a function (Linear Regression context). These scripts demonstrate the conceptual differences between heuristic searches and gradient-based methods.

## Algorithms Included

1.  **Hill Climbing Algorithm**: A local search algorithm that continuously moves in the direction of increasing value/decreasing cost to find the peak or valley.
2.  **Greedy Method**: A strategy that makes the locally optimal choice at each stage with the hope of finding a global optimum.
3.  **Gradient Descent**: An iterative optimization algorithm for finding the local minimum of a differentiable function using derivatives.
4.  **Improved Method**: An enhanced version of Gradient Descent, implementing **Momentum** to accelerate gradients in the right direction and dampen oscillations.

## My Understanding

* **Hill Climbing**: I view this as a "trial and error" approach in the immediate neighborhood. It is simple but can easily get stuck in "local optima" (a small dip that isn't the lowest point of the whole graph).
* **Greedy Method**: This method is about immediate gain. In optimization, it means taking the step that reduces the error the most right now, without looking ahead at the global landscape.
* **Gradient Descent**: This is more mathematically "aware" than Hill Climbing. By calculating the slope (gradient), the algorithm knows exactly which direction leads downwards, making it much more efficient for complex functions like Linear Regression.
* **Improvement Method (Momentum)**: Standard Gradient Descent can be slow or zigzag. By adding momentum, the algorithm gains "inertia" from previous steps, helping it pass through small flat areas and reach the global minimum faster.

AI Conversation Reference AI Tool Used: Google Gemini
Conversation URL: [Gemini](https://gemini.google.com/share/8bdcbc9842bb)
