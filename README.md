# PyEBCDIC
A EBCDIC parsing and encoding tool.<br>

## Usage
### Punched Card to Text
```shell
python EBCDICPCParser.py [Punched Card File] [Output File]
```
### Text to Punched Card
```shell
python EBCDICToPC.py [Text File] [Output File]
```

## About Punched Card File
**'(space)'** means **not punched**.<br>
**'0'** means **punched**.<br>
The characters in each line maps to **'YX0123456789'** of **IBM 80-column punched card**.

## EBCDIC Table
[Link](http://www.quadibloc.com/comp/cardint.htm)
