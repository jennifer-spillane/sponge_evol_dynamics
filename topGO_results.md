# Results from the R package topGO  

I've used this program to find out which gene ontology terms are enriched in gains and losses at the Porifera and Ctenophora nodes. I also did the same calculations for the tree that we constrained so that sponges branch first.  

## For the tree that is based on our data (cteno-first):  

### Gains at the Porifera node  

#### *Biological process*  

Description: Analysis of gains at the Porifera node  
Ontology: BP  
'weight01' algorithm with the 'fisher' test  
1035 GO terms scored: 5 terms with p < 0.01  
Annotation data:  
    Annotated genes: 115696  
    Significant genes: 274  
    Min. no. of genes annotated to a GO: 1  
    Nontrivial nodes: 106    

GO.ID | Term | Annotated | Significant | Expected | classicFisher   
--- | --- | --- | --- | --- | ---
1 GO:0070836 |                             caveola assembly | 117 | 14 | 0.28 | 2.9e-30  
2 GO:0042981 |              regulation of apoptotic process | 666 | 13 | 1.58 | 1.0e-17  
3 GO:0006464 |        cellular protein modification process | 929 | 9 | 2.20 | 7.2e-10  
4 GO:0009116 |                 nucleoside metabolic process | 201 | 5 | 0.48 | 5.4e-08    

#### *Cellular component*  

Description: Analysis of gains at the Porifera node  
Ontology: CC  
'weight01' algorithm with the 'fisher' test  
264 GO terms scored: 2 terms with p < 0.01  
Annotation data:  
    Annotated genes: 143822  
    Significant genes: 491  
    Min. no. of genes annotated to a GO: 1  
    Nontrivial nodes: 15    

GO.ID | Term | Annotated | Significant | Expected | classicFisher  
--- | --- | --- | --- | --- | ---
1 GO:0016021 |               integral component of membrane | 10574 | 66 | 36.10 | <1e-30  
2 GO:0016020 |                                     membrane | 16045 | 100 | 54.78 | <1e-30    

#### *Molecular function*  

Description: Analysis of gains at the Porifera node  
Ontology: MF  
'weight01' algorithm with the 'fisher' test  
601 GO terms scored: 12 terms with p < 0.01  
Annotation data:  
    Annotated genes: 1637364  
    Significant genes: 5399  
    Min. no. of genes annotated to a GO: 1  
    Nontrivial nodes: 83    

GO.ID | Term | Annotated | Significant | Expected | classicFisher  
--- | --- | --- | --- | --- | ---
1 GO:0005515 |                              protein binding | 66620 | 427 | 219.67 | < 1e-30  
2 GO:0005201 |  extracellular matrix structural constitu... | 222 | 11 | 0.73 | 3.5e-21  
3 GO:0005524 |                                  ATP binding | 2428 | 19 | 8.01 | 1.9e-20  
4 GO:0008083 |                       growth factor activity | 422 | 6 | 1.39 | 6.7e-09    



### Losses at the Porifera node  

#### *Biological process*  

Description: Analysis of loss at the Porifera node  
Ontology: BP  
'weight01' algorithm with the 'fisher' test  
1035 GO terms scored: 14 terms with p < 0.01  
Annotation data:  
    Annotated genes: 115696  
    Significant genes: 583  
    Min. no. of genes annotated to a GO: 1  
    Nontrivial nodes: 114  

GO.ID | Term | Annotated | Significant | Expected | classicFisher  
--- | --- | --- | --- | --- | ---
1 GO:0007165 |                          signal transduction | 3134 | 33 | 15.79 | 1.2e-26  
2 GO:0015708 |  silicic acid import across plasma membra... | 6 | 6 | 0.03 | 3.2e-19  
3 GO:0006206 |      pyrimidine nucleobase metabolic process | 4 | 4 | 0.02 | 4.8e-13  
4 GO:0015074 |                              DNA integration | 1115 | 12 | 5.62 | 2.3e-10  
5 GO:0006629 |                      lipid metabolic process | 1154 | 12 | 5.82 | 3.4e-10  
6 GO:0006351 |                 transcription, DNA-templated | 813 | 11 | 4.10 | 1.8e-09  
7 GO:0019079 |                     viral genome replication | 2 | 2 | 0.01 | 7.1e-07   


#### *Cellular component*  

Description: Analysis of loss at the Porifera node  
Ontology: CC  
'weight01' algorithm with the 'fisher' test  
264 GO terms scored: 8 terms with p < 0.01  
Annotation data:  
    Annotated genes: 143822  
    Significant genes: 3764  
    Min. no. of genes annotated to a GO: 1  
    Nontrivial nodes: 64    

GO.ID | Term | Annotated | Significant | Expected | classicFisher  
--- | --- | --- | --- | --- | ---
1 GO:0016021 |               integral component of membrane | 10574 | 427 | 276.73 | < 1e-30  
2 GO:0016592 |                             mediator complex | 184 | 52 | 4.82 | < 1e-30  
3 GO:0016020 |                                     membrane | 16045 | 505 | 419.92 | < 1e-30  
4 GO:0034719 |                       SMN-Sm protein complex | 18 | 18 | 0.47 | < 1e-30  
5 GO:0005634 |                                      nucleus | 1021 | 68 | 26.72 | 8.8e-10    


#### *Molecular function*  

Description: Analysis of loss at the Porifera node  
Ontology: MF  
'weight01' algorithm with the 'fisher' test  
601 GO terms scored: 44 terms with p < 0.01  
Annotation data:  
    Annotated genes: 1637364  
    Significant genes: 30959  
    Min. no. of genes annotated to a GO: 1  
    Nontrivial nodes: 155    

GO.ID | Term | Annotated | Significant | Expected | classicFisher  
--- | --- | --- | --- | --- | ---
1 GO:0005515 |                              protein binding | 66620 | 1767 | 1259.64 | < 1e-30  
2 GO:0008191 |      metalloendopeptidase inhibitor activity | 71 | 70 | 1.34 | < 1e-30  
3 GO:0030414 |                 peptidase inhibitor activity | 1218 | 120 | 23.03 | < 1e-30  
4 GO:0003676 |                         nucleic acid binding | 15493 | 203 | 292.94 | < 1e-30  
5 GO:0008773 |  [protein-PII] uridylyltransferase activi... | 24 | 24 | 0.45 | < 1e-30  
6 GO:0003824 |                           catalytic activity | 25714 | 357 | 486.20 | < 1e-30  
7 GO:0016747 |  transferase activity, transferring acyl ... | 1838 | 63 | 34.75 | < 1e-30  
8 GO:0005509 |                          calcium ion binding | 4886 | 75 | 92.38 | < 1e-30  
9 GO:0004553 |  hydrolase activity, hydrolyzing O-glycos... | 78 | 19 | 1.47 | < 1e-30  
10 GO:0003677 |                                 DNA binding | 4967 | 60 | 93.92 | < 1e-30  
11 GO:0008168 |                  methyltransferase activity | 1359 | 36 | 25.70 | 4.1e-23  
12 GO:0008270 |                            zinc ion binding | 3270 | 40 | 61.83 | 6.0e-22  
13 GO:0030246 |                        carbohydrate binding | 654 | 20 | 12.37 | 7.2e-17  
14 GO:0008080 |                N-acetyltransferase activity | 488 | 16 | 9.23 | 4.7e-16  
15 GO:0046872 |                           metal ion binding | 9946 | 139 | 188.06 | 1.1e-15  
16 GO:0016746 | transferase activity, transferring acyl ... | 2444 | 79 | 46.21 | 9.3e-15  
17 GO:0016787 |                          hydrolase activity | 7603 | 74 | 143.76 | 2.6e-13  
18 GO:0046983 |               protein dimerization activity | 3269 | 28 | 61.81 | 2.5e-12  
19 GO:0016846 |                carbon-sulfur lyase activity | 15 | 5 | 0.28 | 3.5e-11  
20 GO:0003714 |          transcription corepressor activity | 6 | 4 | 0.11 | 1.1e-10  
21 GO:0005524 |                                 ATP binding | 2428 | 20 | 45.91 | 8.2e-09  
22 GO:0005525 |                                 GTP binding | 1534 | 16 | 29.00 | 1.0e-08  
23 GO:0008146 |                   sulfotransferase activity | 998 | 13 | 18.87 | 1.9e-08  
24 GO:0019901 |                      protein kinase binding | 18 | 4 | 0.34 | 2.1e-08  
25 GO:0022857 |          transmembrane transporter activity | 1255 | 14 | 23.73 | 3.7e-08  
26 GO:0008757 | S-adenosylmethionine-dependent methyltra... | 174 | 8 | 3.29 | 1.0e-07  
27 GO:0016757 | transferase activity, transferring glyco... | 1494 | 15 | 28.25 | 1.8e-07    



### Gains at the Ctenophora node  

#### *Biological process*  

Description: Analysis of gains at the Cteno node  
Ontology: BP  
'weight01' algorithm with the 'fisher' test  
998 GO terms scored: 6 terms with p < 0.01  
Annotation data:  
    Annotated genes: 106161  
    Significant genes: 122  
    Min. no. of genes annotated to a GO: 1  
    Nontrivial nodes: 113  

GO.ID | Term | Annotated | Significant | Expected | classicFisher  
--- | --- | --- | --- | --- | ---
1 GO:0042981 |              regulation of apoptotic process | 149 | 6 | 0.17 | 5.1e-13  
2 GO:0051260 |                  protein homooligomerization | 196 | 4 | 0.23 | 8.0e-08    

#### *Cellular component*  

Description: Analysis of gains at the Cteno node  
Ontology: CC  
'weight01' algorithm with the 'fisher' test  
237 GO terms scored: 3 terms with p < 0.01  
Annotation data:  
    Annotated genes: 139143  
    Significant genes: 1484  
    Min. no. of genes annotated to a GO: 1  
    Nontrivial nodes: 37    

GO.ID | Term | Annotated | Significant | Expected | classicFisher  
--- | --- | --- | --- | --- | ---
1 GO:0016021 |               integral component of membrane | 10347 | 285 | 110.35 | < 1e-30  
2 GO:0016020 |                                     membrane | 15188 | 301 | 161.98 | 3.7e-17    

#### *Molecular function*  

Description: Analysis of gains at the Cteno node  
Ontology: MF  
'weight01' algorithm with the 'fisher' test  
573 GO terms scored: 27 terms with p < 0.01  
Annotation data:  
    Annotated genes: 1500323  
    Significant genes: 3434  
    Min. no. of genes annotated to a GO: 1  
    Nontrivial nodes: 96    

GO.ID | Term | Annotated | Significant | Expected | classicFisher  
--- | --- | --- | --- | --- | ---
1 GO:0005515 |                              protein binding | 59949 | 260 | 137.21 | < 1e-30  
2 GO:0005509 |                          calcium ion binding | 4367 | 35 | 10.00 | < 1e-30  
3 GO:0003676 |                         nucleic acid binding | 14298 | 37 | 32.73 | 1.4e-12  
4 GO:0046983 |                protein dimerization activity | 3034 | 10 | 6.94 | 2.1e-08  
5 GO:0022857 |           transmembrane transporter activity | 1234 | 7 | 2.82 | 7.7e-08  
6 GO:0016409 |                palmitoyltransferase activity | 443 | 5 | 1.01 | 2.0e-07  
7 GO:0003824 |                           catalytic activity | 24210 | 44 | 55.41 | 4.2e-07  
8 GO:0003677 |                                  DNA binding | 4694 | 15 | 10.74 | 4.3e-07  
9 GO:0003735 |           structural constituent of ribosome | 58 | 3 | 0.13 | 6.5e-07  
10 GO:0008289 |                               lipid binding | 1660 | 8 | 3.80 | 1.1e-06  
11 GO:0043047 |       single-stranded telomeric DNA binding | 6 | 2 | 0.01 | 1.2e-06    


### Losses at the Ctenophora node  

#### *Biological process*  
Description: Analysis of losses at the Cteno node  
Ontology: BP  
'weight01' algorithm with the 'fisher' test  
998 GO terms scored: 54 terms with p < 0.01  
Annotation data:  
    Annotated genes: 106161  
    Significant genes: 10044  
    Min. no. of genes annotated to a GO: 1  
    Nontrivial nodes: 530  

GO.ID | Term | Annotated | Significant | Expected | classicFisher  
--- | --- | --- | --- | --- | ---
1 GO:0006629 |                      lipid metabolic process | 1065 | 204 | 100.76 | < 1e-30  
2 GO:0000160 |      phosphorelay signal transduction system | 70 | 68 | 6.62 | < 1e-30  
3 GO:0006807 |          nitrogen compound metabolic process | 4794 | 409 | 453.57 | < 1e-30  
4 GO:0070072 |  vacuolar proton-transporting V-type ATPa... | 106 | 69 | 10.03 | < 1e-30  
5 GO:0035556 |            intracellular signal transduction | 1291 | 207 | 122.14 | < 1e-30  
6 GO:0007165 |                          signal transduction | 3081 | 359 | 291.50 | < 1e-30  
7 GO:0019915 |                                lipid storage | 42 | 42 | 3.97 | < 1e-30  
8 GO:0006413 |                     translational initiation | 42 | 42 | 3.97 | < 1e-30  
9 GO:0006450 |         regulation of translational fidelity | 40 | 40 | 3.78 | < 1e-30  
10 GO:0071816 | tail-anchored membrane protein insertion... | 38 | 36 | 3.60 | < 1e-30  
11 GO:0051126 |     negative regulation of actin nucleation | 28 | 28 | 2.65 | < 1e-30  
12 GO:0055114 |                 oxidation-reduction process | 558 | 73 | 52.79 | < 1e-30  
13 GO:0015074 |                             DNA integration | 829 | 82 | 78.43 | < 1e-30  
14 GO:0000272 |            polysaccharide catabolic process | 24 | 22 | 2.27 | < 1e-30  
15 GO:0006412 |                                 translation | 143 | 77 | 13.53 | < 1e-30  
16 GO:0044528 | regulation of mitochondrial mRNA stabili... | 18 | 17 | 1.70 | 1.4e-30  
17 GO:0070836 |                            caveola assembly | 14 | 14 | 1.32 | 2.4e-26  
18 GO:0007009 |                plasma membrane organization | 61 | 35 | 5.77 | 2.6e-26  
19 GO:0042981 |             regulation of apoptotic process | 149 | 31 | 14.10 | 2.9e-26  
20 GO:0006284 |                        base-excision repair | 63 | 22 | 5.96 | 1.5e-24  
21 GO:0042254 |                         ribosome biogenesis | 152 | 26 | 14.38 | 4.5e-23  
22 GO:0009058 |                        biosynthetic process | 1818 | 182 | 172.00 | 8.0e-20  
23 GO:0006360 |           transcription by RNA polymerase I  | 10 | 10 | 0.95 | 5.1e-19  
24 GO:0044237 |                  cellular metabolic process | 4890 | 377 | 462.65 | 2.3e-18  
25 GO:0005975 |              carbohydrate metabolic process | 359 | 52 | 33.97 | 7.9e-16  
26 GO:0031110 | regulation of microtubule polymerization... | 10 | 8 | 0.95 | 1.0e-13  
27 GO:0055085 |                     transmembrane transport | 321 | 40 | 30.37 | 3.5e-13  
28 GO:0009116 |                nucleoside metabolic process | 195 | 24 | 18.45 | 4.0e-12  
29 GO:0015708 | silicic acid import across plasma membra... | 6 | 6 | 0.57 | 1.1e-11  
30 GO:0009306 |                           protein secretion | 6 | 6 | 0.57 | 1.1e-11  
31 GO:0044249 |               cellular biosynthetic process | 1726 | 162 | 163.30 | 2.0e-11  
32 GO:0003333 |          amino acid transmembrane transport | 12 | 7 | 1.14 | 1.2e-10  
33 GO:0006388 | tRNA splicing, via endonucleolytic cleav... | 50 | 11 | 4.73 | 1.7e-10  
34 GO:0006355 | regulation of transcription, DNA-templat... | 451 | 28 | 42.67 | 3.7e-10  
35 GO:0006189 |          'de novo' IMP biosynthetic process | 5 | 5 | 0.47 | 7.2e-10  
36 GO:0002098 |            tRNA wobble uridine modification | 5 | 5 | 0.47 | 7.2e-10  
37 GO:0019428 |              allantoin biosynthetic process | 4 | 4 | 0.38 | 4.9e-08  
38 GO:0000105 |              histidine biosynthetic process | 4 | 4 | 0.38 | 4.9e-08  

#### *Cellular component*   

Description: Analysis of losses at the Cteno node  
Ontology: CC  
'weight01' algorithm with the 'fisher' test  
237 GO terms scored: 23 terms with p < 0.01  
Annotation data:  
    Annotated genes: 139143  
    Significant genes: 6294  
    Min. no. of genes annotated to a GO: 1  
    Nontrivial nodes: 128    

GO.ID | Term | Annotated | Significant | Expected | classicFisher  
--- | --- | --- | --- | --- | ---
1 GO:0016021 |               integral component of membrane | 10347 | 1105 | 468.04 | < 1e-30  
2 GO:0016020 |                                     membrane | 15188 | 1465 | 687.01 | < 1e-30  
3 GO:0005761 |                       mitochondrial ribosome | 59 | 58 | 2.67 | < 1e-30  
4 GO:0000813 |                              ESCRT I complex | 37 | 36 | 1.67 | < 1e-30  
5 GO:0016592 |                             mediator complex | 162 | 54 | 7.33 | < 1e-30  
6 GO:0031966 |                       mitochondrial membrane | 235 | 50 | 10.63 | < 1e-30  
7 GO:0005576 |                         extracellular region | 339 | 69 | 15.33 | < 1e-30  
8 GO:0005753 |  mitochondrial proton-transporting ATP sy... | 18 | 18 | 0.81 | < 1e-30  
9 GO:0034719 |                       SMN-Sm protein complex | 18 | 18 | 0.81 | < 1e-30  
10 GO:0008023 |     transcription elongation factor complex | 14 | 14 | 0.63 | 2.8e-27  
11 GO:0031011 |                               Ino80 complex | 13 | 13 | 0.59 | 2.3e-25  
12 GO:0005634 |                                     nucleus | 945 | 125 | 42.75 | 3.6e-25  
13 GO:0005615 |                         extracellular space | 95 | 19 | 4.30 | 1.7e-17  
14 GO:0016010 | dystrophin-associated glycoprotein compl... | 8 | 8 | 0.36 | 6.9e-16  
15 GO:0005886 |                             plasma membrane | 137 | 15 | 6.20 | 2.6e-08    

#### *Molecular function*  

Description: Analysis of losses at the Cteno node  
Ontology: MF  
'weight01' algorithm with the 'fisher' test  
573 GO terms scored: 125 terms with p < 0.01  
Annotation data:  
    Annotated genes: 1500323  
    Significant genes: 198820  
    Min. no. of genes annotated to a GO: 1  
    Nontrivial nodes: 358     

GO.ID | Term | Annotated | Significant | Expected | classicFisher  
--- | --- | --- | --- | --- | ---
1 GO:0016491 |                     oxidoreductase activity | 1191 | 414 | 157.83 | < 1e-30  
2 GO:0008168 |                  methyltransferase activity | 1333 | 590 | 176.65 | < 1e-30  
3 GO:0016787 |                          hydrolase activity | 7070 | 1560 | 936.90 | < 1e-30  
4 GO:0005515 |                             protein binding | 59949 | 8781 | 7944.33 | < 1e-30  
5 GO:0003824 |                          catalytic activity | 24210 | 6012 | 3208.26 | < 1e-30  
6 GO:0016757 | transferase activity, transferring glyco... | 1432 | 373 | 189.77 | < 1e-30  
7 GO:0022857 |          transmembrane transporter activity | 1234 | 330 | 163.53 | < 1e-30  
8 GO:0008146 |                   sulfotransferase activity | 999 | 273 | 132.39 | < 1e-30  
9 GO:0003697 |                 single-stranded DNA binding | 131 | 125 | 17.36 | < 1e-30  
10 GO:0016791 |                         phosphatase activity | 348 | 201 | 46.12 | < 1e-30  
11 GO:0016772 |  transferase activity, transferring phosp... | 1201 | 215 | 159.15 | < 1e-30  
12 GO:0003676 |                         nucleic acid binding | 14298 | 1012 | 1894.74 | < 1e-30  
13 GO:0008080 |                 N-acetyltransferase activity | 466 | 151 | 61.75 | < 1e-30  
14 GO:0008757 |  S-adenosylmethionine-dependent methyltra... | 173 | 127 | 22.93 | < 1e-30  
15 GO:0051537 |             2 iron, 2 sulfur cluster binding | 121 | 96 | 16.03 | < 1e-30  
16 GO:0008270 |                             zinc ion binding | 2828 | 282 | 374.76 | < 1e-30  
17 GO:0016747 |  transferase activity, transferring acyl ... | 1712 | 437 | 226.87 | < 1e-30  
18 GO:0016810 |  hydrolase activity, acting on carbon-nit... | 277 | 110 | 36.71 | < 1e-30  
19 GO:0005509 |                          calcium ion binding | 4367 | 323 | 578.71 | < 1e-30  
20 GO:0005524 |                                  ATP binding | 2232 | 237 | 295.78 | < 1e-30  
21 GO:0005525 |                                  GTP binding | 1230 | 174 | 163.00 | < 1e-30  
22 GO:0004144 |  diacylglycerol O-acyltransferase activit... | 64 | 64 | 8.48 | < 1e-30  
23 GO:0008171 |                 O-methyltransferase activity | 112 | 72 | 14.84 | < 1e-30  
24 GO:0004064 |                        arylesterase activity | 54 | 54 | 7.16 | < 1e-30  
25 GO:0008484 |            sulfuric ester hydrolase activity | 441 | 131 | 58.44 | < 1e-30  
26 GO:0003735 |           structural constituent of ribosome | 58 | 55 | 7.69 | < 1e-30  
27 GO:0017176 |  phosphatidylinositol N-acetylglucosaminy... | 52 | 52 | 6.89 | < 1e-30  
28 GO:0008374 |                   O-acyltransferase activity | 114 | 114 | 15.11 | < 1e-30  
29 GO:0046872 |                            metal ion binding | 8799 | 790 | 1166.03 | < 1e-30  
30 GO:0035091 |                 phosphatidylinositol binding | 1008 | 135 | 133.58 | < 1e-30  
31 GO:0050660 |          flavin adenine dinucleotide binding | 237 | 116 | 31.41 | < 1e-30  
32 GO:0003953 |                   NAD+ nucleosidase activity | 42 | 42 | 5.57 | < 1e-30  
33 GO:0016788 |  hydrolase activity, acting on ester bond... | 2310 | 568 | 306.12 | < 1e-30  
34 GO:0070567 |                cytidylyltransferase activity | 47 | 41 | 6.23 | < 1e-30  
35 GO:0071949 |                                  FAD binding | 141 | 57 | 18.69 | < 1e-30  
36 GO:0003677 |                                  DNA binding | 4694 | 357 | 622.04 | < 1e-30  
37 GO:0020037 |                                 heme binding | 335 | 72 | 44.39 | < 1e-30  
38 GO:0030246 |                         carbohydrate binding | 469 | 90 | 62.15 | < 1e-30  
39 GO:0016884 |  carbon-nitrogen ligase activity, with gl... | 33 | 33 | 4.37 | < 1e-30  
40 GO:0004869 |  cysteine-type endopeptidase inhibitor ac... | 130 | 52 | 17.23 | < 1e-30  
41 GO:0003723 |                                  RNA binding | 1604 | 141 | 212.56 | < 1e-30  
42 GO:0004129 |                cytochrome-c oxidase activity | 154 | 54 | 20.41 | < 1e-30  
43 GO:0003993 |                    acid phosphatase activity | 32 | 32 | 4.24 | < 1e-30  
44 GO:0004842 |       ubiquitin-protein transferase activity | 478 | 77 | 63.34 | < 1e-30  
45 GO:0002161 |              aminoacyl-tRNA editing activity | 34 | 32 | 4.51 | < 1e-30  
46 GO:0004423 |               iduronate-2-sulfatase activity | 26 | 26 | 3.45 | < 1e-30  
47 GO:0016798 |  hydrolase activity, acting on glycosyl b... | 200 | 116 | 26.50 | < 1e-30  
48 GO:0045145 |  single-stranded DNA 5'-3' exodeoxyribonu... | 25 | 25 | 3.31 | < 1e-30  
49 GO:0004553 |  hydrolase activity, hydrolyzing O-glycos... | 48 | 33 | 6.36 | < 1e-30  
50 GO:0008773 |  [protein-PII] uridylyltransferase activi... | 24 | 24 | 3.18 | < 1e-30  
51 GO:0010181 |                                  FMN binding | 88 | 35 | 11.66 | < 1e-30  
52 GO:0015035 |  protein disulfide oxidoreductase activit... | 49 | 28 | 6.49 | < 1e-30  
53 GO:0008237 |                    metallopeptidase activity | 792 | 84 | 104.95 | < 1e-30  
54 GO:0043531 |                                  ADP binding | 23 | 21 | 3.05 | < 1e-30  
55 GO:0003950 |         NAD+ ADP-ribosyltransferase activity | 353 | 51 | 46.78 | < 1e-30  
56 GO:0003847 |  1-alkyl-2-acetylglycerophosphocholine es... | 19 | 19 | 2.52 | < 1e-30  
57 GO:0016829 |                               lyase activity | 302 | 64 | 40.02 | < 1e-30  
58 GO:0008289 |                                lipid binding | 1660 | 194 | 219.98 | < 1e-30  
59 GO:0008233 |                           peptidase activity | 1257 | 129 | 166.58 | < 1e-30  
60 GO:0004867 |  serine-type endopeptidase inhibitor acti... | 749 | 62 | 99.26 | < 1e-30  
61 GO:0017022 |                               myosin binding | 16 | 16 | 2.12 | < 1e-30  
62 GO:0004346 |               glucose-6-phosphatase activity | 15 | 15 | 1.99 | 1.9e-29  
63 GO:0016746 |  transferase activity, transferring acyl ... | 2313 | 501 | 306.51 | 3.3e-29  
64 GO:0005507 |                           copper ion binding | 103 | 27 | 13.65 | 3.9e-28  
65 GO:0004055 |          argininosuccinate synthase activity | 14 | 14 | 1.86 | 1.6e-27  
66 GO:0008119 |      thiopurine S-methyltransferase activity | 14 | 14 | 1.86 | 1.6e-27  
67 GO:0016279 |  protein-lysine N-methyltransferase activ... | 40 | 16 | 5.30 | 1.3e-25  
68 GO:0016874 |                              ligase activity | 362 | 79 | 47.97 | 1.6e-24  
69 GO:0051539 |             4 iron, 4 sulfur cluster binding | 23 | 15 | 3.05 | 8.5e-24  
70 GO:0043022 |                             ribosome binding | 42 | 18 | 5.57 | 9.1e-24  
71 GO:0035438 |                        cyclic-di-GMP binding | 12 | 12 | 1.59 | 1.1e-23  
72 GO:0051536 |                  iron-sulfur cluster binding | 163 | 125 | 21.60 | 1.6e-23  
73 GO:0016765 |  transferase activity, transferring alkyl... | 243 | 32 | 32.20 | 1.9e-20  
74 GO:0016783 |                   sulfurtransferase activity | 21 | 17 | 2.78 | 7.1e-20  
75 GO:0005085 |  guanyl-nucleotide exchange factor activi... | 809 | 48 | 107.21 | 9.8e-19  
76 GO:0016763 |  transferase activity, transferring pento... | 400 | 68 | 53.01 | 4.5e-18  
77 GO:0030414 |                 peptidase inhibitor activity | 1154 | 132 | 152.93 | 2.4e-16  
78 GO:2001070 |                               starch binding | 24 | 11 | 3.18 | 1.9e-15  
79 GO:0016836 |                         hydro-lyase activity | 85 | 15 | 11.26 | 4.0e-15  
80 GO:0004843 |  thiol-dependent ubiquitin-specific prote... | 70 | 15 | 9.28 | 7.3e-15  
81 GO:0046912 |  transferase activity, transferring acyl ... | 33 | 12 | 4.37 | 8.8e-14  
82 GO:0004518 |                            nuclease activity | 296 | 44 | 39.23 | 3.0e-13  
83 GO:0008658 |                           penicillin binding | 8 | 7 | 1.06 | 3.1e-13  
84 GO:0004222 |                metalloendopeptidase activity | 66 | 13 | 8.75 | 1.4e-12  
85 GO:0004857 |                    enzyme inhibitor activity | 1208 | 144 | 160.08 | 2.1e-12  
86 GO:0043565 |                sequence-specific DNA binding | 130 | 16 | 17.23 | 7.6e-12  
87 GO:0004792 |       thiosulfate sulfurtransferase activity | 11 | 7 | 1.46 | 1.2e-11  
88 GO:0000049 |                                 tRNA binding | 55 | 11 | 7.29 | 6.3e-11  
89 GO:0043169 |                               cation binding | 8873 | 805 | 1175.83 | 1.7e-10  
90 GO:0003714 |           transcription corepressor activity | 5 | 5 | 0.66 | 2.7e-10  
91 GO:0016743 |  carboxyl- or carbamoyltransferase activi... | 5 | 5 | 0.66 | 2.7e-10  
92 GO:0005096 |                    GTPase activator activity | 304 | 20 | 40.29 | 1.8e-09  
93 GO:0016831 |                       carboxy-lyase activity | 38 | 11 | 5.04 | 8.4e-09  
94 GO:0046982 |          protein heterodimerization activity | 525 | 25 | 69.57 | 1.4e-08  
95 GO:0005212 |           structural constituent of eye lens | 4 | 4 | 0.53 | 2.2e-08  
96 GO:0003855 |        3-dehydroquinate dehydratase activity | 4 | 4 | 0.53 | 2.2e-08  
97 GO:0019239 |                           deaminase activity | 104 | 11 | 13.78 | 6.8e-08    




## Sponge-first tree topGO results  

### Porifera gains  

#### *Biological process*  

Description: Analysis of gains at the Porifera node  
Ontology: BP  
'weight01' algorithm with the 'fisher' test  
990 GO terms scored: 5 terms with p < 0.01  
Annotation data:  
    Annotated genes: 106313  
    Significant genes: 274  
    Min. no. of genes annotated to a GO: 1  
    Nontrivial nodes: 106    

GO.ID | Term | Annotated | Significant | Expected | classicFisher
--- | --- | --- | --- | --- | ---
1 GO:0070836 |                             caveola assembly | 28 | 14 | 0.07 | < 1e-30
2 GO:0042981 |              regulation of apoptotic process | 156 | 13 | 0.40 | 1.6e-25
3 GO:0006464 |        cellular protein modification process | 815 | 9 | 2.10 | 4.8e-10
4 GO:0009116 |                 nucleoside metabolic process | 200 | 5 | 0.52 | 7.9e-08  

#### *Cellular component*  

Description: Analysis of gains at the Porifera node  
Ontology: CC  
'weight01' algorithm with the 'fisher' test  
237 GO terms scored: 3 terms with p < 0.01  
Annotation data:  
    Annotated genes: 138150  
    Significant genes: 491  
    Min. no. of genes annotated to a GO: 1  
    Nontrivial nodes: 15    

GO.ID | Term | Annotated | Significant | Expected | classicFisher
--- | --- | --- | --- | --- | ---
1 GO:0016021 |               integral component of membrane | 10128 | 66 | 36.00 | <1e-30
2 GO:0016020 |                                     membrane | 14987 | 100 | 53.27 | <1e-30  

#### *Molecular function*  

Description: Analysis of gains at the Porifera node  
Ontology: MF  
'weight01' algorithm with the 'fisher' test  
572 GO terms scored: 13 terms with p < 0.01  
Annotation data:  
    Annotated genes: 1502288  
    Significant genes: 5399  
    Min. no. of genes annotated to a GO: 1  
    Nontrivial nodes: 83    

GO.ID | Term | Annotated | Significant | Expected | classicFisher
--- | --- | --- | --- | --- | ---
1 GO:0005515 |                              protein binding | 60116 | 427 | 216.05 | < 1e-30
2 GO:0005201 |  extracellular matrix structural constitu... | 209 | 11 | 0.75 | 4.5e-21
3 GO:0005524 |                                  ATP binding | 2248 | 19 | 8.08 | 2.2e-20
4 GO:0008083 |                       growth factor activity | 404 | 6 | 1.45 | 8.6e-09  



### Porifera losses  

#### *Biological process*  

Description: Analysis of loss at the Porifera node  
Ontology: BP  
'weight01' algorithm with the 'fisher' test  
990 GO terms scored: 11 terms with p < 0.01  
Annotation data:  
    Annotated genes: 106313  
    Significant genes: 433  
    Min. no. of genes annotated to a GO: 1  
    Nontrivial nodes: 99    

GO.ID | Term | Annotated | Significant | Expected | classicFisher
--- | --- | --- | --- | --- | ---
1 GO:0007165 |                          signal transduction | 3080 | 30 | 12.54 | 5.1e-28
2 GO:0015708 |  silicic acid import across plasma membra... | 6 | 6 | 0.02 | 9.2e-20
3 GO:0006206 |      pyrimidine nucleobase metabolic process | 4 | 4 | 0.02 | 2.2e-13
4 GO:0006351 |                 transcription, DNA-templated | 794 | 11 | 3.23 | 1.8e-10
5 GO:0006629 |                      lipid metabolic process | 1065 | 9 | 4.34 | 6.1e-08  

#### *Cellular component*  

Description: Analysis of loss at the Porifera node  
Ontology: CC  
'weight01' algorithm with the 'fisher' test  
237 GO terms scored: 9 terms with p < 0.01  
Annotation data:  
    Annotated genes: 138150  
    Significant genes: 486  
    Min. no. of genes annotated to a GO: 1  
    Nontrivial nodes: 53    

GO.ID | Term | Annotated | Significant | Expected | classicFisher
--- | --- | --- | --- | --- | ---
1 GO:0016592 |                             mediator complex | 157 | 52 | 0.55 | < 1e-30
2 GO:0034719 |                       SMN-Sm protein complex | 18 | 18 | 0.06 | < 1e-30
3 GO:0005634 |                                      nucleus | 940 | 68 | 3.31 | 1.9e-20
4 GO:0016021 |               integral component of membrane | 10128 | 45 | 35.63 | 8.2e-15
5 GO:0016020 |                                     membrane | 14987 | 73 | 52.72 | 9.8e-15  

#### *Molecular function*  

Description: Analysis of loss at the Porifera node  
Ontology: MF  
'weight01' algorithm with the 'fisher' test  
572 GO terms scored: 40 terms with p < 0.01  
Annotation data:  
    Annotated genes: 1502288  
    Significant genes: 24121  
    Min. no. of genes annotated to a GO: 1  
    Nontrivial nodes: 137    

GO.ID | Term | Annotated | Significant | Expected | classicFisher
--- | --- | --- | --- | --- | ---
1 GO:0005515 |                              protein binding | 60116 | 1390 | 965.23 | < 1e-30
2 GO:0008773 |  [protein-PII] uridylyltransferase activi... | 24 | 24 | 0.39 | < 1e-30
3 GO:0016747 |  transferase activity, transferring acyl ... | 1705 | 63 | 27.38 | < 1e-30
4 GO:0003824 |                           catalytic activity | 24191 | 306 | 388.41 | < 1e-30
5 GO:0004553 |  hydrolase activity, hydrolyzing O-glycos... | 48 | 19 | 0.77 | < 1e-30
6 GO:0030414 |                 peptidase inhibitor activity | 1157 | 23 | 18.58 | 2.5e-30
7 GO:0008270 |                             zinc ion binding | 2830 | 38 | 45.44 | 4.9e-26
8 GO:0008168 |                   methyltransferase activity | 1333 | 34 | 21.40 | 1.4e-23
9 GO:0005509 |                          calcium ion binding | 4337 | 37 | 69.64 | 6.7e-19
10 GO:0008080 |                N-acetyltransferase activity | 464 | 16 | 7.45 | 4.4e-18
11 GO:0016787 |                          hydrolase activity | 7060 | 70 | 113.36 | 1.2e-16
12 GO:0016746 | transferase activity, transferring acyl ... | 2306 | 79 | 37.03 | 1.5e-16
13 GO:0003714 |          transcription corepressor activity | 5 | 4 | 0.08 | 1.3e-11
14 GO:0005525 |                                 GTP binding | 1232 | 14 | 19.78 | 1.3e-09
15 GO:0016757 | transferase activity, transferring glyco... | 1433 | 15 | 23.01 | 6.0e-09
16 GO:0003676 |                        nucleic acid binding | 14271 | 51 | 229.14 | 8.1e-09
17 GO:0008757 | S-adenosylmethionine-dependent methyltra... | 173 | 8 | 2.78 | 2.4e-08
18 GO:0046872 |                           metal ion binding | 8770 | 88 | 140.81 | 7.7e-08
19 GO:0046983 |               protein dimerization activity | 3024 | 17 | 48.55 | 2.5e-07
20 GO:0005524 |                                 ATP binding | 2248 | 15 | 36.09 | 3.5e-07
21 GO:0016846 |                carbon-sulfur lyase activity | 14 | 3 | 0.22 | 7.4e-07
22 GO:0016872 |               intramolecular lyase activity | 2 | 2 | 0.03 | 1.6e-06
23 GO:0004197 |        cysteine-type endopeptidase activity | 2 | 2 | 0.03 | 1.6e-06
24 GO:0003796 |                           lysozyme activity | 2 | 2 | 0.03 | 1.6e-06  




### Ctenophora gains  

#### *Biological process*  

Description: Analysis of gains at the Cteno node  
Ontology: BP  
'weight01' algorithm with the 'fisher' test  
998 GO terms scored: 6 terms with p < 0.01  
Annotation data:  
    Annotated genes: 106317  
    Significant genes: 122  
    Min. no. of genes annotated to a GO: 1  
    Nontrivial nodes: 113    

GO.ID | Term | Annotated | Significant | Expected | classicFisher
--- | --- | --- | --- | --- | ---
1 GO:0042981 |              regulation of apoptotic process | 149 | 6 | 0.17 | 5.0e-13
2 GO:0051260 |                  protein homooligomerization | 196 | 4 | 0.22 | 8.0e-08  

#### *Cellular component*  

Description: Analysis of gains at the Cteno node  
Ontology: CC  
'weight01' algorithm with the 'fisher' test  
237 GO terms scored: 3 terms with p < 0.01  
Annotation data:  
    Annotated genes: 142451  
    Significant genes: 1484  
    Min. no. of genes annotated to a GO: 1  
    Nontrivial nodes: 37    

GO.ID | Term | Annotated | Significant | Expected | classicFisher
--- | --- | --- | --- | --- | ---
1 GO:0016021 |               integral component of membrane | 10347 | 285 | 107.79 | < 1e-30
2 GO:0016020 |                                     membrane | 15188 | 301 | 158.22 | 2.5e-17  


#### *Molecular function*  

Description: Analysis of gains at the Cteno node  
Ontology: MF  
'weight01' algorithm with the 'fisher' test  
573 GO terms scored: 27 terms with p < 0.01  
Annotation data:  
    Annotated genes: 1507423  
    Significant genes: 3434  
    Min. no. of genes annotated to a GO: 1  
    Nontrivial nodes: 96    

GO.ID | Term | Annotated | Significant | Expected | classicFisher
--- | --- | --- | --- | --- | ---
1 GO:0005515 |                              protein binding | 59949 | 260 | 136.57 | < 1e-30
2 GO:0005509 |                          calcium ion binding | 4367 | 35 | 9.95 | < 1e-30
3 GO:0003676 |                         nucleic acid binding | 14298 | 37 | 32.57 | 1.3e-12
4 GO:0046983 |                protein dimerization activity | 3034 | 10 | 6.91 | 2.0e-08
5 GO:0022857 |           transmembrane transporter activity | 1234 | 7 | 2.81 | 7.5e-08
6 GO:0016409 |                palmitoyltransferase activity | 443 | 5 | 1.01 | 2.0e-07
7 GO:0003824 |                           catalytic activity | 24210 | 44 | 55.15 | 4.0e-07
8 GO:0003677 |                                  DNA binding | 4694 | 15 | 10.69 | 4.1e-07
9 GO:0003735 |           structural constituent of ribosome | 58 | 3 | 0.13 | 6.4e-07  


### Ctenophora losses  

#### *Biological process*  

Description: Analysis of losses at the Cteno node  
Ontology: BP  
'weight01' algorithm with the 'fisher' test  
998 GO terms scored: 54 terms with p < 0.01  
Annotation data:  
    Annotated genes: 106317  
    Significant genes: 9748  
    Min. no. of genes annotated to a GO: 1  
    Nontrivial nodes: 530    

GO.ID | Term | Annotated | Significant | Expected | classicFisher
--- | --- | --- | --- | --- | ---
1 GO:0006629 |                      lipid metabolic process | 1065 | 204 | 97.65 | < 1e-30
2 GO:0006807 |          nitrogen compound metabolic process | 4794 | 407 | 439.55 | < 1e-30
3 GO:0000160 |      phosphorelay signal transduction system | 70 | 67 | 6.42 | < 1e-30
4 GO:0070072 |  vacuolar proton-transporting V-type ATPa... | 106 | 69 | 9.72 | < 1e-30
5 GO:0019915 |                                lipid storage | 42 | 42 | 3.85 | < 1e-30
6 GO:0006413 |                     translational initiation | 42 | 42 | 3.85 | < 1e-30
7 GO:0035556 |            intracellular signal transduction | 1291 | 202 | 118.37 | < 1e-30
8 GO:0006450 |         regulation of translational fidelity | 40 | 40 | 3.67 | < 1e-30
9 GO:0007165 |                          signal transduction | 3081 | 337 | 282.49 | < 1e-30
10 GO:0071816 | tail-anchored membrane protein insertion... | 38 | 36 | 3.48 | < 1e-30
11 GO:0051126 |     negative regulation of actin nucleation | 28 | 28 | 2.57 | < 1e-30
12 GO:0055114 |                 oxidation-reduction process | 558 | 72 | 51.16 | < 1e-30
13 GO:0015074 |                             DNA integration | 829 | 82 | 76.01 | < 1e-30
14 GO:0006412 |                                 translation | 143 | 77 | 13.11 | < 1e-30
15 GO:0000272 |            polysaccharide catabolic process | 24 | 22 | 2.20 | < 1e-30
16 GO:0044528 | regulation of mitochondrial mRNA stabili... | 18 | 17 | 1.65 | < 1e-30
17 GO:0007009 |                plasma membrane organization | 61 | 35 | 5.59 | 1.5e-26
18 GO:0070836 |                            caveola assembly | 14 | 14 | 1.28 | 1.7e-26
19 GO:0006284 |                        base-excision repair | 63 | 22 | 5.78 | 8.8e-25
20 GO:0042254 |                         ribosome biogenesis | 152 | 25 | 13.94 | 5.9e-22
21 GO:0009058 |                        biosynthetic process | 1818 | 181 | 166.69 | 4.9e-20
22 GO:0006360 |           transcription by RNA polymerase I  | 10 | 10 | 0.92 | 3.9e-19
23 GO:0044237 |                  cellular metabolic process | 4890 | 375 | 448.35 | 1.2e-18
24 GO:0005975 |              carbohydrate metabolic process | 359 | 52 | 32.92 | 4.3e-16
25 GO:0042981 |             regulation of apoptotic process | 149 | 20 | 13.66 | 7.8e-14
26 GO:0031110 | regulation of microtubule polymerization... | 10 | 8 | 0.92 | 8.3e-14
27 GO:0055085 |                     transmembrane transport | 321 | 39 | 29.43 | 1.4e-12
28 GO:0009116 |                nucleoside metabolic process | 195 | 23 | 17.88 | 2.6e-12
29 GO:0015708 | silicic acid import across plasma membra... | 6 | 6 | 0.55 | 9.1e-12
30 GO:0009306 |                           protein secretion | 6 | 6 | 0.55 | 9.1e-12
31 GO:0044249 |               cellular biosynthetic process | 1726 | 161 | 158.25 | 1.2e-11
32 GO:0003333 |          amino acid transmembrane transport | 12 | 7 | 1.10 | 9.8e-11
33 GO:0006388 | tRNA splicing, via endonucleolytic cleav... | 50 | 11 | 4.58 | 1.3e-10
34 GO:0006189 |          'de novo' IMP biosynthetic process | 5 | 5 | 0.46 | 6.3e-10
35 GO:0002098 |            tRNA wobble uridine modification | 5 | 5 | 0.46 | 6.3e-10
36 GO:0006355 | regulation of transcription, DNA-templat... | 451 | 27 | 41.35 | 9.6e-10
37 GO:0019428 |              allantoin biosynthetic process | 4 | 4 | 0.37 | 4.4e-08
38 GO:0000105 |              histidine biosynthetic process | 4 | 4 | 0.37 | 4.4e-08  

#### *Cellular component*  

Description: Analysis of losses at the Cteno node  
Ontology: CC  
'weight01' algorithm with the 'fisher' test  
237 GO terms scored: 23 terms with p < 0.01  
Annotation data:  
    Annotated genes: 142451  
    Significant genes: 6234  
    Min. no. of genes annotated to a GO: 1  
    Nontrivial nodes: 128    

GO.ID | Term | Annotated | Significant | Expected | classicFisher
--- | --- | --- | --- | --- | ---
1 GO:0016021 |               integral component of membrane | 10347 | 1098 | 452.81 | < 1e-30
2 GO:0016020 |                                     membrane | 15188 | 1453 | 664.66 | < 1e-30
3 GO:0005761 |                       mitochondrial ribosome | 59 | 58 | 2.58 | < 1e-30
4 GO:0000813 |                              ESCRT I complex | 37 | 36 | 1.62 | < 1e-30
5 GO:0016592 |                             mediator complex | 162 | 54 | 7.09 | < 1e-30
6 GO:0031966 |                       mitochondrial membrane | 235 | 50 | 10.28 | < 1e-30
7 GO:0005576 |                         extracellular region | 339 | 69 | 14.84 | < 1e-30
8 GO:0005753 |  mitochondrial proton-transporting ATP sy... | 18 | 18 | 0.79 | < 1e-30
9 GO:0034719 |                       SMN-Sm protein complex | 18 | 18 | 0.79 | < 1e-30
10 GO:0008023 |     transcription elongation factor complex | 14 | 14 | 0.61 | 1.8e-27
11 GO:0005634 |                                     nucleus | 945 | 125 | 41.36 | 1.1e-25
12 GO:0031011 |                               Ino80 complex | 13 | 13 | 0.57 | 1.5e-25
13 GO:0005615 |                         extracellular space | 95 | 19 | 4.16 | 9.4e-18
14 GO:0016010 | dystrophin-associated glycoprotein compl... | 8 | 8 | 0.35 | 5.3e-16
15 GO:0005886 |                             plasma membrane | 137 | 15 | 6.00 | 2.3e-08  

#### *Molecular function*  

Description: Analysis of losses at the Cteno node  
Ontology: MF  
'weight01' algorithm with the 'fisher' test  
573 GO terms scored: 122 terms with p < 0.01  
Annotation data:  
    Annotated genes: 1507423  
    Significant genes: 192721  
    Min. no. of genes annotated to a GO: 1  
    Nontrivial nodes: 356    

GO.ID | Term | Annotated | Significant | Expected | classicFisher
--- | --- | --- | --- | --- | ---
1 GO:0016787 |                          hydrolase activity | 7070 | 1538 | 903.89 | < 1e-30
2 GO:0016491 |                     oxidoreductase activity | 1191 | 412 | 152.27 | < 1e-30
3 GO:0005515 |                             protein binding | 59949 | 8435 | 7664.36 | < 1e-30
4 GO:0008168 |                  methyltransferase activity | 1333 | 589 | 170.42 | < 1e-30
5 GO:0003824 |                          catalytic activity | 24210 | 5819 | 3095.20 | < 1e-30
6 GO:0016757 | transferase activity, transferring glyco... | 1432 | 354 | 183.08 | < 1e-30
7 GO:0022857 |          transmembrane transporter activity | 1234 | 329 | 157.76 | < 1e-30
8 GO:0008146 |                   sulfotransferase activity | 999 | 264 | 127.72 | < 1e-30
9 GO:0003697 |                 single-stranded DNA binding | 131 | 125 | 16.75 | < 1e-30
10 GO:0016791 |                         phosphatase activity | 348 | 201 | 44.49 | < 1e-30
11 GO:0016772 |  transferase activity, transferring phosp... | 1201 | 214 | 153.55 | < 1e-30
12 GO:0003676 |                         nucleic acid binding | 14298 | 1009 | 1827.97 | < 1e-30
13 GO:0008080 |                 N-acetyltransferase activity | 466 | 150 | 59.58 | < 1e-30
14 GO:0008757 |  S-adenosylmethionine-dependent methyltra... | 173 | 127 | 22.12 | < 1e-30
15 GO:0051537 |             2 iron, 2 sulfur cluster binding | 121 | 95 | 15.47 | < 1e-30
16 GO:0008270 |                             zinc ion binding | 2828 | 276 | 361.55 | < 1e-30
17 GO:0016747 |  transferase activity, transferring acyl ... | 1712 | 427 | 218.88 | < 1e-30
18 GO:0016810 |  hydrolase activity, acting on carbon-nit... | 277 | 110 | 35.41 | < 1e-30
19 GO:0005509 |                          calcium ion binding | 4367 | 321 | 558.31 | < 1e-30
20 GO:0005524 |                                  ATP binding | 2232 | 233 | 285.36 | < 1e-30
21 GO:0004144 |  diacylglycerol O-acyltransferase activit... | 64 | 64 | 8.18 | < 1e-30
22 GO:0005525 |                                  GTP binding | 1230 | 170 | 157.25 | < 1e-30
23 GO:0008171 |                 O-methyltransferase activity | 112 | 71 | 14.32 | < 1e-30
24 GO:0004064 |                        arylesterase activity | 54 | 54 | 6.90 | < 1e-30
25 GO:0003735 |           structural constituent of ribosome | 58 | 55 | 7.42 | < 1e-30
26 GO:0017176 |  phosphatidylinositol N-acetylglucosaminy... | 52 | 52 | 6.65 | < 1e-30
27 GO:0008374 |                   O-acyltransferase activity | 114 | 114 | 14.57 | < 1e-30
28 GO:0035091 |                 phosphatidylinositol binding | 1008 | 134 | 128.87 | < 1e-30
29 GO:0008484 |            sulfuric ester hydrolase activity | 441 | 122 | 56.38 | < 1e-30
30 GO:0046872 |                            metal ion binding | 8799 | 777 | 1124.93 | < 1e-30
31 GO:0050660 |          flavin adenine dinucleotide binding | 237 | 116 | 30.30 | < 1e-30
32 GO:0003953 |                   NAD+ nucleosidase activity | 42 | 42 | 5.37 | < 1e-30
33 GO:0016788 |  hydrolase activity, acting on ester bond... | 2310 | 557 | 295.33 | < 1e-30
34 GO:0071949 |                                  FAD binding | 141 | 57 | 18.03 | < 1e-30
35 GO:0070567 |                cytidylyltransferase activity | 47 | 41 | 6.01 | < 1e-30
36 GO:0003677 |                                  DNA binding | 4694 | 356 | 600.12 | < 1e-30
37 GO:0020037 |                                 heme binding | 335 | 72 | 42.83 | < 1e-30
38 GO:0003723 |                                  RNA binding | 1604 | 141 | 205.07 | < 1e-30
39 GO:0004869 |  cysteine-type endopeptidase inhibitor ac... | 130 | 52 | 16.62 | < 1e-30
40 GO:0016884 |  carbon-nitrogen ligase activity, with gl... | 33 | 33 | 4.22 | < 1e-30
41 GO:0004129 |                cytochrome-c oxidase activity | 154 | 54 | 19.69 | < 1e-30
42 GO:0003993 |                    acid phosphatase activity | 32 | 32 | 4.09 | < 1e-30
43 GO:0004842 |       ubiquitin-protein transferase activity | 478 | 77 | 61.11 | < 1e-30
44 GO:0002161 |              aminoacyl-tRNA editing activity | 34 | 32 | 4.35 | < 1e-30
45 GO:0004423 |               iduronate-2-sulfatase activity | 26 | 26 | 3.32 | < 1e-30
46 GO:0016798 |  hydrolase activity, acting on glycosyl b... | 200 | 116 | 25.57 | < 1e-30
47 GO:0045145 |  single-stranded DNA 5'-3' exodeoxyribonu... | 25 | 25 | 3.20 | < 1e-30
48 GO:0004553 |  hydrolase activity, hydrolyzing O-glycos... | 48 | 33 | 6.14 | < 1e-30
49 GO:0030246 |                         carbohydrate binding | 469 | 75 | 59.96 | < 1e-30
50 GO:0008773 |  [protein-PII] uridylyltransferase activi... | 24 | 24 | 3.07 | < 1e-30
51 GO:0010181 |                                  FMN binding | 88 | 35 | 11.25 | < 1e-30
52 GO:0008237 |                    metallopeptidase activity | 792 | 84 | 101.26 | < 1e-30
53 GO:0015035 |  protein disulfide oxidoreductase activit... | 49 | 28 | 6.26 | < 1e-30
54 GO:0043531 |                                  ADP binding | 23 | 21 | 2.94 | < 1e-30
55 GO:0003847 |  1-alkyl-2-acetylglycerophosphocholine es... | 19 | 19 | 2.43 | < 1e-30
56 GO:0008289 |                                lipid binding | 1660 | 193 | 212.23 | < 1e-30
57 GO:0008233 |                           peptidase activity | 1257 | 129 | 160.70 | < 1e-30
58 GO:0017022 |                               myosin binding | 16 | 16 | 2.05 | < 1e-30
59 GO:0004867 |  serine-type endopeptidase inhibitor acti... | 749 | 61 | 95.76 | < 1e-30
60 GO:0004346 |               glucose-6-phosphatase activity | 15 | 15 | 1.92 | 1.1e-29
61 GO:0016746 |  transferase activity, transferring acyl ... | 2313 | 490 | 295.71 | 5.2e-29
62 GO:0005507 |                           copper ion binding | 103 | 27 | 13.17 | 1.5e-28
63 GO:0008119 |      thiopurine S-methyltransferase activity | 14 | 14 | 1.79 | 9.2e-28
64 GO:0004055 |          argininosuccinate synthase activity | 14 | 14 | 1.79 | 9.2e-28
65 GO:0016279 |  protein-lysine N-methyltransferase activ... | 40 | 16 | 5.11 | 7.9e-26
66 GO:0016874 |                              ligase activity | 362 | 79 | 46.28 | 8.1e-25
67 GO:0043022 |                             ribosome binding | 42 | 18 | 5.37 | 4.7e-24
68 GO:0051539 |             4 iron, 4 sulfur cluster binding | 23 | 15 | 2.94 | 4.9e-24
69 GO:0035438 |                        cyclic-di-GMP binding | 12 | 12 | 1.53 | 6.7e-24
70 GO:0051536 |                  iron-sulfur cluster binding | 163 | 124 | 20.84 | 9.3e-24
71 GO:0016829 |                               lyase activity | 302 | 53 | 38.61 | 1.2e-21
72 GO:0016765 |  transferase activity, transferring alkyl... | 243 | 32 | 31.07 | 7.1e-21
73 GO:0016783 |                   sulfurtransferase activity | 21 | 17 | 2.68 | 4.9e-20
74 GO:0005085 |  guanyl-nucleotide exchange factor activi... | 809 | 48 | 103.43 | 2.3e-19
75 GO:0003950 |         NAD+ ADP-ribosyltransferase activity | 353 | 32 | 45.13 | 1.2e-18
76 GO:0016763 |  transferase activity, transferring pento... | 400 | 49 | 51.14 | 2.6e-18
77 GO:2001070 |                               starch binding | 24 | 11 | 3.07 | 1.2e-15
78 GO:0016836 |                         hydro-lyase activity | 85 | 15 | 10.87 | 2.9e-15
79 GO:0030414 |                 peptidase inhibitor activity | 1154 | 130 | 147.54 | 2.9e-15
80 GO:0004843 |  thiol-dependent ubiquitin-specific prote... | 70 | 15 | 8.95 | 4.3e-15
81 GO:0046912 |  transferase activity, transferring acyl ... | 33 | 12 | 4.22 | 5.9e-14
82 GO:0004518 |                            nuclease activity | 296 | 42 | 37.84 | 1.7e-13
83 GO:0008658 |                           penicillin binding | 8 | 7 | 1.02 | 2.4e-13
84 GO:0004222 |                metalloendopeptidase activity | 66 | 13 | 8.44 | 9.0e-13
85 GO:0043565 |                sequence-specific DNA binding | 130 | 16 | 16.62 | 4.4e-12
86 GO:0004792 |       thiosulfate sulfurtransferase activity | 11 | 7 | 1.41 | 9.6e-12
87 GO:0004857 |                    enzyme inhibitor activity | 1208 | 141 | 154.44 | 3.2e-11
88 GO:0000049 |                                 tRNA binding | 55 | 11 | 7.03 | 4.3e-11
89 GO:0043169 |                               cation binding | 8873 | 792 | 1134.40 | 1.1e-10
90 GO:0016743 |  carboxyl- or carbamoyltransferase activi... | 5 | 5 | 0.64 | 2.2e-10
91 GO:0003714 |           transcription corepressor activity | 5 | 5 | 0.64 | 2.2e-10
92 GO:0005096 |                    GTPase activator activity | 304 | 20 | 38.87 | 9.8e-10
93 GO:0016831 |                       carboxy-lyase activity | 38 | 11 | 4.86 | 6.3e-09
94 GO:0046982 |          protein heterodimerization activity | 525 | 25 | 67.12 | 6.8e-09
95 GO:0003855 |        3-dehydroquinate dehydratase activity | 4 | 4 | 0.51 | 1.9e-08
96 GO:0005212 |           structural constituent of eye lens | 4 | 4 | 0.51 | 1.9e-08
97 GO:0019239 |                           deaminase activity | 104 | 11 | 13.30 | 4.7e-08  
