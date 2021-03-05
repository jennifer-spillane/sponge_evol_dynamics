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
echo "now working on $fs"
blastp -query $fs -db ai_db_all -outfmt 6 -seg yes -evalue 0.001 -out $fs.blast
done
```  

Similarly, that basic loop is also how I will do the next step of the process, when I go through and identify all the alien sequences.  
```bash  
for blst in $(ls *blast)  
do  
alien_index --blast=$blst --alien_pattern=ALIEN_ > $blst.alien_index  
done  
```  

I've now (2-18-21) done this for all of the sponges, and am just waiting for all of the other organisms to run (minus the ones that were included in the database and the outgroups). Meanwhile, I want to figure out how to pull out the names of orthogroups that contain these sequences. Then I will be able to compare them with the orthogroups that are present/absent or gained/lost at each node, and see if these results are being affected by aliens. Again, it is more likely that contamination would look like a gain or like a presence where there really isn't one.  

I wrote a script (/mnt/lustre/macmaneslab/jlh1023/pipeline_dev/pipeline_scripts/og_names_from_seqs.py) that accepts a list of sequences (Genus_species_number, in this case), and pulls out the names of the OGs that contain those seqs. It also produces a tab-delimited file containing the number of alien seqs each OG contains.

I need to give it a text file that is a list of all the alien sequences in a particular dataset (-l argument), and I can get that like this:  
`cut -f 1 Aphrocallistes_vastus.blast.alien_index | grep -v "ID" > Aphrocallistes_vastus_alienseqs.txt`  

Then I need a path to a directory containing fasta files of orthogroups (-d argument). For sponges, I will use a directory of all the orthogroups they might possibly have (the same one I am running through interproscan to use as a "gene universe" for GO term analysis). This consists of the OGs from a number of files from the Dollo parsimony R script: presences at Metazoa (Metazoa_present_seqs), gains at sponge+rest (sponge_rest_seqs), gains at each internal sponge node, including the ancestral one (sponge_specific_seqs). These all exist in separate lists and directories, but I will combine them before running this script (`cp Metazoa_present_seqs/*.fa all_sponge_seqs/`, etc.). Any that are still in list form (have not had corresponding fasta files pulled from the orthofinder results), I can grab using my pull_alignments.py script (don't worry about the name, it's more versatile than that).

The last two arguments (-o, and -c) are for output files: -o for a file that has each alien sequence and the orthogroup it belongs to (if any), and -c for a file that has each orthogroup that contains alien sequences and how many it contains.  

I'm running this from inside this directory `/mnt/lustre/macmaneslab/jlh1023/chap3_2020/alien_indexing/sponge_indexing`, so paths might be relative to there, at least for the sponge ones.  
`/mnt/lustre/macmaneslab/jlh1023/pipeline_dev/pipeline_scripts/og_names_from_seqs.py -l Aphrocallistes_vastus_alienseqs.txt -d /mnt/lustre/macmaneslab/jlh1023/chap3_2020/interesting_orthos/all_sponge_seqs/ -o Aphrocallistes_vastus_alienortho.tsv -c Aphrocallistes_vastus_orthocounts.tsv`   

This script works great, but takes a while to run (unsurprising, considering the number of files and the nested for loops), so I'll split the sponges up into the same groups they were in when I indexed them in the first place. **update:** This was taking so long. I was having it go through all of the files for every entry in the alienseqs textfile, and that was a totally unreasonable thing to expect it to do in anything under a million years. I changed it around so that it's only looping through all of those files once, and now it runs in a tiny fraction of the time! This new version was originally called "og_names_from_seqs2", but the other is now obsolete, so I'm getting rid of that one and renaming this one without the 2. Now I can just run through them all, no problem.  

`cut -f 1 Sycon_ciliatum.blast.alien_index | grep -v "ID" > Sycon_ciliatum_alienseqs.txt
/mnt/lustre/macmaneslab/jlh1023/pipeline_dev/pipeline_scripts/og_names_from_seqs.py -l Sycon_ciliatum_alienseqs.txt -d /mnt/lustre/macmaneslab/jlh1023/chap3_2020/interesting_orthos/all_sponge_seqs/ -o Sycon_ciliatum_alienortho.tsv -c Sycon_ciliatum_orthocounts.tsv`


**More updates:** This is great info to have, but I also just want a simple script that will remove problematic sequences from the interproscan results (obviously all of this is really meant to be done at the beginning of a study before you run a lot of the analyses, but it just doensn't always go down that way). So I wrote one here: `/mnt/lustre/macmaneslab/jlh1023/pipeline_dev/pipeline_scripts/no_aliens_interproscan.py` that takes a list of alien (or otherwise problematic) sequence names and an interproscan output tsv file and outputs a new tsv file without all of the results from the sequences named in the list.  
`/mnt/lustre/macmaneslab/jlh1023/pipeline_dev/pipeline_scripts/no_aliens_interproscan.py -a test_aliens.txt -t test.tsv -o test_done.tsv`  



### Do genes in the same orthogroup get annotated with different GO terms?  

I've been relating GO annotations back to the orthogroups that contain the sequences that were annotated. We want to know now if all the sequences in a given orthogroup will always be annotated with the same GO term. I think the early sets of genes I interproscanned might be useful for this, since they contained whole orthogroups of sequences instead of the filtered ones I used later.  







### Does the uclustering step cluster all or most of the orthogroups in a consistent way?

Since we end up testing the clustered sequences that were run through interproscan in topGO, I want to know how consistently the uclust program is clustering the sequences in orthogroups. Theoretically, there could be one orthogroup that lots of sponges have, that has not diverged that much over the millennia, and that gets clustered into just a few centroid sequences. Then there could be another that has the same number of sequences as the first originally, but diverged more, and so gets clustered into more sequences and ends up with more entries in the interproscan results. This could potentially bias those results into thinking that the more divergent orthogroup is enriched, simply because it has more entries in the interproscan results file. So I'm going to find out how linear the relationship is between original number of sequences in an orthogroup, and number of centroid sequences after uclust does its work.  

I wrote a script that pulls out the number of sequences from fasta files in a directory and records them in a tsv. I did it on the Porifera loss sequences to check things out and it looks very linear, but I'm going to do it on the Metazoa present seqs because it's a nice large dataset for testing.   
`/mnt/lustre/macmaneslab/jlh1023/pipeline_dev/pipeline_scripts/count_seqs.py -d Metazoa_present_seqs/ -o Metazoa_present_counts.tsv`  

This gives me a tsv with all the file names and counts of how many sequences they have.  
`head Metazoa_present_counts.tsv`  
OG0003937.fa.fasta	126  
OG0059868.fa	4  
OG0103678.fa	2  
OG0004795.fa	152  
OG0023117.fa.fasta	6  
OG0009957.fa.fasta	25  
OG0008192.fa.fasta	42  
OG0007861.fa	65  
OG0008988.fa.fasta	36  
OG0000542.fa.fasta	295  

From here, I'll download it, pop it into bbedit, and remove the file extensions. I'll also add a category at the beginning (followed by a tab) that is either "original" (for the .fa files) or "centroid" (for the .fa.fasta files). Then I import it into excel, do a quick pivot table, and pop it into R for plotting. A little roundabout maybe, but it works and is pretty quick. I tagged this one onto the end of the exploratory plotting R script I already had going for this project, "prelim_stats.R".  

Looking super super linear, so I think we are mostly good. If it clusters in a proportional way each time, our results will be proportional to the results we would have gotten if we had interproscanned the whole dataset.  
