import argparse

from cython_api import trial_division, pollards_rho


algorithms_list = ['trial_division', 'pollards_rho']


parser = argparse.ArgumentParser(description='Large Integer Factorization')
parser.add_argument('integer', type=int, help='An integer to factorize')
parser.add_argument('-a', '--algo', type=str, default='trial_division', choices=algorithms_list,
                    help='Algorithm to perform factorization')


def main():
    args = parser.parse_args()
    algorithm = args.algo
    number = args.integer
    if algorithm == "trail_division":
        res = trial_division(number)
        print(', '.join(map(str, res)))
    elif algorithm == "pollards_rho":
        res = pollards_rho(number)
        print(res)
    else:
        print(f"No such algorithm {algorithm}")
        exit(1)
    exit(0)


if __name__ == '__main__':
    main()
