# -*- coding: utf-8 -*-
"""
/***************************************************************************
 autoesdaPlugin
                                 A QGIS plugin
 This plugin automates the exploratory spatial data analysis (ESDA) process by summarizing numerous statistics in an HTML report.
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                             -------------------
        begin                : 2022-04-30
        copyright            : (C) 2022 by Nicholas De Kock
        email                : nicholas.dekock@tuks.co.za
        git sha              : $Format:%H$
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""


# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load autoesdaPlugin class from file autoesdaPlugin.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .autoesda_plugin import autoesdaPlugin
    return autoesdaPlugin(iface)
