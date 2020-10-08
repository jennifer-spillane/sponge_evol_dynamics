# The workflow for putting together the metazoan dataset for the study of gene family dynamics  

Nhen and then Troy have been diligently assembling transcriptomes for this project for a long time. Then more recently Hannah has also been putting together a comprehensive metazoan dataset for use in this project and others.   

**This is what Nhen and Troy were doing to process transcriptomes:**  
- downloaded transcriptome reads from the ENA  
- removed the spaces from their headers  
    `sed -i 's_ __' file_1.fastq`  
- subsampled down to 35 million bp if necessary  
    `seqtk sample -s 51 Genus_species_1.fastq 35000000 > Genus_species_sub_1.fastq`  
- assembled using the ORP  
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
- ran cd-hit on each protein set with threshold of 98% similar  
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
