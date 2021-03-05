#! /usr/bin/env python3

#a script to count the number of sequences in a given fasta file.
#it will record the number with the name of the fasta

import Bio.SeqIO
import os
import argparse

def count():
    #make a list to hold each tuple later
    list_of_seqcounts = []
    try:
        #scan through the files in a directory looking for fasta ones
        for file in os.scandir("{0}".format(args.indir)):
            if file.name.endswith("fa") or file.name.endswith("fasta"):
                #establish a counter and loop through the sequence records counting them
                seq_count = 0
                for record in Bio.SeqIO.parse("{0}".format(file.path), "fasta"):
                    seq_count += 1
                #create a tuple containing the fasta name and the number of seqs it has
                #add this tuple to the list we made earlier
                num_seqs = (file.name, seq_count)
                list_of_seqcounts.append(num_seqs)
            else:
                continue

        #write to the outfile, looping through the list and separating the tuple elements with tabs 
        with open("{0}".format(args.outfile), "w") as out:
            for pair in list_of_seqcounts:
                out.write("{0}\t{1}\n".format(pair[0], pair[1]))
    except IOError:
        print("Issue writing file")

parser = argparse.ArgumentParser(description = "Arguments for extracting clade-specific orthogroups")
parser.add_argument("-d", "--indir", help = "path to a directory that contains fasta files")
parser.add_argument("-o", "--outfile", help = "path to an outputted tsv file with all the file names and how many seqs they contain")
args = parser.parse_args()

count()
