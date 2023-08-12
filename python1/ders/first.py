import cmath

def solve_quadratic(a, b, c):
    # Discriminant
    d = (b**2) - (4 * a * c)
    sqrt_d = cmath.sqrt(d)
    # first solution
    sol1 = (-b + sqrt_d) / (2 * a)
    # second solution
    sol2 = (-b - sqrt_d) / (2 * a)

    return sol1, sol2

# usage
print(solve_quadratic(1, -5, 6))
