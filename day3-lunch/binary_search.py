import sys

gtf_file = sys.argv[1]
mut_chrom = sys.argv[2]
mut_pos = int(sys.argv[3])
f = open(gtf_file)

#parsing genes file
genes = []
for line in f:
    if line.startswith("#"):
        continue
    fields = line.strip("\r\n").split("\t")
    start = int(fields[3])
    end = int(fields[4])
    if (fields[0] == mut_chrom) and (fields[2] == "gene") and ('gene_biotype "protein_coding"' in line):
        subfields = fields[-1].split(';')
        for field in subfields:
            if "gene_name" in field:
                gene_name = field.split()[1]
        genes.append((gene_name, start, end))

#print(genes)

#Find first mid, high, low values
low = int(0)
high = int(len(genes) -1)
mid = int((high + low)/2)

#Initialize counter to record number of iterations
iterations_counter = 0

#Initialize While condition 
while_condition = False

# Initialize old mid to keep track of mid in previous while loop
old_mid = None 

#Initialize variable to hold the length away from the mutation for 2 genes: length from start position for high gene, legnth from end position for high gene; this runs if the mutation position is not present in the range of any gene
length_gene_high = None
length_gene_low = None

#While loop that test if any entry in genes is present in or adjacent to the query position
while while_condition == False:
    iterations_counter += 1
    #print(iterations_counter)
    #print(mid)
    #Check if the mutation position is present in
    #the range of the middle gene
    if mut_pos in range(genes[mid][1],genes[mid][2]+1):
        while_condition = True
        print("Gene:", genes[mid])
        print(iterations_counter)
        break
    #If the mutation position is below the start of the middle gene, reassign high
    if mut_pos < genes[mid][1]:
        high = mid 
    #If the mutation position is above the end of the middle gene, reassign low
    if mut_pos > genes[mid][2]:
        low = mid 
    old_mid = mid
    mid = int((high + low)/2)
    # if the middle does not change, end the while loop and test to see which genes are closer to the mutation position 
    if old_mid == mid:
        while_condition = True 
        #find the distance between the start of the high gene and the mutation position
        length_gene_high = (genes[high][1] - mut_pos)
        #find the distance between the end of the low gene and the mutation position; print the one that is closest
        length_gene_low = (mut_pos - genes[low][2])
        if int(length_gene_high) < int(length_gene_low):
            print("Closest gene:", genes[high])
            print("Linear Gen Dist:",length_gene_high)
            print("Iterations:",iterations_counter)
        if int(length_gene_low) < int(length_gene_high):
            print("Closest gene:",genes[low])
            print("Linear Gen Dist:",length_gene_low)
            print("Iterations:",iterations_counter)



