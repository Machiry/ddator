#!/usr/bin/python
__author__ = 'machiry'
import sys


def print_usage():
    print(sys.arv[0] + " <property_file>")


def main():
    # 1. Check args
    if len(sys.argv) < 2:
        print_usage()
        return -1
    # 2. Parse property file

    # 3. Get various test profiles.

    # 4. Execute each test profile.


if __name__ == "__main__":
    sys.exit(main())
