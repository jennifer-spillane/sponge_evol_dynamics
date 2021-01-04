## Every check we can think of

I want to be as sure as I can that whatever we end up finding (in the way of sponge gene family losses) is a real finding, and not an artifact of some aspect of the analysis. Things in this section are along those lines.

### What if sponge genomes and transcriptomes are less complete than other clades?

If sponge datasets are less complete, than what looks like loss could just be a crappy quality dataset, and we wouldn't be able to say that the losses are actually losses.

This is not much of an issue because we are staying zoomed out in terms of scale. We are talking about gene family (orthogroup) losses, and so an entire orthogroup would have to be missing from a sponge dataset in order to really show up as a loss in our analysis.

Also, we are looking at the last common ancestor node for each phylum, in order to get flagged as a loss, the gene family has to be missing from all of the organisms in that clade in our tree. For sponges, this is 24 chances for one of the datasets to be complete enough to contain the gene family in question, which is not nothing.

Also also, plenty of the sponges score quite high in terms of genic completeness as measured by BUSCO, and all of our organisms (except hexactinellids) have BUSCO scores above 80, so they are pretty complete. It is very unlikely that each dataset is missing the exact same things, so this is not much of a danger.

### Are sponge sequences not getting put into orthogroups in the same proportions as other organisms?

If sponge sequences (the proteins we put into orthofinder) are not getting placed into orthogroups in the same way as other organisms (maybe the sequences are more diverged and orthofinder cannot recognize them), it might look like the loss of a gene family when really that gene family is just off in an unclassified group by itself.

This seems pretty unlikely, as we are dealing with whole gene families here (whole orthogroups) that contain, generally, multiple members, so
