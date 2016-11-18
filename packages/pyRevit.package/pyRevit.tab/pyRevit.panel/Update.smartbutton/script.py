"""
Copyright (c) 2014-2016 Ehsan Iran-Nejad
Python scripts for Autodesk Revit

This file is part of pyRevit repository at https://github.com/eirannejad/pyRevit

pyRevit is a free set of scripts for Autodesk Revit: you can redistribute it and/or modify
it under the terms of the GNU General Public License version 3, as published by
the Free Software Foundation.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

See this link for a copy of the GNU General Public License protecting this package.
https://github.com/eirannejad/pyRevit/blob/master/LICENSE
"""
from pyrevit.logger import get_logger
from pyrevit.config import ICON_LARGE
from pyrevit.loader import updater
import pyrevit.session as session

logger = get_logger(__commandname__)

__doc__ = 'Downloads updates from the github repository.'


def __selfinit__(script_cmp, commandbutton, __rvt__):
    has_update_icon = script_cmp.get_bundle_file('icon_hasupdates.png')

    for repo in updater.get_all_available_repos():
        if updater.has_pending_updates(repo):
            commandbutton.set_icon(has_update_icon, icon_size=ICON_LARGE)


if __name__ == '__main__':
    # collect a list of all repos to be updates
    repo_info_list = updater.get_all_available_repos()
    logger.debug('List of repos to be updated: {}'.format(repo_info_list))

    for repo_info in repo_info_list:
        # update one by one
        logger.info('Updating repo: {}'.format(repo_info))
        if updater.update_pyrevit(repo_info):
            logger.info('Successfully updated: {}'.format(repo_info))

    # now re-load pyrevit session.
    logger.info('Reloading...')
    session.load()
