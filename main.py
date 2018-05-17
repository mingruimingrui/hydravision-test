import os
import sys


if __name__ == 'main':
    sys.path.insert(0, os.path.join(os.path.dirname(__file__name), '..'))

from .data import load_dataset
from . import config

main()


if __name__ == '__main__':
    print('Start of test')
    main()
    print('End of test')
