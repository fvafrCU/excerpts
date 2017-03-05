#!/usr/bin/env python3
"""
 @file
 command line interface
"""


import excerpts
import argparse
import textwrap


def make_parser():
    """
    Use a Custom Parser Function

    To keep main() tiny.
    """
    parser = argparse.ArgumentParser(description="convert markdown-style " +
                                     "comments from a file to markdown and " +
                                     "html via pandoc.",
                                     epilog=textwrap.dedent("""\
markdown style comments are headed by one or more comment characters giving
the markdown heading level and a magic character marking it as
markdown.
try --example for an example
            """))
    parser.add_argument("file_name", metavar="file",
                        help="The name of the file to convert comments from.")
    parser.add_argument("-O", "--output", dest="output_path",
                        default="",
                        help="Change the postfix added to the files created.")
    parser.add_argument("-o", "--postfix", dest="postfix",
                        default="",
                        help="Change the postfix added to the files created.")
    parser.add_argument("-e", "--prefix", dest="prefix",
                        default="",
                        help="Change the prefix added to the files created.")
    parser.add_argument("-c", "--comment", dest="comment_character",
                        default="#",
                        help="Change the comment character.")
    parser.add_argument("-m", "--magic", dest="magic_character",
                        default="%",
                        help="Change the magic character.")
    parser.add_argument("-v", "--version", action="version",
                        version="0.3.0")
    parser.add_argument("-x", "--example", action="version",
                        help="Give an example and exit.",
                        version=("""
##% *This* is an example markdown comment of heading level 2
#######% **This** is an example of a markdown paragraph: markdown recognizes
#######% only six levels of heading, so we use seven levels to mark
#######% "normal" text.
#######% Here you can use the full
#######% [markdown syntax](http://daringfireball.net/projects/markdown/syntax).
#######% *Note* the trailing line: markdown needs an empty line to end a
#######% paragraph.
#######%
"""))
    parser.add_argument("-p", "--pandoc", dest="run_pandoc",
                        help="Run pandoc on the md file created.",
                        action="store_true")
    parser.add_argument("-n", "--no-pandoc", dest="run_pandoc",
                        help="Do not run pandoc on the md file created.",
                        action="store_false")
    parser.add_argument("-l", "--latex", dest="compile_latex",
                        help="Run LaTex on the tex file created via pandoc.",
                        action="store_true")
    parser.add_argument("--no-latex", dest="compile_latex",
                        help="Run LaTex on the tex file created via pandoc.",
                        action="store_false")
    parser.add_argument("--formats", dest="pandoc_formats",
                        default="tex,html,pdf",
                        help="Comma seperated list of pandoc output " +
                        "formats. Only interpreted if --pandoc is given.")
    parser.add_argument("--no-pep8", dest="allow_pep8",
                        help="Allow for pep8 block comments.",
                        action="store_false")
    parser.set_defaults(run_pandoc=False, compile_latex=False, allow_pep8=True)
    return parser


def main():
    """
    A User Command Line Interface
    """
    args = make_parser().parse_args()
    status = excerpts.excerpts(file_name=args.file_name,
                               comment_character=args.comment_character,
                               magic_character=args.magic_character,
                               output_path=args.output_path,
                               allow_pep8=args.allow_pep8,
                               prefix=args.prefix,
                               postfix=args.postfix,
                               run_pandoc=args.run_pandoc,
                               compile_latex=args.compile_latex,
                               pandoc_formats=args.pandoc_formats)
    return status
