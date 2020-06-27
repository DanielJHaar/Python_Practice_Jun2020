def split_and_join(line):
    words = line.split()
    hyphen = "-"
    line = hyphen.join(words)
    return line


if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)