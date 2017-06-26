import numpy

from visit import *


def OperatorSettings(OperatorSet, myList, Centroids=None):
    """Add operator and its settings."""

    if OperatorSet == "Clip":
        """
        with no args - default octant, rotation and midpoint
        [{loc:(x,y,z),oct:(+/-1,+/-1,+/-1),rot:(alpha,beta,gamma)},...]
        produces one image for each dictionary
        """

        myList = dict(myList)

        Attribute = ClipAttributes()

        Attribute.quality = Attribute.Accurate

        Attribute.plane1Status = 1  # yz-plane
        Attribute.plane2Status = 1  # xz-plane
        Attribute.plane3Status = 1  # xy-plane

        if "loc" in myList:
            xpos = myList["loc"][0]
            ypos = myList["loc"][1]
            zpos = myList["loc"][2]

            Attribute.plane1Origin = (xpos, 0, 0)
            Attribute.plane2Origin = (0, ypos, 0)
            Attribute.plane3Origin = (0, 0, zpos)

        else:
            Attribute.plane1Origin = (min(Centroids)[0], 0, 0)
            Attribute.plane2Origin = (0, min(Centroids)[1], 0)
            Attribute.plane3Origin = (0, 0, min(Centroids)[2])
            print min(Centroids)

        Attribute.plane1Normal = (myList["oct"][0], 0, 0)
        Attribute.plane2Normal = (0, myList["oct"][1], 0)
        Attribute.plane3Normal = (0, 0, myList["oct"][2])

        if "rot" in myList:
            xdeg = myList["rot"][0]
            ydeg = myList["rot"][1]
            zdeg = myList["rot"][2]

            ResetView()

            # Set view
            v = GetView3D()

            v.RotateAxis(0, float(xdeg))  # rotate around x-axis
            v.RotateAxis(1, float(ydeg))  # rotate around y-axis
            v.RotateAxis(2, float(zdeg))  # rotate around z-axis

            SetView3D(v)

        else:
            ResetView()

            # Set view
            v = GetView3D()

            v.viewNormal = (myList["oct"][0], myList["oct"][1], myList["oct"][2])

            SetView3D(v)

        SetOperatorOptions(Attribute)

    if OperatorSet == "Slice":
        """
        with no args - default direction and location
        [(<x,y,z>,val),(<x,y,z>,val),....]
        produces one image for each tuple with slice at plane <x,y,z>=val
        """

        myList = list(myList)

        Attribute = SliceAttributes()

        Attribute.originType = Attribute.Point

        if myList[0] == 'x':
            Attribute.originPoint = (myList[1], 0, 0)

        if myList[0] == 'y':
            Attribute.originPoint = (0, myList[1], 0)

        if myList[0] == 'z':
            Attribute.originPoint = (0, 0, myList[1])

        Attribute.axisType = eval("Attribute."+str(myList[0]).upper()+"Axis")

        SetOperatorOptions(Attribute)
