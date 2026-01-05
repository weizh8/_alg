def riemann_n_dim(func, bounds, steps, current_dim=0, point=None):
    """
    func: The function to integrate, accepts a list/tuple of length n.
    bounds: List of tuples [(min1, max1), (min2, max2), ...]
    steps: Number of divisions per dimension.
    """
    n = len(bounds)
    if point is None:
        point = [0.0] * n
    
    if current_dim == n:
        return func(point)

    total_sum = 0
    low, high = bounds[current_dim]
    dx = (high - low) / steps
    
    for i in range(steps):
        # Using the midpoint for better accuracy
        point[current_dim] = low + (i + 0.5) * dx
        total_sum += riemann_n_dim(func, bounds, steps, current_dim + 1, point)
    
    return total_sum * dx
