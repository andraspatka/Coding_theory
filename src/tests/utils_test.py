# utils_test.py
import utils

def test_printInvalidUsageErrorMessage(capfd):
    utils.printInvalidUsageErrorMessage()
    out, err = capfd.readouterr()
    assert out == ""
    assert err == "Invalid usage! Invalid number of arguments.\nCorrect usage: encode.py [task] [filename]\nFor help, use: encode.py -h"
