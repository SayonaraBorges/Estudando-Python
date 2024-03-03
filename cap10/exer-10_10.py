filenames = ['text_files/Mindset_resumo_livro.txt', 'text_files/A coragem de ser imperfeito_resumo_livro.txt']

def count_words(filenames, specific_word):
    """Conta o número aproximado de palavras em um arquivo.""" 
    for filename in filenames: 
        try: 
            with open(filename) as f_obj: 
                contents = f_obj.read() 
        except FileNotFoundError: 
            print(f"!!Erro: arquivo '{filename}' não encontrado!!")
        else: 
            words = contents.split() 
            num_words = len(words) 
            print(f"O arquivo <{filename}> tem cerca de {str(num_words)} palavras.") 
            num_specific_words = words.count(specific_word)
            print(f"A palavra '{specific_word}' ocorre {str(num_specific_words)} vezes no texto contido no arquivo <{filename}>.")
            print(" ")

count_words(filenames, 'ser')