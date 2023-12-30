import argparse
import random

def main():
    args = parse_args()
    output_path = args.output_path
    random_number = random.randint(1, 100)
    with open(output_path, "w") as f:
        f.write(str(random_number))
    print(f"Random number generated and saved to file: {output_path}")

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output-path", type=str, default="random_number.txt")
    return parser.parse_args()

if __name__ == "__main__":
    main()