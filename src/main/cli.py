
"""This module provides the CopiPy CLI."""

import argparse
import pathlib
import sys

from . import __version__
from .tree import DirectoryTree


def main():
    args = parse_cmd_line_arguments()
    root_dir = pathlib.Path(args.root_dir)
    if not root_dir.is_dir():
        print("The specified root directory doesn't exist")
        sys.exit()
    tree = DirectoryTree(root_dir)
    tree.generate()


def parse_cmd_line_arguments():
    parser = argparse.ArgumentParser(
        prog="CopiPy",
        description="CopiPy, Add copyright to all files in a directroy",
        epilog="Thanks for using CopiPy - Developed by Sudoer-Zero",
    )
    parser.version = f"CopiPy v{__version__}"
    parser.add_argument("-v", "--version", action="version")
    parser.add_argument(
        "root_dir",
        metavar="ROOT_DIR",
        nargs="?",
        default=".",
        help="Generate a full directory tree starting at ROOT_DIR",
    )
    return parser.parse_args()

if __name__ == "__main__":
    main()
