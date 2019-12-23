# -*- coding: utf-8 -*-
"""
/***************************************************************************
 ToRadians
                                 A QGIS plugin
 This converts the Latitude and Longitude to Radians
                             -------------------
        begin                : 2019-06-20
        copyright            : (C) 2019 by Ilayaraja
        email                : ilayaraja22@gmail.com
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
    """Load ToRadians class from file ToRadians.

    :param iface: A QGIS interface instance.
    :type iface: QgisInterface
    """
    #
    from .to_radians import ToRadians
    return ToRadians(iface)
