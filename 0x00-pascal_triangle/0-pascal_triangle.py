from functools import reduce

def pascal_triangle(n):
    if n <= 0:
        return []

    def next_row(prev):
        return [1] + [prev[i - 1] + prev[i] for i in range(1, len(prev))] + [1]
    
    return reduce(lambda acc, _: acc + [next_row(acc[-1])], range(n - 1), [[1]])

# Usage example:
# print(pascal_triangle(5))
