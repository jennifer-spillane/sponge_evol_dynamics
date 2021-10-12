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

**Update, 4-29-21:** I want to remove the rest of the alien seqs that I found earlier with the blasting in all the other organisms. So I did the second step, just like I did for sponges, above (the alien_index command in the loop) for each of the four directories that the species are currently in (/mnt/lustre/macmaneslab/jlh1023/chap3_2020/alien_indexing, and within this one, "second_group", "third_group", and "fourth_group"). Now I need to remove the alien seqs found from the orthogroups. Since the orthogroups are just fasta files, I should be able to do this with Joe's removal command instead of writing my own. In a perfect world, we would do this before running orthofinder, but that is not the world we live in, and this should work fine. I'll run the command on all of the orthogroups using a concattenated file of all the alien seqs.  

The alien_index files have a lot of other stuff in their first line, so I'll need that once at the top, but then to get rid of that stuff before I stick all the rest together.
`grep "ID" Craspedacusta_sowerbyi.fa.blast.alien_index > all_alien_seqs.txt`  
`grep -h -v "ID" *.blast.alien_index >> all_alien_seqs.txt`  

Then I just did this in each of the other directories containing these files, and I end up with a file with all the alien seqs in it. Now I can remove them from the orthogroups. I'm going to do this directly in the directory that contains the orthogroups (/mnt/lustre/plachetzki/shared/metazoa_2020/above_80/OrthoFinder/Results_Oct19/Orthogroup_Sequences/) to simplify things, and then I'll just move the clean files to the new one I've set up.   
```bash  
for fs in $(ls *fa)
do
echo "now working on $fs"
remove_aliens all_alien_seqs.txt $fs > $fs.clean
done
```
*Doing this in the directory listed above is a bad idea!* I forgot that the directory contains all of the unclassified sequences also, each in their own "orthogroup" file, when really there are only 105,000 or so that actually have multiple sequences. I will copy these actual orthogroups over to my prepared directory (/mnt/lustre/macmaneslab/jlh1023/chap3_2020/alien_indexing/orthogroups), and then just delete them when I've finished with this step. "OG0105176.fa" is the last one I need.  

remove_alien_seqs.sh:  

```bash  
cp /mnt/lustre/plachetzki/shared/metazoa_2020/above_80/OrthoFinder/Results_Oct19/Orthogroup_Sequences/OG001*.fa  

for fs in $(ls *fa)  
do  
echo "now working on $fs"  
/mnt/lustre/macmaneslab/jlh1023/alien_index-master/remove_aliens all_alien_seqs.txt $fs > $fs.clean  
done  

rm *fa
```

*A couple of notes:* Make sure you put the path to the executable, and that you've changed the permissions on it so it will actually run. Also, you'll have to change the #! at the top, because as it is, it won't work on premise (needs to be "#! /usr/bin/env perl" instead of whatever was there before). Also also, in the log file it will be all "error: expected to filter 57772 seqs, but filtered 26" but this is FINE, because we combined them all a minute ago, and it thinks we're just doing this for one fasta, which, we aren't.    

Above is an example for one that I did, contained in "remove_alien_seqs.sh" but I also did it in "remove2.sh" to "remove6.sh" for the rest of the files.       

Now I have orthogroup files that have ".clean" tacked on the end that have had alien seqs removed. It is very possible that some of these only contain one sequence at this point, so I will address that in the wrapper script I am writing for the uclust step happening before interproscan. See "dataset_workflow.md" for details.  


### Do genes in the same orthogroup get annotated with different GO terms?  

I've been relating GO annotations back to the orthogroups that contain the sequences that were annotated. We want to know now if all the sequences in a given orthogroup will always be annotated with the same GO term. I think the early sets of genes I interproscanned might be useful for this, since they contained whole orthogroups of sequences instead of the filtered ones I used later.  

I have interproscan results for lots of nodes (gains and losses, but lots of losses, especially in sponges), and I have the original orthogroups with all of their sequences. I think I can make a list of all the sequences in an orthogroup, and use them to pull out all the relevant lines of interproscan results. Then I could see if all the GO terms in those interproscan results are the same or not. Doing this here: /mnt/lustre/macmaneslab/jlh1023/chap3_2020/interesting_orthos/losses/  

`grep ">" Porifera_seqs/OG0000319.fa | sed 's_>__' > Porifera_loss_OG0000319_seqs.txt`  
`/mnt/lustre/macmaneslab/jlh1023/pipeline_dev/pipeline_scripts/prune_interpro_results.py -l Porifera_loss_OG0000319_seqs.txt -t Porifera_inter.tsv -o Porifera_OG0000319_inter.tsv`  

`/mnt/lustre/macmaneslab/jlh1023/pipeline_dev/pipeline_scripts/prune_interpro_results.py -l Porifera_common_losses_seqnames.txt -t gene_universe_Porifera_no_aliens.tsv -o Porifera_common_losses_inter.tsv`



### Does the uclustering step cluster all or most of the orthogroups in a consistent way?

Since we end up testing the clustered sequences that were run through interproscan in topGO, I want to know how consistently the uclust program is clustering the sequences in orthogroups. Theoretically, there could be one orthogroup that lots of sponges have, that has not diverged that much over the millennia, and that gets clustered into just a few centroid sequences. Then there could be another that has the same number of sequences as the first originally, but diverged more, and so gets clustered into more sequences and ends up with more entries in the interproscan results. This could potentially bias those results into thinking that the more divergent orthogroup is enriched, simply because it has more entries in the interproscan results file. So I'm going to find out how linear the relationship is between original number of sequences in an orthogroup, and number of centroid sequences after uclust does its work.  

I wrote a script that pulls out the number of sequences from fasta files in a directory and records them in a tsv. I did it on the Porifera loss sequences to check things out and it looks very linear, but I'm going to do it on the Metazoa present seqs because it's a nice large dataset for testing. Doing this here: /mnt/lustre/macmaneslab/jlh1023/chap3_2020/interesting_orthos/   
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


### Are the same organisms getting picked as centroid sequences all the time?

It's pretty easy to figure out how many orthogroups are represented by each species. I can just grep the genus name in the ___ file I made with just one centroid per orthogroup.  

`grep -c "Acropora" ___`  

But these numbers are obviously influenced by how many sequences each organism had in orthogroups to begin with. Normally OrthoFinder gived those numbers, but since I've done filtering steps after OrthoFinder, they aren't accurrate anymore. So I wrote a script to count the number of sequences each species has in the remaining orthogroups: /mnt/lustre/macmaneslab/jlh1023/pipeline_dev/pipeline_scripts/ortho_stats.py.  

I ran it like this: `/mnt/lustre/macmaneslab/jlh1023/pipeline_dev/pipeline_scripts/ortho_stats.py -d /mnt/lustre/macmaneslab/jlh1023/chap3_2020/alien_indexing/orthogroups -o /mnt/lustre/macmaneslab/jlh1023/chap3_2020/alien_indexing/filtered_species_counts.tsv` in this directory: `/mnt/lustre/macmaneslab/jlh1023/chap3_2020/alien_indexing/`.  


### What if the gene families that look like losses in Ctenophores are really just super divergent?

If the ctenos have extra-divergent metabolic genes (or some other category), it might look like they have losses, when really, we just have to look harder for them. Apparently this is a problem especially in ctenos, but it's possible in other organisms too. Something like orthofinder might miss them, so we'll need to use a more sensitive search to try to find them. Maybe we will, which will help us refine the story a little, and maybe we won't, in which case we can be more confident that they are indeed lost.  

I think hh-suite will work well for this. I made a conda environment and installed it on premise.  
```bash
ml anaconda/colsa
conda create --name hhsuite --clone template
conda activate hhsuite
conda install -c conda-forge -c bioconda hhsuite
```

Now I'm going to make a database out of the ctenophore datasets to use when I search. I can do this with normal fastas, according to these instructions: https://github.com/soedinglab/hh-suite/wiki#building-customized-databases, so that's what I'm going to follow.  

First, I need clean cteno assemblies. Before, I eliminated all the putative alien sequences from all the orthogroup files before they got clustered and filtered, but I never did it for the original assemblies themselves. So I want to do that, and then I'll move those cleaned files into a new directory I made here: /mnt/lustre/macmaneslab/jlh1023/chap3_2020/verify_loss/clean_ctenos/. I'm writing a script to do this, because lots of the files are in different locations and I don't remember how long it takes to run. The script is called remove_aliens_ctenos.sh, and I can do it the same way I did for the orthogroups, except not in batches.   

```bash   
cd /mnt/lustre/macmaneslab/jlh1023/chap3_2020/alien_indexing  

/mnt/lustre/macmaneslab/jlh1023/alien_index-master/remove_aliens Coeloplana_meteoris.fa.blast.alien_index Coeloplana_meteoris.fa > Coeloplana_meterois_clean.fa  
/mnt/lustre/macmaneslab/jlh1023/alien_index-master/remove_aliens second_group/Hormiphora_californensis.fa.blast.alien_index second_group/Hormiphora_californensis.fa > Hormiphora_californensis_clean.fa  
/mnt/lustre/macmaneslab/jlh1023/alien_index-master/remove_aliens third_group/Lampea_pancerina.fa.blast.alien_index third_group/Lampea_pancerina.fasta > Lampea_pancerina_clean.fa  
/mnt/lustre/macmaneslab/jlh1023/alien_index-master/remove_aliens fourth_group/Vallicula_multiformis.fa.blast.alien_index fourth_group/Vallicula_multiformis.fa > Vallicula_multiformis_clean.fa  
```  

Alright, that worked great, so now I'm going to copy them (and the Mnemiopsis file from /mnt/lustre/plachetzki/shared/metazoa_2020/above_80/) to the new clean ctenos directory (above). I'll be working from there for this next part. And now I can proceed to try to make a database out of them that can be used by hhsuite. I want them all to be the same database, so I'll cat them all together first.  

`cat *.fa > all_ctenos.fa`  

I also have to download the Uniclust30 database. I'm only going to keep it for as long as I need it, because it's pretty huge. Makes me a little nervous.  
```bash  
mkdir databases  
cd databases  
wget http://wwwuser.gwdg.de/~compbiol/uniclust/2020_06/UniRef30_2020_06_hhsuite.tar.gz  
tar xzvf UniRef30_2020_06_hhsuite.tar.gz  
```  

The next steps I'm going to put into a script, as I have no idea how long they take, and it might be a while. Script is called make_cteno_db.sh.   

```bash
module purge
module load anaconda/colsa
conda activate hhsuite

cd /mnt/lustre/macmaneslab/jlh1023/chap3_2020/verify_loss/

ffindex_from_fasta -s clean_ctenos/all_ctenos.fa.ffdata clean_ctenos/all_ctenos.fa.ffindex clean_ctenos/all_ctenos.fa
hhblits_omp -i clean_ctenos/all_ctenos.fa -d /mnt/lustre/macmaneslab/jlh1023/chap3_2020/verify_loss/databases/UniRef30_2020_06 -oa3m cteno_db_a3m_wo_ss -n 2 -cpu 1 -v 0  
```  

Notes: You definitely have to include the whole prefix of the UniRef database. That makes sense, but I wasn't sure if it would just look for files with those endings or if it would need more of a hint than that. Errored right away for me without it. Also, when the hhsuite docs say something like "<db>_fas.ff{data,index}" they mean that you need to put in two files/filenames, one that ends in "data" and one that ends in "index". Maybe this is obvious or standard notation, but I didn't realize this. Also also, don't forget that the command is "hhblits_omp", otherwise it will not work, and will give you error messages that make no sense and have nothing to do with the actual problem.  
  
Now I need the query sequences so that I can search the clean ctenophore database I made. There is a list of orthogroups that the ctenophores have lost here: /mnt/lustre/macmaneslab/jlh1023/chap3_2020/interesting_orthos/losses/Ctenophora_loss.txt. It contains 6181 orthogroup names. There is also a file with all of the centroid sequences that I identified (and interproscanned) for all of the orthogroups, here: /mnt/lustre/macmaneslab/jlh1023/chap3_2020/rescan/rep_og_seqs.fa. These still have the orthogroup name associated with them, so I should be able to pull the correct ones out relatively easily.  
  
Ok, I wrote a script that will take a list of OG names and pull out sequences from a fasta file that has matching OG names in the fasta headers, like those I mentioned above. The script is called "matching_orthos.py" and is here: /mnt/lustre/macmaneslab/jlh1023/pipeline_dev/pipeline_scripts/matching_orthos.py. When I ran it with the above files (`/mnt/lustre/macmaneslab/jlh1023/pipeline_dev/pipeline_scripts/matching_orthos.py -l /mnt/lustre/macmaneslab/jlh1023/chap3_2020/interesting_orthos/losses/Ctenophora_loss.txt -i /mnt/lustre/macmaneslab/jlh1023/chap3_2020/rescan/rep_og_seqs.fa -o /mnt/lustre/macmaneslab/jlh1023/chap3_2020/verify_loss/cteno_missing_og_seqs.fa`), I get a fasta file with 6068 sequences in it. The list of Ctenophore losses has 6181 og names in it, so not all of them were found in the fasta file of all the representative sequences from the orthogroups. I think this is okay, as they could have been lost at various points, like when I filtered for orthogroups that were too small, but I wanted to pull out the names in case I want to trace them later. So I wrote a different version of the same script, called "matching_orthos2.py" in the same location. It is identical to the first, but it also has a section that captures all the matching ones in a set, and finds the difference between that set and the set containing the original OG names I was trying to match. Then it just prints the different to the screen, which I captured in a file, "non_matching.txt". I copied the file into a bbedit window (just because I like them better), and fixed the formatting so that I can tell what's going on. There are 112 orthogroup names that did not have matches in the fasta file of representative sequences. They are all fairly high numbers, which manes me think that they may have gotten filtered out from a lack of enough sequences. I can investigate more later, after I talk to Dave tomorrow.  
  
In the meantime, I now have the fasta file I need to be the query sequences in the search with the database I made for/with hhblitz. So I can press forward there.  
  

