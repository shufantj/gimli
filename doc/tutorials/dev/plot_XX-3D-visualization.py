#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
3D Visualization (Proof of concept)
-----------------------------------
"""

import pygimli as pg
from pygimli.viewer import show

mesh = pg.createMesh3D(1,1,1)

"""
If interactive is set to True, a Mayavi window pops up which allows for
interactive introspection. If it is set to False, mayavi produces a pixel array
of the scene which is plotted in a mpl figure and therefore
automatically picked up by the plot2rst extension for the documentation.

"""

show(mesh, interactive=False)

"""
.. image:: PLOT2RST.current_figure
    :scale: 75

"""
<<<<<<< .working
=======
pg.showNow()>>>>>>> .new
