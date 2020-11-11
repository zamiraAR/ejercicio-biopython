from Bio.Seq import Seq
from Bio import SeqIO
from Bio.SeqRecord import SeqRecord
import os

filename = os.path.abspath("data/ls_orchid.gbk")

def summarize_contents(filename):
	listaOs = os.path.split(filename)
	listExt = os.path.splitext(filename)
	if (listExt[1] == ".gbk"):
		type_file= "genbank"
	else:
		type_file= "fasta"
	record = list(SeqIO.parse(filename, type_file))

	dictionary = {}
	dictionary['File:'] = listaOs[1]
	dictionary['Path:'] = listaOs[0]
	dictionary['Num_records:'] = len(record)

	dictionary['Names:'] = []
	dictionary['IDs:'] = []
	dictionary['Descriptions'] = []

	for seq_rcd in SeqIO.parse(filename,type_file):
		dictionary['Names:'].append(seq_rcd.name)

		dictionary['IDs:'].append(seq_rcd.id)
		dictionary['Descriptions'].append(seq_rcd.description)
	return dictionary

if __name__ == "__main__":
	result = summarize_contents(filename)
	print(result)


cadena_1 = input ("ingresar la primera secuencia de ADN: ")
cadena_2 = input ("ingresar la segunda secuencia de ADN: ")

Sequencia_1 = Seq(cadena_1)
Sequencia_2 = Seq(cadena_2)

def concatenate_and_get_reverse_of_complement(Sequencia_1, Sequencia_2):
	concatenar = Sequencia_1 + Sequencia_2
	inversa = concatenar.reverse_complement()

	return (inversa)

if __name__ == "__main__":
	result_2 = concatenate_and_get_reverse_of_complement(Sequencia_1, Sequencia_2)
	print (result_2)

