#added line 7, 26, 27 based on feedback

import sys
target = sys.argv[1]
query = sys.argv[2]
#add this line based on feedback; add additional command line argument for kmer size
kmer_size = sys.argv[3]

from fasta_reader import FASTAReader

# Load sequences
#target
target_seqs = FASTAReader(open(target))
#query
query_seqs = FASTAReader(open(query))
# We only need the first query sequence
query_seq = query_seqs[0][1]

# Loop through target_seqs

#initialize blank dictionary 
kmers = {}

#set kmer size
k = 11
#added this from feedback; set kmer size to command line supplied command
k = open(kmer_size)

#create dictionary that will determine all kmers in 
#target sequence and their locations
for seq_id, sequence in target_seqs:
    #set sequence to all uppercase
    sequence = sequence.upper()
    #create dictionary for all kmers
    for i in range(0, len(sequence) - k):
        kmer = sequence[i:i + k]
        kmers.setdefault(kmer, [])
        kmers[kmer].append((seq_id,i))

#Uncomment these to print dictrionary of target kmers
#for key in kmers:
#print(key, kmers[key])

#iterate through query sequence, finding all kmers
#if the kmer is present in the target sequence:
    #prints the location of the kmer in the quesry sequence and the target sequences 
for seq_id, sequence in query_seqs:
    sequence = sequence.upper()
    for i in range(0, len(sequence) - k):
        kmer = sequence[i:i + k]
        if kmer in kmers:
            print(kmer, i, kmers[kmer])
