# CTK: Cherokee Toolkit
#
# Authors:
#      Taher Shihadeh
#      Alvaro Lopez Ortega
#
# Copyright (C) 2010 Alvaro Lopez Ortega
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of version 2 of the GNU General Public
# License as published by the Free Software Foundation.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA
# 02110-1301, USA.
#

from Widget import Widget
from Box import Box
from RawHTML import RawHTML
from Container import Container
from Server import cfg
from util import *


HTML = """
<input type="radio" id="%(id)s" %(props)s />
"""

class Radio (Widget):
    def __init__ (self, props={}):
        # Sanity check
        assert type(props) == dict

        Widget.__init__ (self)
        self._props = props.copy()

    def Render (self):
        # Deal with a couple of exceptions
        new_props = self._props.copy()

        if new_props.has_key('checked') and int(new_props.pop('checked')):
            new_props['checked'] = "checked"

        if new_props.has_key('disabled') and int(new_props.pop('disabled')):
            new_props['disabled'] = "disabled"

        # Render the widget
        render = Widget.Render (self)
        render.html += HTML %({'id':    self.id,
                               'props': props_to_str (new_props)})
        return render


class RadioText (Box):
    def __init__ (self, txt, props={}):
        Box.__init__ (self)

        self.radio = Radio (props.copy())
        self += self.radio

        self.text = Box ({'class': 'radio-text'}, RawHTML(txt))
        self += self.text

        self.text.bind('click', "$('#%s').attr('checked', true);" %(self.radio.id))
