def main():
    print("Let's implement division, Type two numbers for x and y")

    x = int(input("x > "))
    y = int(input("y > "))
    print("%d / %d = %.3f" % (x, y, divide(x, y)))

def add(a, b):
    return a + b
def divide(a, b):
    if b == 0:
        print("Error: cannot divide by zero.")
    else:
        return a/b

if __name__ == "__main__":
    main()