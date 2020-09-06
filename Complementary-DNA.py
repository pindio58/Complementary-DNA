def dna_strand (dna):
    word = ''

    for letter in dna:
        if letter == 'A': word += 'T'
        if letter == 'T': word += 'A'
        if letter == 'G': word += 'C'
        else: word += 'G'

    return word
