#! /usr/bin/env python3

#a script to create a matrix of presences and absences of orthogroups from an Orthogroups.GeneCount.tsv file

import argparse

def make_matrix():
    try:
        with open("{0}".format(args.infile), "r") as old:
            with open("{0}".format(args.outfile), "w") as new:
                for line in old:
                    if line.startswith("Orthogroup"):
                        new.write(line)
                    else:
                        presabs = []
                        line = line.split("\t")
                        for item in line:
                            if item.startswith("OG"):
                                presabs.append(item)
                            else:
                                if int(item) >= 1:
                                    presabs.append("1")
                                else:
                                    presabs.append("0")
                        newline = "\t".join(presabs)
                        new.write(newline)
                        new.write("\n")
    except IOError:
        print("Problem reading or writing files")

parser = argparse.ArgumentParser(description = "arguments for the presence/absence matrix file")
parser.add_argument("-i", "--infile", required = True, help = "path to file to be converted")
parser.add_argument("-o", "--outfile", required = True, help = "path to new matrix file")
args = parser.parse_args()

make_matrix()
