# -*- coding: utf-8 -*-
"""
Visualisation of central filed.
Field center at (1,2)
Field magnitude varies linearly with distance to center.
Field has unit magnitude at (-2,1)
"""


import matplotlib.pyplot as plt
import numpy

def central_field(at, center, factor):
    """Calculate value of central vector field at given point.

    Parameters
    ----------
    at : numpy (2,) vector
        Position (x,y) to calculate the field
    center: nmpy (2,) vector
        Center or the field
    factor:
        Magnitude scaling factor

    Returns
    -------
    numpy (2,) vector
        Field vector at given point
    """
    # Calculate vector from 'center' to point 'at' and scale it by give factor
    v = (at - center)*factor
    return v

def scaling_factor(center, unit_point):
    """Calculate scaling factor for the field
    
    Parameters
    ----------
    at : numpy (2,) vector
        Position (x,y) to calculate the field
    center: numpy (2,) vector
        Center or the field
    """
    return 1/numpy.linalg.norm(center - unit_point)


def show_field(points, field):

    fig, ax = plt.subplots()

    ax.quiver(points[:, 0], points[:, 1], field[:, 0], field[:, 1], scale=4)

    ax.set_xlim(-10, 10)
    ax.set_ylim(-10, 10)
    ax.set_aspect('equal', adjustable='box')

    plt.show()

def main():
    center = numpy.array([1.0, 2.0])
    unit_point = numpy.array([-2.0, 1.0])
    # points at which to calculate field
    points = numpy.array([[3.0, 1.0],
                          [1.0, 2.0],
                          [-2.0, 3.0],
                          [0.0, 0.0],
                          [2.5, 2.5]])
    # prepare array to store field
    field = numpy.empty(points.shape, dtype='float64')
    
    factor = scaling_factor(center, unit_point)
    
    for i in range(points.shape[0]):
        field[i, :] = central_field(points[i,:], center, factor)
    
    show_field(points, field)

if __name__ == '__main__':
    main()
