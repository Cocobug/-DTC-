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
from bottle import Bottle, run, static_file, route, abort, redirect
from bottle import jinja2_view as view, jinja2_template as template
#======================+
# Fonctions internes   |
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

@app.error(404)
def error404(error):
    return 'Nothing here, sorry'

app.debug=True
run(app, reloader=True, host='localhost', port=8080)

