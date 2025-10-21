from isTriangle import Triangle


def testInvalidZeroSide():
    assert Triangle.classify(0, 3, 4) == Triangle.Type.INVALID


def testInvalidInequalityNonequal():
    assert Triangle.classify(2, 3, 5) == Triangle.Type.INVALID


def testValidScalene():
    assert Triangle.classify(3, 4, 5) == Triangle.Type.SCALENE


def testValidEquilateral():
    assert Triangle.classify(2, 2, 2) == Triangle.Type.EQUILATERAL


def testValidIsosceles():
    assert Triangle.classify(3, 3, 4) == Triangle.Type.ISOSCELES


def testIsoscelesFallsThroughToInvalid():
    assert Triangle.classify(2, 2, 5) == Triangle.Type.INVALID
