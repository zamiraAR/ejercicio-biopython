def summarize_contents(filename):
       avance = SeqIO.read(filename, "genbank")
        print("Name: ", avance.name)
        import os
        print ("Path: ", os.path.dirname(filename))
       avances = list(SeqIO.parse(filename, "genbank"))
        print("num_avances = %i avances" % len(avance))

        for seq_record in SeqIO.parse(filename,"genbank"):
                print("ID:",avance.id)
                
summarize_contents(filename)
