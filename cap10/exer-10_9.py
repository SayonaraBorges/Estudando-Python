files = ['text_files/cats.txt', 'text_files/dogs.txt']

def read_paper(files):
        for f in files: 
            try:
                with open(f) as f_obj:
                    doc_lido = f_obj.read()
                    print(doc_lido)
                    print(" ")
            except FileNotFoundError:
                pass
    
read_paper(files)