# Legacy code – intentionally verbose and repetitive
def process(items):
    result = []
    for i in range(len(items)):
        val = items[i]
        squared = val * val
        if squared % 2 == 0:
            result.append(squared)
    return result

if __name__ == "__main__":
    data = list(range(10))
    print(process(data))
