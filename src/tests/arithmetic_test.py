from arithmetic import convertToCode

def test_convertToCode():
    assert convertToCode(0.6875) == "1011"
    assert convertToCode(0.125) == "001"
    assert convertToCode(0.260509077) == "0100001010"