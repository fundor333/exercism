def distance(strand_a, strand_b):
    if len(strand_a) != len(strand_b):
        raise ValueError("Error string lenght")
    count = 0
    for i, p in zip(strand_a, strand_b):
        if i != p:
            count += 1
    return count