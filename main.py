import os
import sys

from data import load_dataset
import config

def main():
    dataset = load_dataset(show_info=True)

if __name__ == '__main__':
    print('Start of test')
    main()
    print('End of test')
