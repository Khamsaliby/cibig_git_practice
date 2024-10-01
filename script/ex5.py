#• Create a python program exo5.py which, starting from the nucleic sequence (character string)
from itertools import count

sequence = "TCTGTTAACCATCCACTTCG"
#Convert str to list
sequence_list  = list(sequence)

# Create it inverse sequence,
sequence_list.reverse()

#Displays it.
print(sequence_list)
len_list_seq = len(sequence_list)
print(len_list_seq)

a = sequence_list.count("A")
t = sequence_list.count("T")
c = sequence_list.count("C")
g = sequence_list.count("G")

ind_list = [a,c,t,g]
print(ind_list)

#print(list(enumerate(animal_list)))
for Nucleotides ,i  in enumerate(ind_list):
    print(f"indice : {indice}, element : {i}")



