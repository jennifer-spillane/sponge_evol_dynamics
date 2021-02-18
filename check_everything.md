## Every check we can think of

I want to be as sure as I can that whatever we end up finding (in the way of sponge gene family losses) is a real finding, and not an artifact of some aspect of the analysis. Things in this section are along those lines.


### What if sponge genomes and transcriptomes are less complete than other clades?

If sponge datasets are less complete, than what looks like loss could just be a crappy quality dataset, and we wouldn't be able to say that the losses are actually losses.

This is not much of an issue because we are staying zoomed out in terms of scale. We are talking about gene family (orthogroup) losses, and so an entire orthogroup would have to be missing from a sponge dataset in order to really show up as a loss in our analysis.

Also, we are looking at the last common ancestor node for each phylum, in order to get flagged as a loss, the gene family has to be missing from all of the organisms in that clade in our tree. For sponges, this is 24 chances for one of the datasets to be complete enough to contain the gene family in question, which is not nothing.

Also also, plenty of the sponges score quite high in terms of genic completeness as measured by BUSCO, and all of our organisms (except hexactinellids) have BUSCO scores above 80, so they are pretty complete. It is very unlikely that each dataset is missing the exact same things, so this is not much of a danger.


### Are sponge sequences not getting put into orthogroups in the same proportions as other organisms?

If sponge sequences (the proteins we put into orthofinder) are not getting placed into orthogroups in the same way as other organisms (maybe the sequences are more diverged and orthofinder cannot recognize them), it might look like the loss of a gene family when really that gene family is just off in an unclassified group by itself.

This seems pretty unlikely, as we are dealing with whole gene families here (whole orthogroups) that contain at least two sequences. It's possible that lots of these are single-species orthogroups, so we want to check the stats that orthofinder puts out to make sure that none of these things are out of whack compared to the rest of the organisms.  

I made some density plots of these stats (I got them from the orthofinder output file `Statistics_PerSpecies.tsv` and made into another file, "Statistics_PerSpecies.csv", and made the plots with the R script "prelim_stats.R"), and put the sponges together in one category and all the other organisms in another category ("sponge" and "not") so I could compare them, and it seems basically fine. These plots are saved as "orthogroup_number_plots.pdf" and "orthogroup_percentage_plots.pdf" in here: /Users/jenniferlhill/Desktop/Analyses/gain_loss.  

I haven't yet tested these density plots for significant differences, but visually the sponges are not showing distributions that are A. very different from the other organisms, or B. different in a direction that could prove problematic for us. If anything, it looks like they may have more gene families than some of the other organisms.  

*I may make one further split in the species, and separate out everything that isn't an animal into a third category. I could also test whether the distributions are significantly different from one another. Since I'm also not going to use all of these orthogroups in the analyses, I might also test the distributions using only the orthogroups I'm actually going to use, that contain enough of the species. Some of these numbers will obviously be meaningless at that point, but not all. Watch this space for any new developments.*  

Joe Ryan asked (and I realized I didn't know the answer right away) if the "species-specific orthogroups" contained "orthogroups" that only have one sequence in them, or if those count as "unclassified" proteins. Orthofinder definitely spits out lots of "orthogroups" and a ton of these are files that only contain one single sequence. I don't mean that they contain only sequences from one species, but just one single sequence at all. And I wasn't sure if these got counted as one of the categories that proteins could fall into in the stats, or if they were technically considered orthogroups and would be throwing off the numbers. If they counted as orthogroups, even though they only have one sequence, then the number of species-specific orthogroups would be higher, and the number of unclassified proteins would be artificially low. If these count as unclassified proteins, then it's fine and the numbers we are seeing in the stats are "correct" in that they are what we think they are.  

I thought about writing a script to test this that would remake all of the orthofinder stats, but as I was looking at the output files and planning my script, I realized I could just pick a test case and do some counting. In the `/mnt/lustre/plachetzki/shared/metazoa_2020/above_80/OrthoFinder/Results_Oct19/Orthogroup_Sequences/` directory there are fasta files for each "orthogroup" from 0 to 870554 in this case. I picked Xestospongia_testudinaria because it is the last species alphabetically, so I already knew the end point of its orthogroups (870554). Then I just had to find the very first time it was the only sequence in an "orthogroup". This turned out to be 8980 "orthogroups" back down the line (861575 is the first time there is a single sequence and it belongs to Xestospongia_testudinaria). Finally, this number is the same number listed in the Statistics_PerSpecies.tsv file in the orthofinder stats files, which means that orthofinder is counting these single sequence "orthogroups" not as orthogroups at all, but as unclassified genes, which is exactly what we want. *whew*  

So the numbers of the density plots hold up, so far as they go.  


### What if there are multiple genes on a single transcript?  

If, in our many transcriptomic datasets included in this study, there are transcripts that contain more than one gene (potential operons), orthofinder might not know where to put these (into the orthogroup for one gene or the other?).  


### What if all the interesting things we find are just contamination?  

It would be difficult for contamination to look like a loss, but absolutely possible that it could look like a gain, or keep us from detecting a loss at a given node. To make sure this doesn't happen, we are alien indexing each animal dataset in the study, using Joe Ryan's alien indexing program.   

I downloaded a zipped folder of alien indexing from here: https://github.com/josephryan/alien_index. Then I unzipped it and followed the instructions for installing without root privileges. I made a new directory `/mnt/lustre/macmaneslab/jlh1023/chap3_2020/alien_indexing` made the alien indexing database there. Then I copied all of the datasets to the alien indexing directory also. I kept datasets starting with a-i in that directory, moved ones starting with j-z to another one ("second_group"), moved ones that didn't need to be indexed (outgroups and datasets that are a part of the indexing process) to yet another one ("no_need_to_index"). Finally, I popped all the sponges (except for Amphimedon, which is in the database) into specific sponge directory. I did the indexing in various batches, so that I could have multiple jobs running on multiple nodes at the same time, but they all followed the pattern below.     
```bash  
for fs in $(ls *fa)
do
blastp -query $fs -db ai_db_all.fa -outfmt 6 -seg yes -evalue 0.001 -out $fs.blast
done
```  

Similarly, that basic loop is also how I will do the next step of the process, when I go through and identify all the alien sequences.  
```bash  
for blst in $(ls *blast)  
do  
alien_index --blast=$blst --alien_pattern=ALIEN_ > $blst.alien_index  
done  
```  
