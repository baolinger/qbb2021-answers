Almost perfect! A couple of small points:
1. Your program should read the kmer length in as a command line argument, rather than defining it in the script itself
2. You're actually skipping the last kmer in each sequence. Try modifying `range(0, len(sequence) - k)`
3. The columns of your output aren't quite in the order we asked for, but we're not going to penalize you for this
