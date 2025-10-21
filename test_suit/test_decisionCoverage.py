from isTriangle import Triangle


def testInvalidNegativeSide():
    assert Triangle.classify(-1, 3, 4) == Triangle.Type.INVALID


def testTriZeroValidScaleneFalseInner():
    assert Triangle.classify(3, 4, 5) == Triangle.Type.SCALENE


def testTriZeroInvalidTrueInner():
    assert Triangle.classify(2, 3, 5) == Triangle.Type.INVALID


def testEquilateral():
    assert Triangle.classify(2, 2, 2) == Triangle.Type.EQUILATERAL


def testIsoscelesTri1True():
    assert Triangle.classify(3, 3, 4) == Triangle.Type.ISOSCELES


def testIsoscelesTri2True():
    assert Triangle.classify(3, 4, 3) == Triangle.Type.ISOSCELES


def testIsoscelesTri3True():
    assert Triangle.classify(4, 3, 3) == Triangle.Type.ISOSCELES


def testIsoscelesTri1FalseFallthrough():
    assert Triangle.classify(2, 2, 5) == Triangle.Type.INVALID


def testIsoscelesTri2FalseFallthrough():
    assert Triangle.classify(2, 5, 2) == Triangle.Type.INVALID


def testIsoscelesTri3FalseFallthrough():
    assert Triangle.classify(5, 2, 2) == Triangle.Type.INVALID
