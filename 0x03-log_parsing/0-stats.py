#!/usr/bin/python3
'''\
The script reads <stdin> line by line and computes metrics

input format: <IP Address> - [<date>] "GET /projects/260 HTTP/1.1" \
<status code> <file size>
    > lines formatted differently will be skipped

After every 10 lines and/or a keyboard interruption (CTRL + C),
these statistics are printed:
    > Total file size: "File size: <total size>"
        where <total size> is the sum of all previous <file size>
    > For each status code appeared a line is printed containing the number \
of lines with that status code: "<status code>: <number of lines>"
        > possible status code: 200, 301, 400, 401, 403, 404, 405 and 500
        > if a status code doesn’t appear or is not an integer, no \
corresponding line is printed
        > status codes will be printed in ascending order
'''
import re
from sys import stdin, stdout


def print_stats(sc_count, file_size):
    '''Print the stats according to the predifined output format'''
    buffer = f"File size: {file_size}\n"
    for key in sorted(sc_count.keys()):
        buffer += f"{key}: {sc_count[key]}\n"

    print(buffer, end='')
    # stdout.write(buffer)
    # stdout.flush()


def main():
    '''main: entry point'''
    pattern = r".+ - \[.+\] \"GET /projects/260 HTTP/1.1\" (.+) (.+)\s"
    line_fmt = re.compile(pattern)

    sc_fmt = re.compile(r"[0-9]+")

    file_size = 0
    sc_count = {}

    try:
        count = 0

        for line in stdin:
            count += 1

            matched = line_fmt.fullmatch(line)
            if not matched:
                continue
            sc, fs = matched.group(1, 2)
            file_size += int(fs)

            if sc_fmt.fullmatch(sc):
                sc = int(sc)
                sc_count[sc] = sc_count.get(sc, 0) + 1

            if count % 10 == 0:
                print_stats(sc_count, file_size)

    except KeyboardInterrupt as e:
        print_stats(sc_count, file_size)
        raise e


if __name__ == "__main__":
    main()
