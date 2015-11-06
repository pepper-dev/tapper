#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
Copyright (c) 2015-2016, Contributor
All rights reserved.

author: Takegami

'''

import os, sys
import pkg_resources, shutil, glob

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
        params = { 'scene': self.args.scene if self.args.scene else 1 }
        print '  Scene %d'% params['scene']
        try:
            for d in (DIR_HTML, DIR_CSS, DIR_JS, DIR_IMG, DIR_PRE):
                os.mkdir(d)
                print '    mkdir: %s'% d

            # index.html
            _render(_get_resource('html',  'index.tmpl'),
                    os.path.join(DIR_HTML, 'index.html'),
                    **params )

            # *.css
            _copy(_get_resource('css', 'contents.css'), DIR_CSS)
            _copy(_get_resource('css', 'normalize.css'), DIR_CSS)

            # tapper.js
            tapper_params  = { }
            _render(_get_resource('js',  'tapper.tmpl'),
                    os.path.join(DIR_JS, 'tapper.js'),
                    **params )

            # contents.js
            content_params = { }
            _render(_get_resource('js',   'contents.tmpl'),
                    os.path.join(DIR_JS, 'contents.js'),
                    **params )
            print '  Succeeded.'

        except OSError:
            print '  Failed. Can not create scaffolds.'
        except Exception as e:
            print '  Failed.'
            print str(e)

    def update(self):

        # find
        def find_path(name):
            for path in os.walk('./'):
                for i in path:
                    if name in i:
                        return os.path.join(path[0], name)

        print 'Tapper update.'
        preload_path = find_path('preloads')
        tapper_path  = find_path('tapper.js')

        src_list = []
        res_list = glob.glob(os.path.join(preload_path, '*'))
        for res in res_list:
            f_name = res.split('/')[-1]
            print '    Load: %s'% f_name
            src_list.append(os.path.join('preloads', f_name))

        _render(_get_resource('js', 'tapper.tmpl'),
                tapper_path,
                src_list=src_list )
        print '  Succeeded.'

    def clean(self):
        print ''' TODO clean sub-command.'''


if __name__ == "__main__":
    main()
