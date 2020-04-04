# Coding theory implemented algorithms 2019

![](https://github.com/andraspatka/Coding_theory/workflows/Encode%20CLI%20Project/badge.svg)

## Usage of Python scripts

# encode.py

Is a CLI for creating a statistic of how many times each character appears in the input document and encoding the input file using the Shannon-Fano or Huffman encoding.

The following script can be invoked from the command line:

```bash
encode.py [task] [filename]
```

For help, invoke it as such:

```bash
encode.py -h
```

Currently available tasks:
 - **-d** : creates and displays the symbol appearance statistics
 - **-sf** : encodes the input file using Shannon-Fano encoding
 - **-sfs** : encodes the input file using Shannon-Fano encoding and prints the encoding's optimality
 - **-hf** : encodes the input file using Huffman encoding
 - **-hfs** : encodes the input file using Huffman encoding and prints the encoding's optimality
 - **-ac** : encodes the input file using Arithmetic coding
 - **-h** :  prints the help message
 
