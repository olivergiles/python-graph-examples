import matplotlib.pyplot as plt

def main():
    plt.plot([1, 2, 3, 4])
    plt.xticks([1, 4], ["start", "end"])
    plt.yticks([0, 5])
    plt.savefig("line.png")
    plt.show()

if __name__ == "__main__":
    main()
