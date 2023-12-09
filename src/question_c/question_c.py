#write functions here, don't add input('') statements here!
def get_most_likely_ancestor_consensus(dna_string1, dna_string2):
    count = 0
    outputValues = []
    len1 = len(dna_string1)
    #print("Len1 = ", len1)

    while count < len1:
        index = dna_string1.find(dna_string2, count, len1)
        #print("Index = ", index)
        if index != -1:
            count = index + 1
            outputValues.append(index + 1)
        else:
            count += 1
        #print("Count = ", count)
    return tuple(outputValues)

