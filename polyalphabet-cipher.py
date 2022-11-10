# coding=utf-8
import sys, getopt
from string import ascii_lowercase
from collections import Counter

##----TODO-------
#
#
#
#encriptar pasando por parámetro el keyword
#
##--------------

inputfile = ''
outputfile = ''
metodo = ''
keyword = ''

def decrypt(llave,ifile,ofile):
    if ofile != 'none':
        archivo = open(ofile,"w")
    
    with open(ifile) as mensaje:
        for line in mensaje:
            key = 0
            for c in line:
                diferencia = (ord(c) - ord(llave[key]))
                if diferencia == 0:
                    chLetra = 'a'
                elif diferencia > 0:
                    chLetra = chr(97 + diferencia)
                else:
                    chLetra = chr(123 + diferencia)
                if key == (len(llave)-1):
                    key = 0
                else:
                    key = key + 1
                if ofile != 'none':
                    archivo.write(chLetra)
                else:
                    print chLetra,
    if ofile != 'none':
        archivo.close()
        print 'Status : COMPLETED'

def main(argv):
    
    try:
        opts, args = getopt.getopt(argv, "hi:o:cd", ["keyword=","ifile=","ofile="])
    except getopt.GetoptError:
        print 'polyalphabetic-cipher.py -<metodo> -k <keyword> -i <inputfile> -o <outputfile OR "none">'
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print 'polyalphabet-cipher.py -<metodo> -k <keyword> -i <inputfile> -o <outputfile OR "none">'
            sys.exit()
        elif opt == "-c":
            metodo = 'crypt'
        elif opt == "-d":
            metodo = 'decrypt'
        elif opt in ("-w", "--keyword"):
            keyword = arg
        elif opt in ("-i", "--ifile"):
            inputfile = arg
        elif opt in ("-o", "--ofile"):
            outputfile = arg
    if metodo == 'decrypt':
        decrypt(keyword,inputfile,outputfile)

if __name__ == "__main__":
    main(sys.argv[1:])
