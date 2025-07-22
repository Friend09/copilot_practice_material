def compute(numbers: list[int]) -> list[int]:
    result = []
    for i in numbers:
        if i % 2 == 0:
            squared = i * i
            result.append(squared)
    return result

if __name__ == "__main__":
    print(compute(list(range(20))))
