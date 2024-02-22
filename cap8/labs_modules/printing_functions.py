def print_models(unprinted_designs, completed_models):
    while unprinted_designs: 
        """ Simula a impressão de cada design, até que não haja mais nenhum.
            Transfere cada design para completed_models após a impressão""" 
        current_design = unprinted_designs.pop()
        # Simula a criação de uma impressão 3D a partir do design 
        print("Printing model: " + current_design)
        completed_models.append(current_design)

def show_completed_models(completed_models):
    """Exibe todos os modelos finalizados """
    print("\nThe following models have been printed:")
    for completed_model in completed_models: 
        print(completed_model)