import random

def main():
    random_number = random.randint(1, 100)
    with open("random_number.txt", "w") as f:
        f.write(str(random_number))
    print("Random number generated and saved to file.")

if __name__ == "__main__":
    main()
