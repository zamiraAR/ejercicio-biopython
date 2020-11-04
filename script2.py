def summarize_contents(filename):
	listOs = os.path.split(filename)
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
#print
if name == "main":
	result = summarize_contents(filename)
	print(result)
