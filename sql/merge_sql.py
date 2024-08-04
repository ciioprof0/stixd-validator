#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Script to merge SQL files matching the pattern 'stixd_corpus_##.sql' into one consolidated file.
"""

import os
import glob
import sys

def merge_sql_files(output_filename: str = 'stixd_corpus.sql') -> None:
    """
    Merge all SQL files matching the pattern 'stixd_corpus_##.sql' into one file.

    Args:
        output_filename (str): The name of the consolidated output file. Defaults to 'stixd_corpus.sql'.
    """
    # Find all files matching the pattern 'stixd_corpus_##.sql'
    sql_files = glob.glob('stixd_corpus_*.sql')

    # Sort files by name to maintain a specific order
    sql_files.sort()

    with open(output_filename, 'w') as outfile:
        for i, sql_file in enumerate(sql_files):
            with open(sql_file, 'r') as infile:
                # Write the content of each SQL file to the output file
                outfile.write(infile.read())

                # Add two blank lines after each file's content, except for the last one
                if i < len(sql_files) - 1:
                    outfile.write('\n\n')

    print(f"Successfully merged {len(sql_files)} files into '{output_filename}'")

if __name__ == "__main__":
    # Accept the output filename as a CLI argument, defaulting to 'stixd_corpus.sql'
    output_filename = sys.argv[1] if len(sys.argv) > 1 else 'stixd_corpus.sql'
    merge_sql_files(output_filename)
