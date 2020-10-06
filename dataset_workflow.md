# The workflow for putting together the metazoan dataset for the study of gene family dynamics  

Nhen and then Troy have been diligently assembling transcriptomes for this project for a long time. Then more recently Hannah has also been putting together a comprehensive metazoan dataset for use in this project and others.   

This is what Nhen and Troy were doing in terms of processing:  
- downloading transcriptome reads from the ENA  
- removing the spaces from their headers `sed -i 's_ __' file_1.fastq`  
- subsampling down to 35 million bp if necessary `seqtk sample -s 51 genus_species_1.fastq 35000000 > genus_species_sub_1.fastq`  
- assembling using the ORP 

This is what Hannah was doing in terms of processing:  


With these datasets combined, we had just shy of 170 species of animals and close relatives to include. These were not spread evenly across Metazoa, however. Hannah sent me the spreadsheet of all the organisms, and I annotated it with class, order, and family information, so that we could narrow things down appropriately. We had a hilarious number of cnidarians, for example, and while they are great, we just don't need all of them to do this study. Where we had multiple organisms in the same class, we chose the ones that had the best BUSCO scores (preliminary ones) up to three representatives from that clade, and continued with those.
