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
# along with Belluaire. If not, see <http://www.gnu.org/licenses/>.

#----------------------+
# Initialisation       |
#- - - - - - - - - - - +
import ConfigParser,os
#======================+
# Fonctions internes   |
#----------------------+

#======================+
# Classes              |
#----------------------+
class Preferences(object):
    def __init__(self,filepref='./Ressources/prefs.cfg'):
        assert(os.path.exists(filepref))
        self.filepref=filepref
        self.config=ConfigParser.RawConfigParser()
        self.config.read(filepref)
        self.load()
   
    def load(self):
        self.lang=self.config.get('global','lang')
        self.language={}
        for item in self.config.items(self.lang):
            self.language.update(eval(item[1]))


