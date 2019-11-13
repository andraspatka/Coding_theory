# encode_test.py
import errno
import subprocess

def test_argumentListTooShort():
    command = ["python", "encode.py"]
    out, err, exitCode = capture(command)

    assertInvalidUsageMessage(err)
    assert out == b''
    assert exitCode == errno.EINVAL

def test_firstArgumentHelp():
    command = ["python", "encode.py", "-h"]
    out, err, exitCode = capture(command)
    outputMessages = out.split(b'\r\n')

    assert len(outputMessages) == 5
    assert outputMessages[0] == b'Usage: encode.py [task] [filename]'
    assert outputMessages[1] == b'Available tasks: -d:  creates and displays the symbol appearance statistics'
    assert outputMessages[2] == b'                 -sf: performs a shannon-fano encoding'
    assert outputMessages[3] == b'                 -h:  displays this message'
    assert outputMessages[4] == b'' #Trailing endline

    assert err == b''
    assert exitCode == 0

def test_argumentListInvalid_tooShort():
    command = ["python", "encode.py", "invalid"]
    out, err, exitCode = capture(command)

    assertInvalidUsageMessage(err)
    assert out == b''
    assert exitCode == errno.E2BIG

def test_argumentListInvalid_tooLong():
    command = ["python", "encode.py", "invalid", "arg", "list"]
    out, err, exitCode = capture(command)

    assertInvalidUsageMessage(err)
    assert out == b''
    assert exitCode == errno.E2BIG

def test_invalidTask():
    command = ["python", "encode.py", "-todo", "file.txt"]
    out, err, exitCode = capture(command)

    errorMessages = err.split(b'\r\n')
    assert len(errorMessages) == 2
    assert errorMessages[0] == b'Invalid usage! The given task: -todo does not exist!'
    assert errorMessages[1] == b'For help, use: encode.py -h'

    assert out == b''
    assert exitCode == errno.EINVAL

def test_fileDoesNotExist():
    command = ["python", "encode.py", "-d", "file.txt"]
    out, err, exitCode = capture(command)

    errorMessages = err.split(b'\r\n')
    assert len(errorMessages) == 1
    assert errorMessages[0] == b'Could not find input file: file.txt'

    assert out == b''
    assert exitCode == errno.ENOENT

"""
Helper function for checking the invalid usage message.
"""
def assertInvalidUsageMessage(err):
    errorMessages = err.split(b'\r\n')

    assert len(errorMessages) == 3
    assert errorMessages[0] == b'Invalid usage! Invalid number of arguments.'
    assert errorMessages[1] == b'Correct usage: encode.py [task] [filename]'
    assert errorMessages[2] == b'For help, use: encode.py -h'

"""
Helper function for testing the encode.py CLI
"""
def capture(command):
    proc = subprocess.Popen(command,
        stdout = subprocess.PIPE,
        stderr = subprocess.PIPE,
    )
    out,err = proc.communicate()
    return out, err, proc.returncode
