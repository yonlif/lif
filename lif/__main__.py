import argparse
from typing import List

from cython_api import trial_division


parser = argparse.ArgumentParser(description='Large Integer Factorization')
parser.add_argument('integer', type=int, help='An integer to factorize')
parser.add_argument('-a', '--algo', type=str, default='trail_division', choices=['trail_division'],
                    help='Algorithm to perform factorization')


def main():
    args = parser.parse_args()
    algorithm = args.algo
    number = args.integer
    res: List[str] = []
    if algorithm == "trail_division":
        res = trial_division(number)
    else:
        print(f"No such algorithm {algorithm}")
        exit(1)
    print(', '.join(map(str, res)))
    exit(0)


if __name__ == '__main__':
    main()
