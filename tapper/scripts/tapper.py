#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
Copyright (c) 2015-2016, Contributor
All rights reserved.

author: Takegami

'''

import os, sys
import shutil, glob, html

from pkg_resources import (resource_filename, get_distribution)
from HTMLParser import HTMLParser
from argparse import ArgumentParser
from jinja2 import Template

DIR_HTML = './html'
DIR_CSS  = './html/css'
DIR_JS   = './html/js'
DIR_IMG  = './html/img'
DIR_PRE  = './html/img/preloads'

PROG = 'tapper'

def main(argv=sys.argv):
    command = TapperCommand(argv)
    command.run()

def _get_resource(kind, name):
    filename = os.path.join('scaffolds', kind, name)
    return resource_filename('tapper', filename)

def _render(i_file, o_file, **kwarg):
    with open(i_file, 'r') as i_fp, open(o_file, 'wb') as o_fp:
        tmpl = Template(i_fp.read())
        o_fp.write(tmpl.render(**kwarg))

    print '    create: %s'% o_file

def _copy(i_file, o_dir):
    shutil.copy(i_file, o_dir)
    print '    create: %s'% os.path.join(DIR_CSS, i_file.split('/')[-1])


class TapperCommand(object):
    parser = ArgumentParser(prog=PROG)
    parser.add_argument('-v',
        action='version',
        version='%s %s'%(PROG, get_distribution(PROG).version))

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

        except Exception as e:
            print '  Failed.'
            print str(e)


    def update(self):

        # find file_path
        def find_path(name):
            for path in os.walk('./'):
                for i in path:
                    if name in i:
                        return os.path.join(path[0], name)
            raise IOError("File is not exists. '%s'"% name)

        print 'Tapper update.'
        try:
            tapper_path  = find_path('tapper.js')
            preload_path = find_path('preloads')

            src_list = []
            res_list = glob.glob(os.path.join(preload_path, '*'))
            for res in res_list:
                f_name = res.split('/')[-1]
                print '    load: %s'% f_name
                src_list.append(os.path.join('img/preloads', f_name))

            _render(_get_resource('js', 'tapper.tmpl'),
                    tapper_path,
                    src_list=src_list)
            print '  Succeeded.'

        except Exception as e:
            print '  Failed.'
            print str(e)


if __name__ == "__main__":
    main()
