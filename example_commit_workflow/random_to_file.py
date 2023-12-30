import argparse
import random
import datetime

def main():
    args = parse_args()
    output_path = args.output_path
    random_number = random.randint(1, 100)
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(output_path, "a") as f:
        f.write(f"{random_number} {timestamp}")
    print(f"Random number generated and saved to file: {output_path}")

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output-path", type=str, default="random_number.txt")
    return parser.parse_args()

if __name__ == "__main__":
    main()