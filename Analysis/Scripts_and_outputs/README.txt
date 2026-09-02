This file contains the description of the preparation of the GPCR data for alphafold simulations. 

WholeProteomePDBs was downloaded from the Mnemiopsis server available at: https://research.nhgri.nih.gov/mnemiopsis/jbrowse/jbrowse.cgi. The whole proteome sequences were also downloaded here.

Step 0.
Use the Annotation excel file from M. leidyi which includes characterization of different GPCRs and filter by classA 7tm1 class. Obtain the IDs from those GPCRs and store them in the Accessions.txt

Step 1. Use Accessions.txt as input for the 1_Accession_Filter.py script. This script takes the accessions available in the Accessions.txt file and looks for matching PDBs in the WholeProteomePDBs directory. The matching PDBs will be copied into Filtered_GPCRs directory

Step 2. Use 2_ClassA_filtersequence.py to take the accessions of the ClassA GPCRs and obtain a list of only class A GPCR sequences that will be used in step3

Step 3. Use 3_length_filtered.py to take the filtered_sequences.fasta file and use it to filter the Filtered_GPCRs directory and copy the files whose name match the ones available in filtered_sequences.fasta. The output will be a directory containing PDBs which are at minimum 225 Aminoacids

Step 4. Filter the length-filtered sequences using cdhit. Cdhit is a Linux-installed program which groups all the sequences and reduces any redundancies in the sequences, and only consider a representative one. 

Step 5. Apply pLDDT_filter.py to reduce to 234 sequences. plddt_seq.fasta will contain the accessions but then also onelineseq.fasta will contain the GPCR sequences that will be used for Alphafold sequences during the HPC script