#Number Compression Counter
def compressed_length(n: int) -> int:
    count = 0
    while n > 0 and n % 2 == 0:
        count += 1
        n //= 2
    return count