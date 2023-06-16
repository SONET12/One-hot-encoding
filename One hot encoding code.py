from Bio import SeqIO
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import OneHotEncoder
import numpy as np
import re

def string_to_array(seq_string):
    seq_string = seq_string.lower()
    seq_string = re.sub('[^acgt]', 'n', seq_string)
    seq_string = np.array(list(seq_string))
    return seq_string

label_encoder = LabelEncoder()
label_encoder.fit(np.array (['a', 'c', 'g', 't', 'z',]))

def one_hot_encoder(seq_string):
    int_encoded = label_encoder.transform(seq_string)
    onehot_encoder = OneHotEncoder (sparse= False, dtype= int)
    int_encoded = int_encoded.reshape(len(int_encoded), 1)
    onehot_encoded = onehot_encoder.fit_transform(int_encoded)
    onehot_encoded = np.delete(onehot_encoded, -1, 1)
    return onehot_encoded

with open('One_hot_output.txt', 'w') as outfile:
    for sequence in SeqIO.parse("file format", "fasta"):
        sequence_string = str(sequence.seq)
        encoded_sequence = one_hot_encoder(string_to_array(sequence_string))
        outfile.write(f'>{sequence.id}\n')
        outfile.write(f'{sequence_string}\n')
        outfile.write(f'{encoded_sequence}\n')