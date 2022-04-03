import json
import numpy as np


# Save json
def save_json():
    np.random.seed(1)
    a = np.random.randint(0, 2000, 160)
    a = a.tolist()
    filename = './data/numbers.json'
    with open(filename, 'w') as file1:
        json.dump(a, file1)


# Load json
def load_json():
    filename = './data/numbers.json'
    with open(filename, 'r') as file1:
        a = json.load(file1)
        print(a)
        print(len(a))


if __name__ == '__main__':
    save_json()
    load_json()
