import matplotlib.pyplot as plt

def main():
    plt.plot([1, 2, 3, 4], label="a line")
    plt.ylabel("some numbers")
    plt.legend()
    plt.show()

if __name__ == "__main__":
    main()
