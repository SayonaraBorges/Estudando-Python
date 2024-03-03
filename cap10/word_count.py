def count_words(filename):
    """Conta o número aproximado de palavras em um arquivo.""" 
    try: 
        with open(filename) as f_obj: 
            contents = f_obj.read() 
    except FileNotFoundError: 
        #msg = "Sorry, the file " + filename + " does not exist."
        #print(msg) 
        pass
    else: 
        words = contents.split() 
        num_words = len(words) 
        print("The file " + filename + " has about " + str(num_words) + " words.") 
        filename = 'alice.txt' 
        count_words(filename)


filenames = ['text_files/alice.txt', 'siddhartha.txt', 'text_files/programming.txt', 'text_files/respostas.txt']

for filename in filenames: 
    count_words(filename)