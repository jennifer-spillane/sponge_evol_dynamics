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

Based on those results, I now have lists of orthogroups that have been gained and lost at each internal node of the tree. Also, all the internal nodes have been named, so they are easier to identify. I'm going to focus on sponges first, and then maybe do some additional nodes to follow up. I want to run all of the sequences in these orthogroups through interproscan to figure out what they are. Then I'll do some GO analysis to see if anything is enriched. This is happening in this directory: /mnt/lustre/macmaneslab/jlh1023/chap3_2020/interesting_orthos/

The nodes I want to focus on first are all sponge ones:  
- Homoscleromorpha  
- Hexactinellida  
- homo+calc (renamed homo_calc when I'm working with it on premise)  
- Calcarea  
- Haplosclerida  
- Myxospongia  
- por2  
- Porifera  

The files that go with these nodes are here: /Users/jenniferlhill/Dropbox/Jenn_R/metazoa_ortho_dollo/all_114_presabs/losses_by_node_tip/  

I can just take one of these files, copy it onto premise, and use it to extract the necessary files from the orthofinder results directory with an old script I wrote to pull out interesting alignments. These are not alignments, but it works the same way on unaligned orthofinder output. The -l is the file that lists the OGs of interest, -a is a path to a directory containing the sequence (or alignment) files, and -n is a new directory in which to place all the right sequence files that match the OGs of interest.  
`/mnt/lustre/macmaneslab/jlh1023/pipeline_dev/pipeline_scripts/pull_alignments.py -l Homoscleromorpha.txt -a /mnt/lustre/plachetzki/shared/metazoa_2020/above_80/OrthoFinder/Results_Oct19/Orthogroup_Sequences/ -n /mnt/lustre/macmaneslab/jlh1023/chap3_2020/interesting_orthos/Homoscleromorpha_seqs`  

Once I have them all in a directory, I need to make sure there are no asterisks in any of the files, as interproscan will choke and die on them. I wrote a script ages ago that does this. Only argument necessary is the directory from the previous script.    
`/mnt/lustre/macmaneslab/jlh1023/pipeline_dev/pipeline_scripts/remove_asterisks.py Homoscleromorpha_seqs/`  

I like to go into the directory with all the seq files before I cat them together, to avoid weirdness with the paths, then I cat them together, and then I move it out to the parent directory where everything else is happening.  
    cd Homoscleromorpha_seqs/  
    cat *.fa > Homoscleromorpha_all.fa  
    mv Homoscleromorpha_all.fa ..  
    cd ..  

And then we can run interproscan.  
`interproscan -i Homoscleromorpha_all.fa -b Homoscleromorpha_inter -goterms -f TSV`
