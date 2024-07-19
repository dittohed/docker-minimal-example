import argparse
import numpy as np

from sklearn.model_selection import train_test_split


def main(length: int, low: int, high: int, seed: int):
    np.random.seed(seed)

    data = np.random.randint(low, high, length)
    train, test = train_test_split(data, test_size=0.2, random_state=seed)

    print('Train:', train)
    print('Test:', test)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Generate and split a list of random integers.',
        add_help=False
    )
    parser.add_argument(
        '-h', '--help', action='help', default=argparse.SUPPRESS,
        help='Show this help message and exit.'
    )
    parser.add_argument(
        '--length', type=int, required=True, 
        help='Length of the list.'
    )
    parser.add_argument(
        '--low', type=int, required=True, 
        help='Lowest possible integer.'
    )
    parser.add_argument(
        '--high', type=int, required=True, 
        help='Highest possible integer.'
    )
    parser.add_argument(
        '--seed', type=int, required=True, 
        help='Random seed for reproducibility.'
    )
    
    args = parser.parse_args()
    main(args.length, args.low, args.high, args.seed)
