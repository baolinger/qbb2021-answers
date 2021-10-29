#from pysam import FastaFile
import numpy as np
import sys
import Bio
import pandas as pd
import numpy as np

#read in fasta file 
fasta = sys.argv[1]
score = sys.argv[2]
gap = int(sys.argv[3])
output = sys.argv[4]

#sequences_object = FastaFile(fasta)
#tmp_sequence = fasta.fetch("ENSP00000264010.4")
#print(temp_sequence)

from Bio import SeqIO

import fastaparser

#Make list and fill with 2 fasta sequences 
sequence = []
with open(fasta) as fasta_file:
        parser = fastaparser.Reader(fasta_file)
        for seq in parser:
            # seq is a FastaSequence object
            sequence.append(seq.sequence_as_string())

print(sequence[0][5])

#read in scoring matrix 
score = pd.read_csv(score, sep='\s+', header=0, index_col=0)
#print(score.loc["R","R"])

#creates 2 matrices with columns and rows equal to the length of the sequences
n = len(sequence[0])
m = len(sequence[1])

F_matrix = pd.DataFrame(np.random.randint(0,1, size=(n+1,m+1)))
T_matrix = pd.DataFrame(np.random.randint(0,1, size=(n+1,m+1)))

##Fill in the f matrix 
#gaps first
for i in range(len(sequence[0])+1):
	F_matrix.iloc[i,0] = i*gap

for j in range(len(sequence[1])+1):
	F_matrix.iloc[0,j] = j*gap

#all other values
print(score.loc[sequence[0][5],sequence[1][5]])
print(F_matrix.iloc[1, 1])



for i in range(1, len(sequence[0])+1): # loop through rows
	for j in range(1, len(sequence[1])+1): # loop through columns
		if sequence[0][i-1] == sequence[1][j-1]: # if sequence1 and sequence2 match at positions i and j, respectively...
			d = F_matrix.iloc[i-1, j-1] + score.loc[sequence[0][i-1],sequence[1][j-1]]
		else: # if sequence1 and sequence2 don't match at those positions...
			d = F_matrix.iloc[i-1, j-1] + score.loc[sequence[0][i-1],sequence[1][j-1]]
		h = F_matrix.iloc[i,j-1] - gap
		v = F_matrix.iloc[i-1,j] - gap

		F_matrix.iloc[i,j] = max(d,h,v)

#print(F_matrix)

###Find highest scoring alignment, while building optimal sequences 
#create empty variables
seq1=""
seq1_gaps = 0
seq1_counter = len(sequence[0]) -1
seq2=""
seq2_gaps = 0
seq2_counter = len(sequence[1]) -1
#pull co

#find alignment score
align_score = F_matrix.iloc[len(F_matrix)-1,len(F_matrix[0])-1]

#build alignments
i=1
iterations = 0
while i > 0:
	if iterations == 0:
		seq1= seq1 + sequence[0][seq1_counter]
		seq2= seq2 + sequence[1][seq2_counter]
		iterations += 1
	d = F_matrix.iloc[seq1_counter-1, seq2_counter-1]
	h = F_matrix.iloc[seq1_counter,seq2_counter-1]
	v = F_matrix.iloc[seq1_counter-1,seq2_counter]
	if d == max(d,v,h):
		seq1_counter = seq1_counter -1
		seq1 = seq1 + sequence[0][seq1_counter]
		seq2_counter = seq2_counter -1
		seq2 = seq2 + sequence[1][seq2_counter]
	elif v == max(d,v,h):
		seq1_counter = seq1_counter -1
		seq1 = seq1 + sequence[0][seq1_counter]
		seq2 = seq2 + "-"
		seq2_gaps += 1
	elif h == max(d,v,h):
		seq2_counter = seq2_counter -1
		seq2 = seq2 + sequence[1][seq2_counter]
		seq1 = seq1 + "-"
		seq1_gaps += 1
	if seq1_counter == 0:
		i = 0 

#write output file
text_file = open(output, "w")
text_file.write(seq1)
text_file.write("\n")
text_file.write(seq2)
text_file.write("\n")
text_file.write("Number of gaps in seq1: ")
text_file.write(str(seq1_gaps))
text_file.write("\n")
text_file.write("Number of gaps in seq2: ")
text_file.write(str(seq2_gaps))
text_file.write("\n")
text_file.write("Alignment score: ")
text_file.write(str(align_score))










