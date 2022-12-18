#!/usr/bin/env python3

import argparse
import sys
sys.path.append("../jupyter-translator/")
sys.path.append("../jupyter-to-html/")
from jupyter_translator import main as jt
from jupyter_to_html import main as jh


def parse_arguments():
    parser = argparse.ArgumentParser(description='Jupyter notebook translator')
    parser.add_argument('-f', '--file', help='The notebook to translate', required=True)
    parser.add_argument('-t', '--target', nargs='+', help='The target language, can be a list of languajes', required=True)
    
    return parser.parse_args()

def main(file, target):
    # Translate the notebook
    print("Translating notebook")
    paths = jt(args.file, args.target)

    # Convert the notebooks translated to html
    print("Converting notebooks to html")
    converted_paths = []
    for path in paths:
        print(f"\tConverting {path}")
        converted_notebook = jh(path)
        converted_paths.append(converted_notebook)
    
    return converted_paths



if __name__ == '__main__':
    args = parse_arguments()
    main(args.file, args.target)