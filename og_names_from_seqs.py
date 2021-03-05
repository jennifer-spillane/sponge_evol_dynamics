#! /usr/bin/env python3

#function to identify orthogroups associated with individual sequences.
#needs a list of sequences of interest, and a directory of fastas to search through.
#written to find which orthogroups contain alien sequences after alien indexing yields lists of alien proteins.
#also works to find with orthogroups contain sequences that are associated with specific GO terms!

import argparse
import os
import Bio.SeqIO
import re

def identify_ogs():

    #create a dictionary to hold seq names of interest (in this case alien seqs) and the OGs they are a part of
    #create a dictionary to hold count info for each OG
    aliens_with_ogs = {}
    ogs_and_counts = {}
    alien_seqs = set()

    try:
        with open("{0}".format(args.listfile), "r") as inlist:
            #add all the sequence names to a set
            for seq in inlist:
                seq_name = seq.strip()
                alien_seqs.add(seq_name)
            with open("{0}".format(args.output), "w") as outlist:
                with open("{0}".format(args.countfile), "w") as counts:
                    #scan through the directory containing the fasta files to be searched
                    #isolate the name of the orthogroup from the file name
                    for file in os.scandir("{0}".format(args.directory)):
                        og_name = re.match("(OG\d+)\.fa", "{0}".format(file.name))
                        if og_name:
                            #go through each sequence in the fasta and check to see if the name matches one in the set
                            #if it does, put the sequence name as the key and the orthogroup as the value of a dictionary
                            for record in Bio.SeqIO.parse("{0}".format(file.path), "fasta"):
                                if record.id in alien_seqs:
                                    aliens_with_ogs.setdefault(record.id, og_name.group(1))
                                else:
                                    continue


                    #now write the first output file with the info from the first dictionary
                    #populate the second dictionary with counts as it goes
                    for item in aliens_with_ogs:
                        outlist.write("{0}\t{1}\n".format(item, aliens_with_ogs[item]))
                        ogs_and_counts.setdefault(aliens_with_ogs[item], 0)
                        ogs_and_counts[aliens_with_ogs[item]] += 1
                    #write out the count info also 
                    for entry in ogs_and_counts:
                        counts.write("{0}\t{1}\n".format(entry, ogs_and_counts[entry]))



    except IOError:
        print("Issue reading or writing file")

parser = argparse.ArgumentParser(description = "Arguments for extracting clade-specific orthogroups")
parser.add_argument("-l", "--listfile", help = "path to input list of sequences that have been flagged as interesting")
parser.add_argument("-d", "--directory", help = "path to a directory that contains fasta files")
parser.add_argument("-o", "--output", help = "path to an outputted list file with all the orthogroup names")
parser.add_argument("-c", "--countfile", help = "path to a new file to hold count data for the orthogroups")
args = parser.parse_args()

identify_ogs()
