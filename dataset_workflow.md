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

Based on those results, I now have lists of orthogroups that have been gained and lost at each internal node of the tree. Also, all the internal nodes have been named, so they are easier to identify.  

Here are just some numbers of gains and losses at various nodes.  
- Choanozoa: 4656 gained, 112 lost  
- Metazoa: 1912 gained, 196 lost  
- Ctenophora: 2767, 6180 lost  
- sponge+rest: 13283 gained, 46 lost  
- Porifera: 1317 gained, 2765 lost  
- Eumetazoa: 3741 gained, 73 lost  
- bilat2: 2599 gained, 380 lost  


I'm going to focus on sponges first, and then maybe do some additional nodes to follow up. I want to run all of the sequences in these orthogroups through interproscan to figure out what they are. Then I'll do some GO analysis to see if anything is enriched. This is happening in this directory: /mnt/lustre/macmaneslab/jlh1023/chap3_2020/interesting_orthos/. I've also included the number of OGs that were lost at these nodes.  

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


**Update 5-5-21:**  
I have now gotten rid of all of the alien sequences identified by the alien_index program for all of the species in the whole dataset. Occasionally, this leads to orthogroups having fewer than two sequences in them, so I've weeded these out. With all of the orthogroups that still have two or more seqs, I have run `usearch -cluster_fast` to narrow them down to centroid sequences for each orthogroup (see "check_everything.md" for details) and then choose the centroid sequence that is representative of the most sequences. If there are multiples, it will take the longest of these representative sequences. All of this is contained in the script `/mnt/lustre/macmaneslab/jlh1023/pipeline_dev/pipeline_scripts/clust_wrapper.py`.   

At the end of this filtering, I have a single fasta file with all the representative sequences for all the orthogroups called "rep_og_seq.fa" that contains 102,288 sequences.

Now, I can interproscan all of these representative sequences, so that I have one interproscan result per orthogroup. This "rescanning" is happening in this directory: /mnt/lustre/macmaneslab/jlh1023/chap3_2020/rescan. 



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

To pull these out, I'm going to start the same way that I did when I was interproscanning, and use the `pull_alignments.py` script. This will give me a directory with all of the othrogroup file in it. These fasta files contain all the sequences in that orthogroup. I will need to cat these sequences together, pull out just the sequence names, and remove the ">" symbol from the front so that they are just a list of sequence names. Then I can use a script I wrote called "prune_interpro_results.py" to select just the lines of interproscan results that correspond to the sequence names in the file from the orthogroups.   
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

*topGO results can be found in the file "topGO_results.md".*



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

**Update:**  
I'm doing the losses at the rest of the sponge nodes now, just looking for numbers.  
- democ2 = 362  
- democ3 = 501  
- Democlavia = 914  
- Demospongiidae = 61  
- Heteroscleromorpha = 173  
- Poecilosclerida = 576  


#### Is it more parsimonious for the ctenophores to branch first?  

What is the magnitude of the Ctenophore loss in each of the branching scenarios?
ctenos first = 6180 orthogroups lost  
sponges first = 18572 orthogroups lost  

**sponge first tree:**  
Metazoa gains = 14238
cteno_rest gains = 947  
cteno losses = 18572  
sponge losses = 1854  

comparison of the OGs gained in the cteno_rest node and Metazoa node with those lost in the Ctenophora node.  
`sort cteno_rest.txt > sorted_cteno_rest.txt`  
`sort Ctenophora_loss.txt > sorted_Ctenophora_loss.txt`  
`comm -12 sorted_cteno_rest.txt sorted_Ctenophora_loss.txt | less`  <- yields nothing at all. This makes sense, because the Dollo parsimony model would have merely inferred the gain somewhere else. Reality check.    
`sort Metazoa_gains.txt > sorted_Metazoa_gains.txt`  
`comm -12 sorted_Metazoa_gains.txt sorted_Ctenophora_loss.txt > metagain_ctenoloss.txt`  
This new file, "metagain_ctenoloss.txt" contains 13284 orthogroups, so ctenophores are losing a huge portion of the genes that have now been gained at the ancestral Metazoa node.

How do sponges do in this same scenario?  
`sort Porifera_loss.txt > sorted_Porifera_loss.txt`  
`comm -12 sorted_Metazoa_gains.txt sorted_Porifera_loss.txt > metagain_spongeloss.txt`  
This new file contains 1 orthogroup. Literally just the one.  

**cteno first tree:**  
Metazoa gains = 1913  
sponge_rest gains = 13283  
cteno losses = 6180  
sponge losses = 2765  

comparison of the OGs gained in the sponge_rest node and Metazoa node with those lost in the Ctenophora node. Procedure is the same as above.  
`comm -12 losses/sorted_Ctenophora_loss.txt sorted_Metazoa_gain.txt | less` <- yields nothing. Again, this makes sense for the Dollo parsimony approach.  
At the Porifera node, sponges lose 957 (in metagain_spongeloss.txt) of the OGs gained at the Metazoa node.


**How many orthogroups that are gained at the sponge+rest node in the Ctenophora-first tree get shifted over to the Metazoa node in the Porifera-first tree? And where do the other ones go?**

`comm -12 sorted_sponge_rest.txt ../sponge_first/sorted_Metazoa_gains.txt | wc -l`  
All of the gains that happen at the sponge+rest node in the cteno-first tree happen at the Metazoa node in the sponge-first tree  

`comm -12 sorted_Metazoa_gain.txt ../sponge_first/sorted_cteno_rest.txt | wc -l`  
They have 958 orthogroups in common - all of the ones from the cteno+rest node from the sponge-first tree  

This makes sense but I wanted to double check.   



#### How many losses are in common between the two trees?  

(from here: /mnt/lustre/macmaneslab/jlh1023/chap3_2020/interesting_orthos)
`comm -12 losses/sorted_Porifera_loss.txt ../sponge_first/sorted_Porifera_loss.txt > Porifera_common_losses.txt`
There are **1808** OGs that are lost at the Porifera node no matter which clade branches first. This is almost every loss from the sponge-first tree, and the majority of them from the cteno-first tree. I'm going to pull these out an have a look at them separately.  

`/mnt/lustre/macmaneslab/jlh1023/pipeline_dev/pipeline_scripts/pull_alignments.py -l Porifera_common_losses.txt -a /mnt/lustre/plachetzki/shared/metazoa_2020/above_80/OrthoFinder/Results_Oct19/Orthogroup_Sequences/ -n Porifera_common_losses_seqs`  

`grep -h ">" Porifera_common_losses_seqs/*fa | sed 's_>__' > Porifera_common_losses_seqnames.txt`  

`/mnt/lustre/macmaneslab/jlh1023/pipeline_dev/pipeline_scripts/prune_interpro_results.py -l Porifera_common_losses_seqnames.txt -t gene_universe_Porifera_no_aliens.tsv -o Porifera_common_losses_inter.tsv`  


Comparing the unique GO terms of the losses from the ctenopore node in both trees.
comm -12 Desktop/Analyses/gain_loss/unique_sf_ctenoloss_gos.txt Dropbox/Jenn_R/Gain_Loss/Cteno_First/Ctenos/cteno_loss_gos.txt | wc -l
    1682
comm -23 Desktop/Analyses/gain_loss/unique_sf_ctenoloss_gos.txt Dropbox/Jenn_R/Gain_Loss/Cteno_First/Ctenos/cteno_loss_gos.txt | wc -l
       0
comm -13 Desktop/Analyses/gain_loss/unique_sf_ctenoloss_gos.txt Dropbox/Jenn_R/Gain_Loss/Cteno_First/Ctenos/cteno_loss_gos.txt | wc -l
      29

Porifera-first lost GO terms are completely contained by Ctenophora-first lost GO terms.

#### Checking the overlap of GO terms between gains and losses at each node

I need to find out how many overlapping GO terms there are between the losses and the gains for both trees. I've already sort of done these comparisons when I was isolating the terms for the unique sets, but I just want the numbers this time.  

I'm going to use the "og_goterms.txt" files as a starting place, since they will have all the info I need and nothing I don't. But these files are lists of all unique GO terms in each orthogroup, catted together, so there are lots of repeats.
`sort Ctenophora_gain_og_goterms.txt | uniq > Ctenophora_gain_all_unique_terms.txt`  
`sort Porifera_gain_og_goterms.txt | uniq > Porifera_gain_all_unique_terms.txt`  
`sort losses/Ctenophora_loss_og_goterms.txt | uniq > losses/Ctenophora_loss_all_unique_terms.txt`  
`sort losses/Porifera_loss_og_goterms.txt | uniq > losses/Porifera_loss_all_unique_terms.txt`  
`sort ../sponge_first/Ctenophora_loss_og_goterms.txt | uniq > ../sponge_first/Ctenophora_loss_all_unique_terms.txt`  
`sort ../sponge_first/Porifera_loss_og_goterms.txt | uniq > ../sponge_first/Porifera_loss_all_unique_terms.txt`  

Now I can compare the gains and losses to one another.  
Ctenophora-first, sponges: file 1 = 329, file 2 = 562, overlap = 182   
`comm -12 Porifera_gain_all_unique_terms.txt losses/Porifera_loss_all_unique_terms.txt | wc -l`  

Ctenophora-first, ctenophores: file 1 = 271, file 2 = 1949, overlap = 238    
`comm -12 Ctenophora_gain_all_unique_terms.txt losses/Ctenophora_loss_all_unique_terms.txt | wc -l`  

Porifera-first, sponges: file 1 = 329, file 2 = 510, overlap = 174   
`comm -12 Porifera_gain_all_unique_terms.txt ../sponge_first/Porifera_loss_all_unique_terms.txt | wc -l`  

Porifera-first, ctenophores: file 1 = 271, file 2 = 1920, overlap = 238   
`comm -12 Ctenophora_gain_all_unique_terms.txt ../sponge_first/Ctenophora_loss_all_unique_terms.txt | wc -l`  

So, all of them have a bit of overlap, but we've excluded the overlap for the revigo analyses, so it will not affect the gains and losses that we are crafting the story around.  


#### Qualtifying GO terms for nodes in the sponge-first tree as well  

I need comparison numbers of GO terms for the nodes at the beginning of the sponge first tree, and I don't have them for the Metazoa node under that topology, or the Ctenophora+ParaHoxozoa node. I think I have all the right things interproscanned already, but I need to figure out what combination of things in the ctenofirst tree I need to do this correctly in the sponge first tree.  




#### Characterizing gains and losses at focal nodes (cteno first tree)  

I have put lists of GO terms for the Porifera node into revigo (http://revigo.irb.hr/) which eliminates duplicates and helps with listing and visualizing the terms. I put in the GO terms for Porifera gains, a different one for Porifera losses, and a third one for Porifera losses that also overlap with Porifera losses in the sponge-first tree. These are the losses that no one will be able to dispute, so they could be important. I'm not sure which of these GO terms I should look into first, so I am just going to take a couple of top hits from the gains to begin with, and trace them back to their orthogroups. That way we can make trees from the orthogroups and get a clear idea of what they are in a more specific way than the very general terms that GO stuff annotates with.  

I'm going to start with a molecular function one, GO:0005201 - extracellular matrix structural constituent. It's a decently high hit in the gains, but it also shows up in the losses, so I want to see a little more nuance with it, which I'm hoping I'll get by investigating the OGs that go with it.  

First, I need to search for the GO term in the interproscan results.  
`grep "GO:0005201" Porifera_gain_inter.tsv | less`  
There are 59 lines of results here. I'm just going to take the sequence name of the first one and search for it in the orthogroup files.  
`grep "Leuconia_nivea_36217" Porifera_gain_seqs/*.fa`
This yields just one instance (which makes sense) "Porifera_gain_seqs/OG0011214.fa" so that worked great!  
I did the same thing for the last entry in that first grep result, "Mycale_grandis_48606" and it gave me a different orthogroup, "Porifera_gain_seqs/OG0012807.fa" so there could definitely be multiple that have the same GO term associated with them. Because of this, I'm going to take a slightly different approach to finding the right OGs. I'll save the results of that first grep to a file, and then pare it down to just the sequence names. Then I can use one of the scripts I've already written to pull out the OGs associated with those sequences.  

I looked for the same GO term in the Porifera losses because it is also listed there, and got a different OG back, which makes sense.  

**Update:** The extra-good news is, I already wrote this script! I wrote it originally to get info about alien sequences in the orthogroups, but it works for any list of sequence names that you want more orthogroup info about. And it's already been tested and optimized, so it should work well.  I'm going to start with one that popped up as significantly enriched as a gain at the sponge node, GO:0070836.
`grep "GO:0070836" Porifera_gain_inter.tsv | cut -f 1 > GO_0070836.txt`  

Here, -l is the list file I just made, -l is a directory containing every orthogroup sponges might have, -o is the output file with just a list of orthogroups, and -c is a tab separated file containing the names of the orthogroups with the number of sequences in them that were in the original list (this last one won't be super useful, I don't think, but will not hurt anything).  
`/mnt/lustre/macmaneslab/jlh1023/pipeline_dev/pipeline_scripts/og_names_from_seqs.py -l GO_0070836.txt -d all_sponge_seqs/ -o GO_0070836_og_names.txt -c GO_0070836_og_counts.tsv`  

Takes a minute to run through all of the files, but works great!

**Metazoa gains:**  
- GO:0017147 - Wnt protein binding - OG0000067  
- GO:0005911 - cell-cell junction - OG0001805   
- GO:0005615 - extracellular space - OG0000110, OG0002109, OG0004814, OG0032101, OG0000051, OG0000203  
- GO:0008283 - cell population proliferation - OG0000016   
- GO:0007155 - cell adhesion - OG0003495, OG0000821, OG0002452, OG0008099, OG0006772, OG0000696, OG0063416, OG0045604, OG0003668, OG0000009, OG0029462, OG0009221, OG0069489, OG0018438, OG0000345, OG0000205, OG0008154  
    - GO:0007160 - cell matrix adhesion  
    - GO:0007156 - homophilic cell adhesion via plasma membrane adhesion molecules  
    - GO:0098609 - cell-cell adhesion  
- GO:0015026 - coreceptor activity - OG0005525, OG0000009

I'm going to script this so that it doesn't take me a million years.  

```bash  
#! /bin/bash   
for term in GO:0008283 GO:0007155 GO:0015026  
do  
grep $term Metazoa_gain_inter.tsv | cut -f 1 > goterm_orthogroups/$term.txt
/mnt/lustre/macmaneslab/jlh1023/pipeline_dev/pipeline_scripts/og_names_from_seqs.py -l goterm_orthogroups/$term.txt -d Metazoa_gain_seqs/ -o goterm_orthogroups/$term_og_names.txt -c goterm_orthogroups/$term.tsv   
done   
```  

This script does not successfully make the names.txt file, but it's not the more vital one anyway, so I'm just going to go with it for the sake of time. I'll change it to use a different interproscan results file to draw from, and different GO terms, and do it for the other nodes, listed below.  

**Porifera+ParaHoxozoa gains:**  
- GO:0009584 - detection of visible light - OG0009705, OG0042173, OG0013200  
- GO:0010506 - regulation of autophagy - OG0048545  
- GO:0007568 - aging - OG0002497  
- GO:0099106 - ion channel regulator activity - OG0008591  

```bash  
#! /bin/bash   
for term in GO:0009584 GO:0010506 GO:0007568 GO:0099106  
do  
grep $term sponge_rest_inter.tsv | cut -f 1 > goterm_orthogroups/$term.txt  
/mnt/lustre/macmaneslab/jlh1023/pipeline_dev/pipeline_scripts/og_names_from_seqs.py -l goterm_orthogroups/$term.txt -d sponge_rest_seqs -o goterm_orthogroups/$term_og_names.txt -c goterm_orthogroups/$term.tsv   
done   
```  

**Porifera gains:**  
- GO:0070836 - caveola assembly - OG0010034    
- GO:0075509 - endocytosis involved in viral entry into host cell - OG0091630  
- GO:0051470 - ectoine transport - OG0046989  
- GO:0033294 - ectoine binding - OG0046989  


```bash  
#! /bin/bash   
for term in GO:0070836 GO:0075509 GO:0051470 GO:0033294  
do  
grep $term Porifera_gain_inter.tsv | cut -f 1 > goterm_orthogroups/$term.txt  
/mnt/lustre/macmaneslab/jlh1023/pipeline_dev/pipeline_scripts/og_names_from_seqs.py -l goterm_orthogroups/$term.txt -d Porifera_gain_seqs -o goterm_orthogroups/$term_og_names.txt -c goterm_orthogroups/$term.tsv   
done   
```


**Porifera losses:**  
- GO:0000278 - mitotic cell cycle - OG0007776  
- GO:0006915 - apoptotic process - OG0020094  
- GO:0000902 - cell morphogenesis - OG0017665  
- GO:0031012 - extracellular matrix - OG0078217, OG0034281, OG0023295  
- GO:0005540 - hyaluronic acid binding - OG0015041
- GO:0016192 - vesicle mediated transport - OG0025571, OG0012351  
- GO:0043113 - receptor clustering - OG0032215  
- GO:0003774 - motor activity - OG0026955, OG0046220, OG0028521, OG0034180, OG0026770

```bash  
#! /bin/bash   
for term in GO:0000278 GO:0006915 GO:0000902 GO:0031012 GO:0005540  
do  
grep $term losses/Porifera_inter.tsv | cut -f 1 > goterm_orthogroups/$term.txt  
/mnt/lustre/macmaneslab/jlh1023/pipeline_dev/pipeline_scripts/og_names_from_seqs.py -l goterm_orthogroups/$term.txt -d losses/Porifera_seqs -o goterm_orthogroups/$term_og_names.txt -c goterm_orthogroups/$term.tsv   
done   
```

Accidentally left off the last three when I first ran this, so now I've corrected that.  

**Ctenophora gains:**  
- GO:0090307 - mitotic spindle assembly - OG0026271  
- GO:0030131 - clathrin adaptor complex - OG0037883  
- GO:0051033 - RNA transmembrane transporter activity - OG0037656, OG0046401  

```bash  
#! /bin/bash   
for term in GO:0090307 GO:0030131 GO:0051033  
do  
grep $term Ctenophora_inter.tsv | cut -f 1 > goterm_orthogroups/$term.txt  
/mnt/lustre/macmaneslab/jlh1023/pipeline_dev/pipeline_scripts/og_names_from_seqs.py -l goterm_orthogroups/$term.txt -d Ctenophora_seqs -o goterm_orthogroups/$term_og_names.txt -c goterm_orthogroups/$term.tsv   
done   
```


**Ctenophora losses:**  
- GO:0007586 - digestion - OG0006549  
- GO:1904970 - brush border assembly - OG0005896  
- GO:0043560 - insulin receptor substrate binding - OG0001466  

```bash  
#! /bin/bash   
for term in GO:0007586 GO:1904970 GO:0043560  
do  
grep $term Ctenophora_loss_inter.tsv | cut -f 1 > goterm_orthogroups/$term.txt  
/mnt/lustre/macmaneslab/jlh1023/pipeline_dev/pipeline_scripts/og_names_from_seqs.py -l goterm_orthogroups/$term.txt -d losses/Ctenophora_loss_seqs -o goterm_orthogroups/$term_og_names.txt -c goterm_orthogroups/$term.tsv   
done   
```


I need to find all the GO terms for Metazoa gains and the gains at the sponge+rest node also. Sponge+rest is pretty easy, as I have done all of the steps before for different nodes, and it has a ready-to-go interproscan results file.  
`cut -f 14 sponge_rest_inter.tsv | sed 's_|_\n_g' | sed '/^$/d' | sort | uniq > sponge_rest_unique_goterms.txt`  

For the Metazoa node, I had to start back at the point of orthogroup names, and pulled the relevant interproscan results out based on the sequences in those orthogroups.  
`/mnt/lustre/macmaneslab/jlh1023/pipeline_dev/pipeline_scripts/pull_alignments.py -l Metazoa_gain.txt -a /mnt/lustre/plachetzki/shared/metazoa_2020/above_80/OrthoFinder/Results_Oct19/Orthogroup_Sequences/ -n Metazoa_gain_seqs/`
`grep -h ">" Metazoa_gain_seqs/*fa | sed 's_>__' > Metazoa_gain_seq_names.txt`
`/mnt/lustre/macmaneslab/jlh1023/pipeline_dev/pipeline_scripts/prune_interpro_results.py -l Metazoa_gain_seq_names.txt -t Metazoa_present_all_inter.tsv -o Metazoa_gain_inter.tsv`
`cut -f 14 Metazoa_gain_inter.tsv | sed 's_|_\n_g' | sed '/^$/d' | sort | uniq > Metazoa_gain_unique_goterms.txt`

I also want to see how many of these two lists overlap with one another (GO term-wise, they won't overlap at all on the level of orthogroup).  
sponge_rest_unique_goterms.txt = 1416 unique GO terms   
Metazoa_gain_unique_goterms.txt = 708 unique GO terms  
`comm -12 Metazoa_gain_unique_goterms.txt sponge_rest_unique_goterms.txt | wc -l`  
442 overlapping GO terms  

I also made a file that has all of the unique GO terms from sponge+rest, without the overlapping ones with Metazoa.  
`comm -13 Metazoa_gain_unique_goterms.txt sponge_rest_unique_goterms.txt > sponge_rest_nomet_unique_goterms.txt`  

I ran the raw Metazoa gains list through revigo (small setting) and the sponge+rest (or Porifera+ParaHoxozoa) gains through also (tiny setting) to get their GO info also.  

**Update**  
I've realized I need to exclude GO terms that overlap with the losses in these two nodes also. The sponge+rest node won't be a huge deal, but the Metazoa losses have never been interproscanned, so I'm going to get that started now so that it can run while I'm working on other edits. I made a file /mnt/lustre/macmaneslab/jlh1023/chap3_2020/interesting_orthos/losses/Metazoa_loss.txt of all the orthogroups that have been lost at Metazoa. It's not that many of them, so this should go quickly.  
`/mnt/lustre/macmaneslab/jlh1023/pipeline_dev/pipeline_scripts/pull_alignments.py -l Metazoa_loss.txt -a /mnt/lustre/plachetzki/shared/metazoa_2020/above_80/OrthoFinder/Results_Oct19/Orthogroup_Sequences/ -n Metazoa_loss_seqs/`  
Then I ran the uclust script (above) on these fasta files from within the directory, catted all the clustered/filtered fastas together, and called it "Metazoa_loss_filtered.fa" in the losses directory. Interproscan command was just like all the others.  

For the sponge+rest, I'll need to pull out these losses from one of the gene universe files. Everything present at the Metazoa node will include things that get lost at the sponge+rest node, so that should be a safe interproscan file to draw from.  
First I'll need the orthogroups, just like before. They are in a file here: /mnt/lustre/macmaneslab/jlh1023/chap3_2020/interesting_orthos/losses/  
`/mnt/lustre/macmaneslab/jlh1023/pipeline_dev/pipeline_scripts/pull_alignments.py -l sponge_rest_loss.txt -a /mnt/lustre/plachetzki/shared/metazoa_2020/above_80/OrthoFinder/Results_Oct19/Orthogroup_Sequences/ -n sponge_rest_loss_seqs/`  
These I don't need to filter in the same way, since all the sequences have been filtered already, just as part of a different procedure. So when I pull the interproscan results that go with these, they will be filtered results anyway.  
`grep -h ">" sponge_rest_loss_seqs/*fa | sed 's_>__' > sponge_rest_loss_seq_names.txt`  
`/mnt/lustre/macmaneslab/jlh1023/pipeline_dev/pipeline_scripts/prune_interpro_results.py -l sponge_rest_loss_seq_names.txt -t ../Metazoa_present_all_inter.tsv -o sponge_rest_loss_inter.tsv`  
`cut -f 14 sponge_rest_loss_inter.tsv | sed 's_|_\n_g' | sed '/^$/d' | sort | uniq > sponge_rest_loss_unique_goterms.txt`  

I also don't think I need to exclude the GO terms that the Metazoa gains and the sponge_rest gains have in common. It seems pretty reasonable that both those node would be adding the same sorts of gene families. So I'm just going to exclude the losses from both of those nodes, and then do the revigo analyses on those files.  

`comm -23 sponge_rest_unique_goterms.txt losses/sponge_rest_loss_unique_goterms.txt > sponge_rest_noloss_unique_goterms.txt`  

It's not a huge difference, because the losses are a pretty tiny file, but I feel better about this analysis now. Just going to quantify all the overlap so I can make a figure.  

Ctenophora-first, sponge_rest: file 1 = 1416, file 2 = 22, overlap = 22   
`comm -12 sponge_rest_unique_goterms.txt losses/sponge_rest_loss_unique_goterms.txt | wc -l`  



For Metazoa: (in the losses directory)  
`cut -f 14 Metazoa_loss_inter.tsv | sed 's_|_\n_g' | sed '/^$/d' | sort | uniq > Metazoa_loss_unique_goterms.txt`  

 (in the interesting_orthos directory)  
 `comm -23 Metazoa_gain_unique_goterms.txt losses/Metazoa_loss_unique_goterms.txt > Metazoa_gain_noloss_unique_goterms.txt`  

 Ctenophora-first, metazoa: file 1 = 708, file 2 = 70, overlap = 59    
 `comm -12 Metazoa_gain_unique_goterms.txt losses/Metazoa_loss_unique_goterms.txt | wc -l`



**For the sponge-first tree:**  

I need to find numbers of GO terms for the gains and losses at Metazoa and Ctenophora+ParaHoxozoa.  

The losses at Metazoa are identical to those in the cteno-first tree, so that means there are 70 GO terms. We can just pop that in an move on.  

For the gains at Metazoa, I just need to find orthogroup sets in the cteno-first tree that contain all of the orthogroups in the Metazoa gains file. Then I can use that combination to pull the interproscan results for the Metazoa gains.  
From in the sponge_first directory:  
`wc -l sorted_Metazoa_gains.txt`  14238  
`comm -12 sorted_Metazoa_gains.txt ../interesting_orthos/sorted_Metazoa_gain.txt | wc -l`  956  
`comm -12 sorted_Metazoa_gains.txt ../interesting_orthos/sorted_sponge_rest.txt | wc -l`  13283  

Ok, so these together make up all of the orthogroups in the Metazoa gains for the sponge-first tree. So I can combine the interproscan results for these sets of orthogroups and use the Metazoa gains files to pull relevant results.  
`cat ../interesting_orthos/Metazoa_gain_inter.tsv ../interesting_orthos/sponge_rest_inter.tsv > cf_met_porpara_gains_inter.tsv`  


For the gains at the cteno+rest node, we can do a similar process. I noticed earlier that there were 958 orthogroups that were in the Metazoa gains for the cteno-first tree, that were not in the Metazoa gains for the sponge-first tree, so we'll look at those first.  
`wc -l  sorted_cteno_rest.txt`  958 -  same number  
`comm -12 sorted_cteno_rest.txt ../interesting_orthos/sorted_Metazoa_gain.txt | wc -l`  958 - this is excellent, will make things much easier.  
So now I can just use the Metazoa gains from the cteno-first tree by itself to pull the right interproscan results for the cteno+rest gains in the sponge-first tree.   

*Actually, I think I've already done this one. I have a file of all of these unique GO terms already, so I'm just going to leave this one here.*   
`wc -l cteno_rest_unique_goterms.txt`  185 go terms  


For the losses at the cteno_rest node:  
`wc -l sorted_cteno_rest_loss.txt`  891  
`comm -12 sorted_cteno_rest_loss.txt ../interesting_orthos/losses/sorted_Ctenophora_loss.txt | wc -l`  891  
When I compared them to the losses at Ctenophora in the other tree, they overlap completely, so I can use those interproscan results to pull the right things for the losses at this node.  


Actually making those files from the interproscan results:  
`/mnt/lustre/macmaneslab/jlh1023/pipeline_dev/pipeline_scripts/pull_alignments.py -l cteno_rest_loss.txt -a /mnt/lustre/plachetzki/shared/metazoa_2020/above_80/OrthoFinder/Results_Oct19/Orthogroup_Sequences/ -n cteno_rest_loss_seqs/`  
`/mnt/lustre/macmaneslab/jlh1023/pipeline_dev/pipeline_scripts/pull_alignments.py -l Metazoa_gains.txt -a /mnt/lustre/plachetzki/shared/metazoa_2020/above_80/OrthoFinder/Results_Oct19/Orthogroup_Sequences/ -n Metazoa_gains_seqs/`  


`grep -h ">" cteno_rest_loss_seqs/*fa | sed 's_>__' > cteno_rest_loss_seq_names.txt`  
`/mnt/lustre/macmaneslab/jlh1023/pipeline_dev/pipeline_scripts/prune_interpro_results.py -l cteno_rest_loss_seq_names.txt -t ../interesting_orthos/Ctenophora_loss_inter.tsv -o cteno_rest_loss_inter.tsv`  
`cut -f 14 cteno_rest_loss_inter.tsv | sed 's_|_\n_g' | sed '/^$/d' | sort | uniq > cteno_rest_loss_unique_goterms.txt`  

`grep -h ">" Metazoa_gains_seqs/*fa | sed 's_>__' > Metazoa_gains_seq_names.txt`  
`/mnt/lustre/macmaneslab/jlh1023/pipeline_dev/pipeline_scripts/prune_interpro_results.py -l Metazoa_gains_seq_names.txt -t cf_met_porpara_gains_inter.tsv -o Metazoa_gains_inter.tsv`  
`cut -f 14 Metazoa_gains_inter.tsv | sed 's_|_\n_g' | sed '/^$/d' | sort | uniq > Metazoa_gains_unique_goterms.txt`  










#### Characterizing gains and losses at the cteno and sponge nodes (sponge-first tree)  

I needed the actual GO terms associated with losses at these two nodes for this tree (I just had the sequence names before).  
`/mnt/lustre/macmaneslab/jlh1023/pipeline_dev/pipeline_scripts/prune_interpro_results.py -l Ctenophora_loss_filtered_seqnames.txt -t gene_universe_Ctenophora_goterms.tsv -o Ctenophora_loss_goterms.tsv`  
`/mnt/lustre/macmaneslab/jlh1023/pipeline_dev/pipeline_scripts/prune_interpro_results.py -l Porifera_loss_filtered_seqnames.txt -t gene_universe_Porifera_goterms.tsv -o Porifera_loss_goterms.tsv`  

Then I downloaded these resulting files. I don't need to download "Porifera_gain_inter.tsv" and "Ctenophora_gain_inter.tsv" because they are identical to the ones in the other tree. Again, because the gains are based on the nodes below them, not on the nodes above. I opened them in BBEdit, isolated the GO terms, and popped them into revigo.  





#### I need lists of all the GO terms associated with each orthogroup  

From inside this directory: /mnt/lustre/macmaneslab/jlh1023/chap3_2020/interesting_orthos/Metazoa_present_seqs/  

This is what it looks like for an individual one:  
`grep ">" OG0000000.fa.fasta | sed 's_>__' > OG0000000.fa.fasta.seqs.txt`
`/mnt/lustre/macmaneslab/jlh1023/pipeline_dev/pipeline_scripts/prune_interpro_results.py -l OG0000000.fa.fasta.seqs.txt -t /mnt/lustre/macmaneslab/jlh1023/chap3_2020/interesting_orthos/Metazoa_present_all_inter.tsv -o OG0000000.fa.fasta.goterms.tsv`
`cut -f 14 OG0000000.fa.fasta.goterms.tsv | sed 's_|_\n_g' | sed '/^$/d' | sort | uniq > OG0000000.fa.fasta.goterms.txt`

This is what it looks like for lots of files at once:  
```bash  
#! /bin/bash   
for file in $(ls *fasta)  
do  
grep ">" $file | sed 's_>__' > $file.seqs.txt  
/mnt/lustre/macmaneslab/jlh1023/pipeline_dev/pipeline_scripts/prune_interpro_results.py -l $file.seqs.txt -t /mnt/lustre/macmaneslab/jlh1023/chap3_2020/interesting_orthos/Metazoa_present_all_inter.tsv -o $file.goterms.tsv  
cut -f 14 $file.goterms.tsv | sed 's_|_\n_g' | sed '/^$/d' | sort | uniq > $file.goterms.txt  
done   
```  

This was going too slowly, so I had to split it up into multiple jobs for Metazoa presences and Ctenophora losses (sponge-first), but it worked the same way.  

Then I catted the files together from inside the directory where they were being made, like this:  
`cat *terms.txt >> ../Porifera_loss_og_goterms.txt`  

And then I could download them and pop them into the R script.  




#### Word clouds  

```bash  
#! /bin/bash   
for file in $(ls *terms.tsv)  
do  
cut -f 6 $file | sed '/^$/d' | sort | uniq > $file.uniqdes.txt   
done   
```  
