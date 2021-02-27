# The workflow for putting together the metazoan dataset for the study of gene family dynamics  

Nhen and then Troy have been diligently assembling transcriptomes for this project for a long time. Then more recently Hannah has also been putting together a comprehensive metazoan dataset for use in this project and others.   

**This is what Nhen and Troy were doing to process transcriptomes:**  
- downloaded transcriptome reads from the ENA  
- removed the spaces from their headers  
    `sed -i 's_ __' file_1.fastq`  
- subsampled down to 35 million bp if necessary (1.2-r94)  
    `seqtk sample -s 51 Genus_species_1.fastq 35000000 > Genus_species_sub_1.fastq`  
- assembled using the ORP (2.2.3)  
    `oyster.mk main TMP_FILT=1 STRAND=RF MEM=110 CPU=24 READ1=Genus_species_1.fastq READ2=Genus_species_2.fastq RUNOUT=Genus_species`  
- predicted proteins with TransDecoder  
    `TransDecoder.LongOrfs -t Genus_species.fasta`  
    `TransDecoder.Predict -t Genus_species.fasta`  

**This is what Hannah was doing to process genomes:**  
- downloaded genomes (that did not already have protein models) - six species of cnidarians  
- ran BUSCO --long mode on each one  
- ran MAKER with the training models from the BUSCO run  
- final BUSCO run with both euk and met databases to determine quality  

We also downloaded already established protein datasets from genomes in various databases (Ensembl, Compagen)  

**Steps common to all datasets**  
- ran cd-hit (V4.7) on each protein set with threshold of 98% similar  
    `cd-hit -i Genus_species.fasta.transdecoder.pep -o Genus_species_98.fasta -c 0.98 -n 5 -d 0`  
- changed headers to be simple and informative  
    `awk '/^>/{print ">Genus_species_" ++i; next}{print}' Genus_species_98.fasta > Genus_species.fa`  
- ran through BUSCO once more with the euk database to make sure not too much was lost  
    `run_BUSCO.py -i Genus_species.fa -o Genus_species -m prot -l /mnt/lustre/hcgs/shared/databases/busco/eukaryota_odb9 -c 24`  


With these three sources of data combined, we had just shy of 170 species of animals and close relatives to include. These were not spread evenly across Metazoa, however. Hannah sent me the spreadsheet of all the organisms, and I annotated it with class, order, and family information, so that we could narrow things down appropriately. We had a hilarious number of cnidarians, for example, and while they are great, we just don't need all of them to do this study.  

Where we had multiple organisms in the same class, we chose the ones that had the best BUSCO scores (preliminary ones) up to three representatives from that clade, and continued with those. These can be found in this spreadsheet: https://docs.google.com/spreadsheets/d/1ZBnQyYTja2mqxcd52VBv6Z_XhC6IJW-NtcNO_-yq-kI/edit?usp=sharing.  

We decided to use 80% complete BUSCOS as the quality threshold, and took organisms that reached that threshold in either the eukaryotic or metazoan BUSCO database. We also required a 0.22 threshold for TransRate scores, where applicable. The only exceptions to these rules are the hexactinellid sponges, none of which reached the appropriate quality thresholds. Since we need to include as much sponge diversity as possible, we decided to include the three hexactinellid species anyway (*Aphrocallistes vastus*, *Rossella fibulata*, and *Sympagella nux*).  

All of these organisms (blue, green, and purple rows on the spreadsheet) I put into a new directory for OrthoFinder (/mnt/lustre/plachetzki/shared/metazoa_2020/above_80) and ran it:  
`orthofinder.py -a 24 -f /mnt/lustre/plachetzki/shared/metazoa_2020/above_80/ -t 24 -S diamond -M msa`


Premise was up and down and all over the place while this OrthoFinder run was going, and at one point I restarted it with this command instead:  
`orthofinder.py -b /mnt/lustre/plachetzki/shared/metazoa_2020/above_80/OrthoFinder/Results_Oct05/ -a 30 -t 30 -S diamond -M msa`  

This was so that it could skip the diamond steps, which it had already done, and move on to the orthogroups parts and the MSA parts.  

At this point I am 95% sure it has finished everything that it needs to do, although it sort of looked like there was a memory error at one point. But I've checked all the output files and everything seems to be accounted for, so maybe it's nothing. Regardless, all the orthogroup parts definitely finished, as it produced summary stats for them, and it does that bit before it finds MSAs for all of the orthogroups, obviously, so we can feel confident about that.  


## Post-OrthoFinder Steps  

Whenever these analyses are on premise, they will be in this directory: `/mnt/lustre/macmaneslab/jlh1023/chap3_2020`.  
Whenever they are on my computer (in R or something), they will be here: `/Users/jenniferlhill/Desktop/Analyses/gain_loss`.  



### Creating the presence/absence matrix  

Before when I was doing this, we were thinking of using KinFin for some parts of the analysis, so I ran some of the OrthoFinder files through it before processing them further. We didn't end up needing it for anything however, so I altered the make_matrix.py script slightly so that it can handle output directly from OrthoFinder instead of having another step first. Then I ran it on the new OrthoFinder output.  
`/mnt/lustre/macmaneslab/jlh1023/pipeline_dev/pipeline_scripts/make_matrix.py -i Orthogroups.GeneCount.tsv -o all_114_presabs.tsv`  

So now this `/mnt/lustre/macmaneslab/jlh1023/chap3_2020/presabs_matrix/all_114_presabs.tsv` file contains all the presences and absences for these (105177) orthogroups and species.  

### Trimming the matrix to certain OGs  

Similarly to the script above, I need to change my "half_species.py" script to reflect the fact that we are going straight from the OrthoFinder gene count file. All I had to do was give the script a different (and more logical) way to recognize the first line that it is supposed to write to the output file, so not a big deal.  

I'll do this in three different groups, with different thresholds for keeping an orthogroup in the analysis.  
**50%:** `/mnt/lustre/macmaneslab/jlh1023/pipeline_dev/pipeline_scripts/half_species.py -m all_114_presabs.tsv -o presabs_50.tsv -c 57`  
5923 orthogroups left  

**25.4%:** `/mnt/lustre/macmaneslab/jlh1023/pipeline_dev/pipeline_scripts/half_species.py -m all_114_presabs.tsv -o presabs_25.tsv -c 29`  
7268 orthogroups left  

**75.4%:** `/mnt/lustre/macmaneslab/jlh1023/pipeline_dev/pipeline_scripts/half_species.py -m all_114_presabs.tsv -o presabs_75.tsv -c 86`  
4470 orthogroups left  


**Update: we might not need the presence/absence matrix or the versions with different percentages. Many of the analyses below contain all of the orthogroups we found (105177)**  


### Dollo Parsimony  

Sabrina pulled a dollo parsimony script from another paper that she worked on and got it to stand alone, as well as run a lot of data (instead of data from just a handful of species).  

Based on those results, I now have lists of orthogroups that have been gained and lost at each internal node of the tree. Also, all the internal nodes have been named, so they are easier to identify. I'm going to focus on sponges first, and then maybe do some additional nodes to follow up. I want to run all of the sequences in these orthogroups through interproscan to figure out what they are. Then I'll do some GO analysis to see if anything is enriched. This is happening in this directory: /mnt/lustre/macmaneslab/jlh1023/chap3_2020/interesting_orthos/. I've also included the number of OGs that were lost at these nodes.  

The nodes I want to focus on first are all sponge ones:  
- Homoscleromorpha = 2374  
- Hexactinellida = 16246  
- homo+calc (renamed homo_calc when I'm working with it on premise) = 12335  
- Calcarea = 3635  
- Haplosclerida = 10724  
- Myxospongia = 13217  
- por2 = 2572  
- Porifera = 2765  

The files that go with these nodes are here: /Users/jenniferlhill/Dropbox/Jenn_R/metazoa_ortho_dollo/all_114_presabs/losses_by_node_tip/  

I can just take one of these files, copy it onto premise, and use it to extract the necessary files from the orthofinder results directory with an old script I wrote to pull out interesting alignments. These are not alignments, but it works the same way on unaligned orthofinder output. The -l is the file that lists the OGs of interest, -a is a path to a directory containing the sequence (or alignment) files, and -n is a new directory in which to place all the right sequence files that match the OGs of interest.  
`/mnt/lustre/macmaneslab/jlh1023/pipeline_dev/pipeline_scripts/pull_alignments.py -l Homoscleromorpha.txt -a /mnt/lustre/plachetzki/shared/metazoa_2020/above_80/OrthoFinder/Results_Oct19/Orthogroup_Sequences/ -n /mnt/lustre/macmaneslab/jlh1023/chap3_2020/interesting_orthos/Homoscleromorpha_seqs`  

#### Interproscanning  

Once I have them all in a directory, I need to make sure there are no asterisks in any of the files, as interproscan will choke and die on them. I wrote a script ages ago that does this. Only argument necessary is the directory from the previous script.    
`/mnt/lustre/macmaneslab/jlh1023/pipeline_dev/pipeline_scripts/remove_asterisks.py Homoscleromorpha_seqs/`  

I like to go into the directory with all the seq files before I cat them together, to avoid weirdness with the paths, then I cat them together, and then I move it out to the parent directory where everything else is happening.  

```bash
cd Homoscleromorpha_seqs/  
cat *.fa > ../Homoscleromorpha_all.fa   
cd ..  
```

And then we can run interproscan.  
`interproscan -i Homoscleromorpha_all.fa -b Homoscleromorpha_inter -goterms -f TSV`  

*This works great for smaller groups or orthogroups, but can still take forever for larger orthogroups or clades with more losses, so we're putting in another filtering step before we get to the interproscanning bit.*  

I'm going to go into the directory with all the seqs just like above, apply the filter, cat them all together into a new file in the parent directory, and back out.  

```bash  
cd Homoscleromorpha_seqs/  
./uclust.sh  
cat *.fasta > ../Homoscleromorpha_filtered.fa  
cd ..  
```  

The contents of `uclust.sh` is below. I'm using an identity of 60% (50% is the lowest you can go and still have the algorithm function properly, and higher values will yield more clusters, which doesn't help us pare down the data very much, plus we have a hugely diverse dataset, so lower numbers make sense), and having it output all it's files with a ".fasta" ending, so they are slightly different from the original files.    

```bash  
#! /bin/bash  
for fs in $(ls *fa)  
do  
usearch -cluster_fast $fs -id 0.6 -centroids $fs.fasta -uc $fs.uc  
done  
```

Now the interproscan line changes but only a little:  
`interproscan -i Homoscleromorpha_filtered.fa -b Homoscleromorpha_inter -goterms -f TSV`  



**Update again:**   
This works great for the majority of clades, but I need to interproscan all of the orthogroups that are present at the ancestral Metazoa node, and it is a lot. It is either erroring on premise right now, or going so slowly that it might as well be, so instead of the standard approach that i've done for all the other clades above, I'm splitting up the OGs at this node and running them as different interproscan jobs so that they might actually finish. This means that everything will look exactly the same, except when I'm catting all the fastas together, I'll just cat some of them together. So I'll have five files total, instead of just one for this particular node. The commands to get the first two are shown below.  
`cat *0.fa.fasta *1.fa.fasta >> ../met1_filtered.fa`  
`cat *2.fa.fasta *3.fa.fasta >> ../met2_filtered.fa`  



#### GO term analysis on the interproscan results  

Over the weekend all of the interproscan jobs finished (except Hexactinellida, which ran out of memory - I've submitted it with more so fingers crossed it finishes this time), so now I'm going to move on to the next step, which is gene ontology (GO) analysis. I'm going to do it the same way I did for the transcriptome quality paper, in topGO in R.  

I need some kind of "gene universe" to compare the sponge losses to, so I'm going to use all of the OGs present at the Metazoa node, as well as the OGs that sponges have gained at various nodes in their tree. This should work, as that should be everything (or nearly everything) that they've lost, so the losses will be a subset of the total OGs for which I have GO terms. Did I need to interproscan all those sponge node losses? Possibly not. I'm going to try this approach first and see how it works.  

I'm using the same procedure as above to get to the interproscanning step, I'm just doing it for Metazoa presences (input to interproscan is "Metazoa_present_filtered.fa", output is "Metazoa_present_inter.tsv" *Now these are 1-5*), sponge gains (input into interproscan is "sponge_specific_filtered.fa", output is "sponge_specific_inter.tsv"), and the node in between, labeled as "sponge+rest" in the R output files (input into interproscan is "sponge_rest_filtered.fa", output is "sponge_rest_inter.tsv").  

First, I'm catting all of the tsv files that I will use in the gene universe together. Command below.  
`cat Metazoa_present_inter1.tsv Metazoa_present_inter2.tsv Metazoa_present_inter3.tsv Metazoa_present_inter4.tsv Metazoa_present_inter5.tsv sponge_rest_inter.tsv sponge_specific_inter.tsv > gene_universe_raw.tsv`  

Now I want to filter out the sequences that could be alien sequences using a script I wrote for this purpose. It will weed out any sequences whose names are in a list, so I can use it for the operons too. First, I need a list of all the alien sequences that were found in sponges, and a list of each putative operon sequence found in sponges. I'll save each file as I do each step, in case I want to go back to one.  
```bash
#From /mnt/lustre/macmaneslab/jlh1023/chap3_2020/alien_indexing/sponge_indexing/
cat *alienseqs.txt >> all_sponge_aliens.txt

#From /mnt/lustre/macmaneslab/jlh1023/chap3_2020/interesting_orthos/
/mnt/lustre/macmaneslab/jlh1023/pipeline_dev/pipeline_scripts/no_aliens_interproscan.py -a /mnt/lustre/macmaneslab/jlh1023/chap3_2020/alien_indexing/sponge_indexing/all_sponge_aliens.txt -t gene_universe_raw.tsv -o gene_universe_no_aliens.tsv

#From /mnt/lustre/macmaneslab/jlh1023/chap3_2020/operons/sponge_pep_operons/
cat *operons.txt >> all_sponge_operons.txt

#From /mnt/lustre/macmaneslab/jlh1023/chap3_2020/interesting_orthos/
/mnt/lustre/macmaneslab/jlh1023/pipeline_dev/pipeline_scripts/no_aliens_interproscan.py -a /mnt/lustre/macmaneslab/jlh1023/chap3_2020/operons/sponge_pep_operons/all_sponge_operons.txt -t gene_universe_no_aliens.tsv -o gene_universe_no_ops_aliens.tsv
```  

How much the file decreased through these filtering steps:  
- gene_universe_raw.tsv = 12126445  
- gene_universe_no_aliens.tsv = 11959436  
- gene_universe_no_ops_aliens.tsv = 11782979  


Now I can pull out just the things I will need to run these data through topGO. I use a simple cut command to pull out the columns I want.    
`cut -f 1,14 gene_universe_no_ops_aliens.tsv > gene_universe_no_ops_aliens_goterms.tsv`  


**Update:** This is overall a good plan, but I am going to modify it to do the actual GO analysis. I want more specialized gene universes to use in the analysis, because I don't want them to be skewed by the fact that they contain genes that that particular clade could not have. So now the strategy is to use all of the Metazoa presences, the gains at sponge+rest and Porifera, and then to tailor the rest of the gains that I include to the node in question. I will list these below. "Metazoa" always refers to presences, but all of the others refer to gains at that node.    
- Homoscleromorpha: Metazoa, sponge_rest, Porifera, homo_calc, Homoscleromorpha   
- Hexactinellida: Metazoa, sponge_rest, Porifera, por2, Hexactinellida    
- homo_calc: Metazoa, sponge_rest, Porifera, homo_calc  
- Calcarea: Metazoa, sponge_rest, Porifera, homo_calc, Calcarea  
- Haplosclerida: Metazoa, sponge_rest, Porifera, por2, Demospongiidae, Heteroscleromorpha, Haploscerida  
- Myxospongia: Metazoa, sponge_rest, Porifera, por2, Demospongiidae, Myxospongia    
- por2: Metazoa, sponge_rest, Porifera, por2  
- Porifera: Metazoa, sponge_rest, Porifera   

Since I did not interproscan these all separately, I will need to pull out the appropriate sequences from the output. I wrote a script that filters out sequences from interproscan results, so I'm converting it into a new one that will do the opposite - keep those sequences that are in a list provided to it. I'm going to start with Porifera, since I'll need it for all the others and it is the most fundamental, but all the others will be done the same way.    

To pull these out, I'm going to start the same way that I did when I was interproscanning, and use the `pull_alignments.py` script. This will give me a directory with all of the othrogroup file in it. These fasta files contain all the sequences in that orthogroup. I will need to cat these sequences together, pull out just the sequence names, and remove the ">" symbol from the front so that they are just a list of sequence names.  
`/mnt/lustre/macmaneslab/jlh1023/pipeline_dev/pipeline_scripts/pull_alignments.py -l sponge_gains/Porifera.txt -a /mnt/lustre/plachetzki/shared/metazoa_2020/above_80/OrthoFinder/Results_Oct19/Orthogroup_Sequences/ -n /mnt/lustre/macmaneslab/jlh1023/chap3_2020/interesting_orthos/Porifera_gain_seqs/`  
`grep -h ">" Porifera_gain_seqs/*fa | sed 's_>__' > Porifera_gain_seq_names.txt`  
`/mnt/lustre/macmaneslab/jlh1023/pipeline_dev/pipeline_scripts/prune_interpro_results.py -l Porifera_gain_seq_names.txt -t sponge_specific_inter.tsv -o Porifera_gain_inter.tsv`  

Now, I can combine this interproscan results file (the pruned down one I just made) with the ones from Metazoa and sponge_rest, and filter it to get rid of alien sequences. Then the filtered file will be the gene universe I need for testing the gene enrichment for the Porifera gains and losses.  
`cat Metazoa_present_inter1.tsv Metazoa_present_inter2.tsv Metazoa_present_inter3.tsv Metazoa_present_inter4.tsv Metazoa_present_inter5.tsv sponge_rest_inter.tsv Porifera_gain_inter.tsv > gene_universe_Porifera_raw.tsv`  
`/mnt/lustre/macmaneslab/jlh1023/pipeline_dev/pipeline_scripts/no_aliens_interproscan.py -a /mnt/lustre/macmaneslab/jlh1023/chap3_2020/alien_indexing/sponge_indexing/all_sponge_aliens.txt -t gene_universe_Porifera_raw.tsv -o gene_universe_Porifera_no_aliens.tsv`  
`cut -f 1,14 gene_universe_Porifera_no_aliens.tsv > gene_universe_Porifera_goterms.tsv`

### Fair warning: disorganization to follow.  

**I need to plunk all of this down so that I don't get confused or forget, and I will add in annotations on Monday after I've turned in my draft.**  

Ok, the Porifera_gain_inter.tsv is a file that contains a the interproscan results from a filtered set of sequences. These sequences were formerly combined with sequences from all other internal sponge nodes also. That was how they were filtered and run through interproscan. I need the filtered set of sequence names from each node individually. So to make sure everything lines up, I need to follow these steps:  
1. get orthogroup names from the original files from R  
2. get sequence names for all sequences in those orthogroups  
3. use sequence names to prune interproscan results (for the sponge_specific OGs) so that they contain only results that correspond with that node - will only have to do this once per gene universe, and then it can be used for both gains and losses   
4. use pruned interproscan results to filter the sequence names so that they contain only the sequences that made it through the filtering process that came before interproscan (make sure the interproscan results have had aliens removed before this step, because if it happens after, they still won't match up)  


Right now, all of the topGO input files will have sponge aliens removed, but no other aliens until the rest of the indexing finishes.  


#### Gains at the Porifera node  
Description: Analysis of gains at the Porifera node
Ontology: BP
'weight01' algorithm with the 'fisher' test
1035 GO terms scored: 5 terms with p < 0.01
Annotation data:
    Annotated genes: 115696
    Significant genes: 274
    Min. no. of genes annotated to a GO: 1
    Nontrivial nodes: 106  

    GO.ID                                        Term Annotated Significant Expected classicFisher
1  GO:0070836                            caveola assembly       117          14     0.28       2.9e-30  
2  GO:0042981             regulation of apoptotic process       666          13     1.58       1.0e-17  
3  GO:0006464       cellular protein modification process       929           9     2.20       7.2e-10  
4  GO:0009116                nucleoside metabolic process       201           5     0.48       5.4e-08  
5  GO:0007160                        cell-matrix adhesion       268           3     0.63       0.00031  
6  GO:0000272            polysaccharide catabolic process        25           1     0.06       0.01203
7  GO:0007165                         signal transduction      3134           5     7.42       0.01773
8  GO:0006355 regulation of transcription, DNA-templat...       470           2     1.11       0.02195
9  GO:0043248                         proteasome assembly       199           1     0.47       0.09192
10 GO:0055085                     transmembrane transport       331           1     0.78       0.14827
11 GO:0055114                 oxidation-reduction process       571           1     1.35       0.24204
12 GO:0015074                             DNA integration      1115           1     2.64       0.41867
13 GO:1901564 organonitrogen compound metabolic proces...      2142          14     5.07       1.00000
14 GO:0044281            small molecule metabolic process       538           5     1.27       1.00000
15 GO:0043412                  macromolecule modification       946           9     2.24       1.00000
16 GO:0016070                       RNA metabolic process      1491           2     3.53       1.00000
17 GO:0050896                        response to stimulus      3449           5     8.17       1.00000
18 GO:0006351                transcription, DNA-templated       813           2     1.93       1.00000
19 GO:0009056                           catabolic process       448           1     1.06       1.00000
20 GO:0060255 regulation of macromolecule metabolic pr...       680           2     1.61       1.00000

#### Losses at the Porifera node  
Description: Analysis of loss at the Porifera node
Ontology: BP
'weight01' algorithm with the 'fisher' test
1035 GO terms scored: 5 terms with p < 0.01
Annotation data:
    Annotated genes: 115696
    Significant genes: 274
    Min. no. of genes annotated to a GO: 1
    Nontrivial nodes: 106

    GO.ID                                        Term Annotated Significant Expected classicFisher
1  GO:0070836                            caveola assembly       117          14     0.28       2.9e-30
2  GO:0042981             regulation of apoptotic process       666          13     1.58       1.0e-17
3  GO:0006464       cellular protein modification process       929           9     2.20       7.2e-10
4  GO:0009116                nucleoside metabolic process       201           5     0.48       5.4e-08
5  GO:0007160                        cell-matrix adhesion       268           3     0.63       0.00031
6  GO:0000272            polysaccharide catabolic process        25           1     0.06       0.01203
7  GO:0007165                         signal transduction      3134           5     7.42       0.01773
8  GO:0006355 regulation of transcription, DNA-templat...       470           2     1.11       0.02195
9  GO:0043248                         proteasome assembly       199           1     0.47       0.09192
10 GO:0055085                     transmembrane transport       331           1     0.78       0.14827
11 GO:0055114                 oxidation-reduction process       571           1     1.35       0.24204
12 GO:0015074                             DNA integration      1115           1     2.64       0.41867
13 GO:1901564 organonitrogen compound metabolic proces...      2142          14     5.07       1.00000
14 GO:0044281            small molecule metabolic process       538           5     1.27       1.00000
15 GO:0043412                  macromolecule modification       946           9     2.24       1.00000
16 GO:0016070                       RNA metabolic process      1491           2     3.53       1.00000
17 GO:0050896                        response to stimulus      3449           5     8.17       1.00000
18 GO:0006351                transcription, DNA-templated       813           2     1.93       1.00000
19 GO:0009056                           catabolic process       448           1     1.06       1.00000
20 GO:0060255 regulation of macromolecule metabolic pr...       680           2     1.61       1.00000

#### Gains at the Ctenophora node  
Description: Analysis of gains at the Cteno node
Ontology: BP
'weight01' algorithm with the 'fisher' test
998 GO terms scored: 6 terms with p < 0.01
Annotation data:
    Annotated genes: 106161
    Significant genes: 122
    Min. no. of genes annotated to a GO: 1
    Nontrivial nodes: 113

    GO.ID                                        Term Annotated Significant Expected classicFisher
1  GO:0042981             regulation of apoptotic process       149           6     0.17       5.1e-13
2  GO:0051260                 protein homooligomerization       196           4     0.23       8.0e-08
3  GO:0035556           intracellular signal transduction      1291           5     1.48       5.9e-06
4  GO:0006275               regulation of DNA replication         1           1     0.00       0.00021
5  GO:0019064 fusion of virus membrane with host plasm...         1           1     0.00       0.00021
6  GO:0060964       regulation of gene silencing by miRNA        27           1     0.03       0.00558
7  GO:0043087               regulation of GTPase activity       103           1     0.12       0.02113
8  GO:0070072 vacuolar proton-transporting V-type ATPa...       106           1     0.12       0.02174
9  GO:0006355 regulation of transcription, DNA-templat...       451           1     0.52       0.08942
10 GO:0007165                         signal transduction      3081           6     3.54       0.25375
11 GO:0010629      negative regulation of gene expression       141           1     0.16       1.00000
12 GO:0051052         regulation of DNA metabolic process         1           1     0.00       1.00000
13 GO:0044403                            symbiont process        30           1     0.03       1.00000
14 GO:0050896                        response to stimulus      3376           6     3.88       1.00000
15 GO:0016070                       RNA metabolic process      1457           1     1.67       1.00000
16 GO:0006351                transcription, DNA-templated       793           1     0.91       1.00000
17 GO:0060255 regulation of macromolecule metabolic pr...       651           3     0.75       1.00000
18 GO:0006259                       DNA metabolic process      1188           1     1.37       1.00000
19 GO:0043933 protein-containing complex subunit organ...       711           5     0.82       1.00000
20 GO:0009058                        biosynthetic process      1818           2     2.09       1.00000

#### Losses at the Ctenophora node  
Description: Analysis of losses at the Cteno node
Ontology: BP
'weight01' algorithm with the 'fisher' test
998 GO terms scored: 54 terms with p < 0.01
Annotation data:
    Annotated genes: 106161
    Significant genes: 10044
    Min. no. of genes annotated to a GO: 1
    Nontrivial nodes: 530

    GO.ID                                        Term Annotated Significant Expected classicFisher
1  GO:0006629                     lipid metabolic process      1065         204   100.76       < 1e-30
2  GO:0000160     phosphorelay signal transduction system        70          68     6.62       < 1e-30
3  GO:0006807         nitrogen compound metabolic process      4794         409   453.57       < 1e-30
4  GO:0070072 vacuolar proton-transporting V-type ATPa...       106          69    10.03       < 1e-30
5  GO:0035556           intracellular signal transduction      1291         207   122.14       < 1e-30
6  GO:0007165                         signal transduction      3081         359   291.50       < 1e-30
7  GO:0019915                               lipid storage        42          42     3.97       < 1e-30
8  GO:0006413                    translational initiation        42          42     3.97       < 1e-30
9  GO:0006450        regulation of translational fidelity        40          40     3.78       < 1e-30
10 GO:0071816 tail-anchored membrane protein insertion...        38          36     3.60       < 1e-30
11 GO:0051126     negative regulation of actin nucleation        28          28     2.65       < 1e-30
12 GO:0055114                 oxidation-reduction process       558          73    52.79       < 1e-30
13 GO:0015074                             DNA integration       829          82    78.43       < 1e-30
14 GO:0000272            polysaccharide catabolic process        24          22     2.27       < 1e-30
15 GO:0006412                                 translation       143          77    13.53       < 1e-30
16 GO:0044528 regulation of mitochondrial mRNA stabili...        18          17     1.70       1.4e-30
17 GO:0070836                            caveola assembly        14          14     1.32       2.4e-26
18 GO:0007009                plasma membrane organization        61          35     5.77       2.6e-26
19 GO:0042981             regulation of apoptotic process       149          31    14.10       2.9e-26
20 GO:0006284                        base-excision repair        63          22     5.96       1.5e-24



/mnt/lustre/macmaneslab/jlh1023/pipeline_dev/pipeline_scripts/no_aliens_interproscan.py -a /mnt/lustre/macmaneslab/jlh1023/chap3_2020/alien_indexing/sponge_indexing/all_sponge_aliens.txt -t gene_universe_Ctenophora_raw.tsv -o gene_universe_Ctenophora_noaliens.tsv
cut -f 1,14 gene_universe_Ctenophora_noaliens.tsv > gene_universe_Ctenophora_goterms.tsv
cut -f 1 gene_universe_Ctenophora_noaliens.tsv | sort > sorted_gene_universe_Ctenophora_seqnames.txt





### Results when sponges branch first  

copy over Ctenophora_gain_inter.tsv, Metazoa_present_all_inter.tsv, Porifera_gain_inter.tsv
interproscan cteno_rest, as above  
cat Metazoa_present_all_inter.tsv cteno_rest_inter.tsv Ctenophora_gain_inter.tsv > gene_universe_Ctenophora_raw.tsv  
/mnt/lustre/macmaneslab/jlh1023/pipeline_dev/pipeline_scripts/no_aliens_interproscan.py -a /mnt/lustre/macmaneslab/jlh1023/chap3_2020/alien_indexing/sponge_indexing/all_sponge_aliens.txt -t gene_universe_Ctenophora_raw.tsv -o gene_universe_Ctenophora_noaliens.tsv
/mnt/lustre/macmaneslab/jlh1023/pipeline_dev/pipeline_scripts/no_aliens_interproscan.py -a /mnt/lustre/macmaneslab/jlh1023/chap3_2020/alien_indexing/sponge_indexing/all_sponge_aliens.txt -t gene_universe_Porifera_inter_raw.tsv -o gene_universe_Porifera_noaliens.tsv
cut -f 1,14 gene_universe_Ctenophora_noaliens.tsv > gene_universe_Ctenophora_goterms.tsv
cut -f 1 gene_universe_Ctenophora_noaliens.tsv | sort > sorted_gene_universe_Ctenophora_seqnames.txt
cut -f 1,14 gene_universe_Porifera_noaliens.tsv > gene_universe_Porifera_goterms.tsv
cut -f 1 gene_universe_Porifera_noaliens.tsv | sort > sorted_gene_universe_Porifera_seqnames.txt
/mnt/lustre/macmaneslab/jlh1023/pipeline_dev/pipeline_scripts/pull_alignments.py -l Ctenophora_loss.txt -a /mnt/lustre/plachetzki/shared/metazoa_2020/above_80/OrthoFinder/Results_Oct19/Orthogroup_Sequences/ -n Ctenophora_loss_seqs/
/mnt/lustre/macmaneslab/jlh1023/pipeline_dev/pipeline_scripts/pull_alignments.py -l Porifera_loss.txt -a /mnt/lustre/plachetzki/shared/metazoa_2020/above_80/OrthoFinder/Results_Oct19/Orthogroup_Sequences/ -n Porifera_loss_seqs/
grep -h ">" Ctenophora_loss_seqs/*.fa | sed 's_>__' | sort > sorted_Ctenophora_loss_seqnames_raw.txt
comm -12 sorted_gene_universe_Ctenophora_seqnames.txt sorted_Ctenophora_loss_seqnames_raw.txt > Ctenophora_loss_filtered_seqnames.txt
grep -h ">" Porifera_loss_seqs/*.fa | sed 's_>__' | sort > sorted_Porifera_loss_seqnames_raw.txt
comm -12 sorted_gene_universe_Porifera_seqnames.txt sorted_Porifera_loss_seqnames_raw.txt > Porifera_loss_filtered_seqnames.txt
cut -f 1 Ctenophora_gain_inter.tsv > Ctenophora_gain_inter_seqnames.txt
cut -f 1 Porifera_gain_inter.tsv > Porifera_gain_inter_seqnames.txt








#### Are the sponges losing things that are sponge-specific in the first place?

If the sponges are losing things that all other animals have, that is one thing. If they are losing things that only other sponges had in the first place, that is kind of a different story. To figure this out, I'm going to do some simple comparisons. (I actually wrote a script to pull out orthogroups that were contained sponges but no other organisms called `clade_specific_ogs`, but then realized that I already have all of the node-specific gains just like I have all the node-specific losses, so I did it as demonstrated below instead.) I uploaded all of the sponge gains files to premise (`scp ~/Dropbox/Jenn_R/metazoa_ortho_dollo/all_114_presabs/gains_by_node/Verongiida.txt jlh1023@premise.sr.unh.edu:/mnt/oldhome/macmaneslab/jlh1023/chap3_2020/interesting_orthos/sponge_gains/`) and grepped out the OG lines into a separate file. The "-h" keeps grep from printing the file name before each match when it is searching multiple files.  
`grep "OG" -h *.txt >> sponge_specific_ogs.text`  

And now I can do some comparisons to the loss files I've already copied over. The loss files are individual and go in increasing OG number, but the file I just grepped together is mixed up, so I'll sort it first.  
`sort sponge_gains/sponge_specific_ogs.text > sorted_sponge_specific_ogs.txt`  

I'll do each of the sponge nodes I've got on premise so far (so, the 7 [not counting Porifera] that are listed above), and below I've listed the numbers of sponge-specific OGs that have been lost in each node. I'm popping them into a new directory `/mnt/lustre/macmaneslab/jlh1023/chap3_2020/interesting_orthos/specific_losses/` so that if I make a million of them, they are a bit more organized.    
`comm -12 Calcarea.txt sorted_sponge_specific_ogs.txt | wc -l`  
`comm -12 Calcarea.txt sorted_sponge_specific_ogs.txt > specific_losses/Calcarea_lost_sponge_ogs.txt`  

- Homoscleromorpha = 270  
- Hexactinellida = 1169  
- homo_calc = 0 (this one will not have a file in the specific_losses directory, because it would be empty)  
- Calcarea = 943 (fav number ftw!)  
- Haplosclerida = 700  
- Myxospongia = 976  
- por2 = 0 (this one will not have a file in the specific_losses directory, because it would be empty)  
