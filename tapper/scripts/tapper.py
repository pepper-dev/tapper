#!/usr/bin/python
# -*- coding: utf-8 -*-

import os, sys
from argparse import ArgumentParser

def main(argv=sys.argv):
    command = TapperCommand(argv)
    command.run()

class TapperCommand(object):
    parser = ArgumentParser(prog='tapper')
    subparsers = parser.add_subparsers(help='sub-command help')

    # create sub-command
    parser_create = subparsers.add_parser('create',
        help='create scaffolds.')
    parser_create.add_argument('--scene',
        type=int,
        help='scene num')

    # clean sub-command
    parser_clean = subparsers.add_parser('clean',
        help='clean scaffolds.')

    def __init__(self, argv):
        self.args = self.parser.parse_args(argv[1:])
        self.name = argv[1]

    def run(self):
        try:
            getattr(self, self.name)()
        except AttributeError:
            raise RuntimeError('Undefined sub-command.')

    def create(self):
        print ''' TODO create sub-command.'''

    def clean(self):
        print ''' TODO clean sub-command.'''



if __name__ == "__main__":
    main()
