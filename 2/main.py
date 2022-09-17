if __name__ == "__main__":
    result = 0
    x = 1
    y = 2

    while x <= (4000 * 1000):
        if x % 2 == 0:
            result += x
        x, y = y, x + y

    print(result)
