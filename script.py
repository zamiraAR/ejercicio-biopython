from bio.seq import seq
from bio.seqFeature import seqFeature, FeatureLocation
from Bio import seqRecord
def summarize_contens(filename):
    record = seqIO.read(filename, "getbank")
    print(record)
 summarize_contents(filename)
