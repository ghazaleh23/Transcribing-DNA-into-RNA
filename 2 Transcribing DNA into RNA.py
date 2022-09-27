'''An RNA string is a string formed from the alphabet containing 'A', 'C', 'G', and 'U'.
Given a DNA string t corresponding to a coding strand,
its transcribed RNA string u is formed by replacing all occurrences of
'T' in t with 'U' in u.'''
DNA='GATGGAACTTGACTACGTAAATT'
DNA_list = list(DNA)
for i in range(len(DNA)) :
    if DNA[i] == "T" :
        DNA_list[i] = "U"
RNA = ""
for i in DNA_list :
    RNA += i        