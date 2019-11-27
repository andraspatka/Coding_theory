# Coding theory implemented algorithms 2019

![](https://github.com/andraspatka/Coding_theory/workflows/Encode%20CLI%20Project/badge.svg)

## Usage of Python scripts

# encode.py

Creates a statistic of how many times each character appears in the input document. The created statistic is output to stdout and to out.txt

The following script can be invoked from the command line:

```bash
encode.py [task] [filename]
```

For help, invoke it as such:

```bash
encode.py [task] [filename]
```

Currently available tasks:
 - **-d** : creates and displays the symbol appearance statistics
 - **-sf** : encodes the input file using Shannon-Fano encoding
 - **-sfs** : encodes the input file using Shannon-Fano encoding and prints the encoding's optimality
 - **-h** :  prints the help message
