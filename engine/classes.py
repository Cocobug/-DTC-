# -*- coding:utf8 -*-

###########################################
# Copyright 2011: Cocobug                 #
###########################################
# This file is part of dtc-engine.
#
# dtc-engine is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# dtc-engine is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with dtc-engine. If not, see <http://www.gnu.org/licenses/>.

#----------------------+
# Initialisation       |
#- - - - - - - - - - - +
import ConfigParser,os
import markdown

from jinja2 import Environment, FileSystemLoader
env = Environment(loader=FileSystemLoader('templates'))

#======================+
# Fonctions internes   |
#----------------------+



def reading(link):
    link=open(link)
    return link.read()

def markdown(link):
    link=reading(link)
    return markdown.markdown(link)

def liquid(model,kwargs):
    tmpl = env.get_template(model)
    return tmpl.render(**kwargs)

def parser(config):
    fob=open(config)
    res={}
    for line in fob.readline():
        name,val=line.split('=',1)
        name.strip()
        val.strip()
        res[name]=val
    return res
    
def Parser(config):
    parser=ConfigParser.RawConfigParser()
    parse.read(config)
    return parser.load()

