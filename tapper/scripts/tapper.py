#!/usr/local/bin/ python3
# -*- coding: utf-8 -*-

import os, sys
import optparse

def main(argv=sys.argv):
    command = TapperCommand(argv)
    command.run()

class TapperCommand(object):
    pass
