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
from bottle import Bottle, run, static_file, route, abort, redirect
from bottle import jinja2_view as view, jinja2_template as template

#----------------------+
# Initialisation       |
#- - - - - - - - - - - +

templates={'global':'global/global.liquid','news':'news/news.liquid'}
css={'global':'global/global.css','news':'global/news.css'}

#======================+
# Fonctions internes   |
#----------------------+

def model(category):
	if category in templates and os.exists(templates[category]):
		templates[category]
	return templates['global']

def article(filepath):
	temp='pages/'+filepath+'.md'
	if os.exists(temp): return temp
	abort(404, 'Thou are weak')

def css(category):
	if category in css and os.exists(css[category]):
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

@app.route('/images/<filename:re:.*\.png>#')
def send_image(filename):
	return static_file(filename, root='/path/to/image/files', mimetype='image/png')

@app.route('/static/<filename:path>')
def send_static(filename):
	return static_file(filename, root='/path/to/static/files')

@app.route('/news/<category>/<int:date>/name')
def news(date,name):
	pagename=name
	header=''
	footer=''
	content='/news/'+category+'/'+date+'-'+name'
	with open ar('news') as article: text=article.read()
	template(model('news'),header=deader,footer=footer,content=text)

app.debug=True
run(app, reloader=True, host='localhost', port=8080)

