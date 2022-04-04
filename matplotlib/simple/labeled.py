import matplotlib.pyplot as plt

def main():
    plt.plot([1, 2, 3, 4])
    plt.ylabel("some numbers")
    plt.xlabel("numbers in order")
    plt.title("Random graph")
    plt.savefig("line.png")
    plt.show()

if __name__ == "__main__":
    main()
