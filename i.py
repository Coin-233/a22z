import re
import sys
import argparse

def w(word):
    if len(word) <= 3:
        return word
    else:
        return word[0] + str(len(word) - 2) + word[-1]

def s(input_str):
    words = re.findall(r'\b\w+\b', input_str)
    ws = [w(word) for word in words]
    return ' '.join(ws)

def ip(input_str):
    lines = input_str.split('\n')
    processed_lines = [s(line) for line in lines]
    return '\n'.join(processed_lines)

def i():
    while True:
        input_str = input("输入:")
        if input_str.lower() == 'exit':
            break
        result = ip(input_str)
        print("输出:", result)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-I", "--interactive", action="store_true", help="交互模式")
    parser.add_argument("-i", "--input", help="输入文件")
    parser.add_argument("-o", "--output", help="输出文件")
 
    args = parser.parse_args()

    if len(sys.argv) == 1:
        parser.print_help(sys.stderr)
        sys.exit(1)

    if args.interactive:
        i()
        sys.exit()

    if args.input:
        with open(args.input, 'r') as file:
            input_str = file.read()
    else:
        input_str = input("输入:")

    result = ip(input_str)

    if args.output:
        with open(args.output, 'w') as file:
            file.write(result)
    else:
        print("输出:")
        print(result)

if __name__ == "__main__":
    main()
