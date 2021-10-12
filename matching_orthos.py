#! /usr/bin/env python3 


#This script will take a list of orthogroup names, and search through a fasta file that has OG names as part of the heading.
#When it finds matches, it will pull those sequences (and their headers, obviously) out and into a new file 

import argparse 
import re 
import Bio.SeqIO 

def matching_orthos():








#! /usr/bin/env python3

#a function to pull the gene tree files that correspond to a list of gene trees of interest
#could be anything of interest in a list of gene trees.
#this script pulls gene trees based on identity number, but pull_short_gene_trees.py will work on order number within the directory

import argparse
import os
import shutil
import re

def psgt():
    #creating the set I'll need inside the loop
    certain_set = set()
    #putting all of the numbers of interest into a set for easy comparison
    try:
        with open("{0}".format(args.tree_nums), "r") as interesting:
            print("opened interesting gene tree num file")
            for line in interesting:
                tree = line.strip()
                certain_set.add(tree)
            print("made set of gene tree nums")
            try:
                os.mkdir("{0}".format(args.new_dir))
            except FileExistsError:
                print("This directory already exists. Please provide a different name")
            #scanning through the directory of gene trees and finding the ones that match up with the numbers
            #in the list file provided. Copying these trees to a new directory
            for item in os.scandir("{0}".format(args.tree_dir)):
                just_name = re.match("(Mus_musculus\|\d+_rename)\.phylip\.treefile", "{0}".format(item.name))
                if just_name.group(1) in certain_set:
                    #copy the ones that match into the directory you made earlier
                    destination = os.path.join(args.new_dir, item.name)
                    shutil.copy(item.path, destination)

    except IOError:
        print("problem reading file")


parser = argparse.ArgumentParser(description = "arguments for filtering OGs to only those with a given number of taxa")
parser.add_argument("-t", "--tree_nums", required = True, help = "list of gene tree numbers of interest")
parser.add_argument("-d", "--tree_dir", required = True, help = "path to a directory with gene trees in it")
parser.add_argument("-n", "--new_dir", required = True, help = "path to a directory for the desired gene trees")
args = parser.parse_args()

psgt()

#/mnt/lustre/macmaneslab/jlh1023/pipeline_dev/pipeline_scripts/pull_certain_gene_trees.py \
#-t /mnt/lustre/macmaneslab/jlh1023/phylo_qual/actual_final/comparisons/common_to_both.txt \
#-d /mnt/lustre/macmaneslab/jlh1023/phylo_qual/actual_final/good/trees/gene_trees/ \
#-n /mnt/lustre/macmaneslab/jlh1023/phylo_qual/actual_final/good/trees/good_common_gene_trees




#! /usr/bin/env python3

import argparse
import Bio.SeqIO

#function to pull members of one-to-one orthogroups from a protein fasta file
def pull():
    try:
        #creating an empty set and dictionary to hold orthogroups
        ogs = set()
        ols = {}
        prot_set = set()
        with open("{}".format(args.cluster), "r") as cluster_file:
            with open("{}".format(args.ortho), "r") as ortho_file:
                #saving all the orthogroup names in a set
                print("Getting orthogroup names from kinfin file")
                for line in cluster_file:
                    line = line.split("\t")
                    if line[0].startswith("OG"):
                        ogs.add(line[0])
                print("Pulled orthogroup names from kinfin file")

                #populating the dictionary with keys = orthogroup names,
                #and values = a list of the proteins in that orthogroup
                #also making a set that contains all the protein names
                print("Getting protein names from orthofinder file")

                for line in ortho_file:
                    if line.startswith("OG"):
                        #stripping of white space and splitting on tabs
                        line = line.rstrip()
                        line = line.lstrip()
                        line = line.split("\t")
                        #if the OG name is in the set, put all the proteins into a new set (and dictionary)
                        if line[0] in ogs:
                            ols.setdefault(line[0], line[1:])
                            for protein in line[1:]:
                                protein = protein.split(", ")
                                for indv in protein:
                                    if indv != "":
                                        prot_set.add(indv)
                print("Pulled {0} protein names from orthofinder file".format(len(prot_set)))

        print("Parsing the fasta file")
        #running through the catted fasta of all the proteins and pulling those seqs that
        #match the ones in the set.
        prot_seqs = []
        prot_names = set()
        for record in Bio.SeqIO.parse("{}".format(args.prots), "fasta"):
            if record.id in prot_set:
                cur_prot = Bio.SeqRecord.SeqRecord(id = record.id, seq = record.seq, description = "")
                cur_prot_name = record.id
                prot_seqs.append(cur_prot)
                prot_names.add(cur_prot_name)
        test_set = prot_set.difference(prot_names)
        print(len(test_set))
        print(test_set)

        Bio.SeqIO.write(prot_seqs, "{}".format(args.out), "fasta")

    except IOError:
        print("Problem reading files")

parser = argparse.ArgumentParser(description = "arguments for pulling 1-to-1 orthologues from a fasta")
parser.add_argument("-c", "--cluster", required = True, help = "all.all.cluster_1to1s.txt provided by kinfin")
parser.add_argument("-r", "--ortho", required = True, help = "Orthogroups.csv provided by orthofinder")
parser.add_argument("-p", "--prots", required = True, help = "fasta file containing all proteins in the orthofinder analysis")
parser.add_argument("-o", "--out", required = True, help = "name of the output fasta file")
args = parser.parse_args()

pull()