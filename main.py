from sys import stdin
from sapifalic import bible2ilrdf


def main():
    for tsua in stdin.readlines():
        print(bible2ilrdf(tsua.strip()))


if __name__ == '__main__':
    main()
