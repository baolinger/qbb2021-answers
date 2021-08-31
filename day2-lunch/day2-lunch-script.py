import sys
fly_mapping = sys.argv[1]
c_tab_name = sys.argv[2]

#blank dictionary to fill
map_dict = {}
#open ctab file
fly_map = open(fly_mapping)
for line in fly_map:
    entry = line.strip("\n").split('\t')
    map_dict[entry[0]] = entry[1] 


if len(sys.argv) == 3:
    #open ctab file
    ctab = open(c_tab_name)
    #replace gene ID with protein ID in mapping file
    for line in ctab:
        entry = line.strip("\n").split('\t')
        if entry[8] in map_dict:
            entry[8] = map_dict[entry[8]]
            print(("\t").join(entry))

if len(sys.argv) == 4:
    missing_text = sys.argv[3]
    #open missing argument
    # missing_text = open(missing_text)
    #open ctab file
    ctab = open(c_tab_name)
    #replace gene ID with protein ID in mapping file
    for line in ctab:
        entry = line.strip("\n").split('\t')
        if entry[8] in map_dict:
            entry[8] = map_dict[entry[8]]
        else:
            entry[8] = missing_text
        print(("\t").join(entry))
        

