def number_sum(n: int) -> int:
    if n < 1:
        return 0
    num_sum = 0
    for x in range(n+1):
        num_sum += x

    return num_sum