if __name__ == "__main__":
    result = 600851475143
    i = 2

    while i * i < result:
        while result % i == 0:
            result = result / i
        i = i + 1

    print(result)
