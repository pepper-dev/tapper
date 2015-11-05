#!/usr/bin/python
# -*- coding: utf-8 -*-

import os, sys

import pkg_resources
import shutil
from argparse import ArgumentParser
from jinja2 import Template

def main(argv=sys.argv):
    command = TapperCommand(argv)
    command.run()

def _get_resource(kind, name):
    filename = os.path.join('scaffolds', kind, name)
    return pkg_resources.resource_filename('tapper', filename)

def _render(i_file, o_file, **kwarg):
    with open(i_file, 'r') as fp:
        tmpl = Template(fp.read())
        with open(o_file, 'wb') as fp:
            fp.write(tmpl.render(**kwarg))
    print '    create: %s'% o_file

def _copy(i_file, o_dir):
    shutil.copy(i_file, o_dir)
    print '    create: %s'% os.path.join(DIR_CSS, i_file.split('/')[-1])

DIR_HTML = './html'
DIR_CSS  = './html/css'
DIR_JS   = './html/js'
DIR_IMG  = './html/img'
DIR_PRE  = './html/img/preloads'

class TapperCommand(object):
    parser = ArgumentParser(prog='tapper')
    subparsers = parser.add_subparsers(help='sub-command help')

    # create sub-command
    parser_create = subparsers.add_parser('create',
        help='create scaffolds.')
    parser_create.add_argument('--scene',
        type=int,
        help='scene num')

    # update sub-command
    parser_update = subparsers.add_parser('update',
        help='update scaffplds.')

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
        print 'Tapper create.'
        try:
            for d in (DIR_HTML, DIR_CSS, DIR_JS, DIR_IMG, DIR_PRE):
                os.mkdir(d)
                print '    mkdir: %s'% d

            # index.html
            index_params   = { }
            _render(_get_resource('html',  'index.tmpl'),
                    os.path.join(DIR_HTML, 'index.html'),
                    **index_params )

            # *.css
            _copy(_get_resource('css', 'contents.css'), DIR_CSS)
            _copy(_get_resource('css', 'normalize.css'), DIR_CSS)

            # tapper.js
            tapper_params  = { }
            _render(_get_resource('js',  'tapper.tmpl'),
                    os.path.join(DIR_JS, 'tapper.js'),
                    **tapper_params )

            # contents.js
            content_params = { }
            _render(_get_resource('js',   'contents.tmpl'),
                    os.path.join(DIR_JS, 'contents.js'),
                    **content_params )

        except OSError:
            print "  Failed. Can not create scaffolds."

    def update(self):
        print ''' TODO update sub-command.'''

    def clean(self):
        print ''' TODO clean sub-command.'''



if __name__ == "__main__":
    main()
