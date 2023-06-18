try:
    # Código que pode gerar exceções
    resultado = 10 / 2  # Divisão por zero
except ZeroDivisionError:
    # Tratamento específico para a exceção ZeroDivisionError
    print("Erro: Divisão por zero não é permitida.")
except Exception as e:
    # Tratamento genérico para todas as outras exceções
    print("Erro: ", str(e))
else:
    # Executado se nenhuma exceção for levantada
    print("Resultado:", resultado)
finally:
    # Sempre executado, independentemente de exceções
    print("Fim do programa.")

# resultado = 10 / 0
# print("Resultado:", resultado)
# print("Fim do programa.")
