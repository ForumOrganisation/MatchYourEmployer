#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Copyright © 2017 Thomas Lacroix <toto.rigolo@free.fr>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

"""
    Simple logger.
"""

import datetime
import sys
from termcolor import cprint


def log(status, message):
    if not (hasattr(sys.stdout, 'isatty') and sys.stdout.isatty()):
        print('[%s] %s: %s' %
              (datetime.datetime.now().isoformat(), status, message))
        return

    cprint('[%s] ' % datetime.datetime.now().isoformat(),
           'yellow', attrs=['bold'], end='')
    if status == 'info':
        cprint('Info: ', 'yellow', attrs=['bold'], end='')
        cprint(message, 'blue')
    elif status == 'success':
        cprint('Success: ', 'yellow', attrs=['bold'], end='')
        cprint(message, 'green')
    elif status == 'warning':
        cprint('Warning: ', 'yellow', attrs=['bold'], end='')
        cprint(message, 'red')
    elif status == 'danger':
        cprint('Danger: ', 'yellow', attrs=['bold'], end='')
        cprint(message, 'white', 'on_red')
    elif status == 'critical':
        cprint('Critical: ', 'yellow', attrs=['bold'], end='')
        cprint(message, 'red', attrs=['bold'])
