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
# Importation          |
#- - - - - - - - - - - +

import os,sys
import markdown
from bottle import Bottle, run, static_file, route, abort, redirect
from bottle import jinja2_view as view, jinja2_template as template

#----------------------+
# Initialisation       |
#- - - - - - - - - - - +
exists=os.path.exists

PATH_PAGES='pages/'
PATH_IMAGES='images/'
PATH_STATIC='static/'

PATH_NEWS=PATH_PAGES+'news/'
PATH_GLOBAL=PATH_PAGES+'global/'

templates={'global':PATH_GLOBAL+'global.liquid','news':PATH_GLOBAL+'news.liquid'}
css={'global':PATH_GLOBAL+'global.css','news':PATH_GLOBAL+'news.css'}

#======================+
# Fonctions internes   |
#----------------------+

def model(category):
	if category in templates and exists(templates[category]):
		templates[category]
	return templates['global']

def article(filepath):
	temp=filepath+'.md'
	if exists(temp): return temp
	abort(404, temp+'\nThou are weak')

def css(category):
	if category in css and exists(css[category]):
		return css[category]
	return css['global']

#======================+
# Programme principal  |
#----------------------+

app = Bottle()

@app.route('/')
@app.route('/hello')
def hello():
	return "Hello World!"

@app.route(PATH_IMAGES+'<filename:re:.*\.png>#')
def send_image(filename):
	return static_file(filename, root='/path/to/image/files', mimetype='image/png')

@app.route(PATH_STATIC+'<filename:path>')
def send_static(filename):
	return static_file(filename, root='/path/to/static/files')

@app.route('/news/<dd>/<mm>/<aa>/<name>')
def news(dd,mm,aa,name):
	pagename=name
	date=dd+mm+aa
	path=PATH_NEWS+date+'-'+name	
	with open(article(path)) as text: html=markdown.markdown(text.read())
	print html
	return template(model('news'),title=pagename,content=html)

app.debug=True
run(app, reloader=True, host='localhost', port=8080)

