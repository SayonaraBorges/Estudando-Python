class Employee():
    def __init__(self, nome, sobrenome, salario_anual):
        """Inicializa um funcinário com nome, sobrenome e salário anual."""
        self.nome = nome
        self.sobrenome = sobrenome
        self.salario_anual = salario_anual
    
    def give_raise(self, aumento=5000):
        """Realiza aumento de $5.000,00 ou outro valor no salário anual."""
        self.salario_anual += aumento

empregado1 = Employee("Sandra", "Borges", 60000)
print(f"Salário anual antes do aumento: ${empregado1.salario_anual}")
empregado1.give_raise()
print(f"Salário anual após o aumento padrão: ${empregado1.salario_anual}")
empregado1.give_raise(3000)
print(f"Salário anual após um aumento personalizado: ${empregado1.salario_anual}")
