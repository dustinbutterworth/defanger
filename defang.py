#!/usr/bin/env python3
import os
import argparse
from pathlib import Path


def defang_url(url: str) -> str:
    url = url.split(".")
    separator = "[.]"
    url = separator.join(url)
    url = url.replace("http", "hxxp")
    url = url.replace("@", "[AT]")
    return url


def defang_file(filename: Path):
    with open(filename, 'r') as infile:
        outfile_path = os.path.dirname(os.path.abspath(filename))
        with open(
            f'{outfile_path}/{filename.stem}_defanged{filename.suffix}', "w") as outfile:
                for line in infile:
                    str = defang_url(line)
                    outfile.write(str)
    print(f'Created new defanged version of {infile.name} at {outfile.name}')


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--file',
                        type=Path,
                        help="Provide the path to a file to defang."
                        )
    parser.add_argument('--url',
                        type=str,
                        help="Provide a url to defang."
                        )
    args = parser.parse_args()

    if args.url:
        print(defang_url(args.url))
    elif args.file:
        defang_file(args.file)
    else:
        parser.error('Please provide --url or --file. Run defang.py --help'
                     ' for more information')


if __name__ == "__main__":
    main()
