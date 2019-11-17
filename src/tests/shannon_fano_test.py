# shannon_fano_test.py
import shannon_fano

def test_indexToPartAt_perfectParting():
    p = [50.0, 25.0, 12.5, 6.25, 3.125, 3.125]
    for i in range(0, 5):
        assert callIndexToPartAt(p) == 1
        p = p[1:]

def test_indexToPartAt_imperfectParting():
    p = [30.0, 11.0, 6.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 3.0]
    assert callIndexToPartAt(p) == 4

    p = [30.0, 11.0, 7.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 2.0]
    assert callIndexToPartAt(p) == 3

def test_indexToPartAt_oneElement():
    p = [50.0]
    assert callIndexToPartAt(p) == 0

def test_indexToPartAt_twoElements():
    p1 = [50.0, 10.0]
    p2 = [30, 10.0]
    assert callIndexToPartAt(p1) == 1
    assert callIndexToPartAt(p2) == 1

def test_indexToPartAt_3ElementsSameProb():
    p = [3.0, 3.0, 3.0]
    assert callIndexToPartAt(p) == 1

def test_indexToPartAt_emptyList():
    p = []
    assert callIndexToPartAt(p) == 0

"""
Convenience method for calling shannon_fano.indexToPartAt
"""
def callIndexToPartAt(probs):
    return shannon_fano.indexToPartAt(createCodesTestData(probs), 0, len(probs))

"""
Creates test data from a list of probabilities
"""
def createCodesTestData(probabilities):
    return [['', '', p] for p in probabilities]