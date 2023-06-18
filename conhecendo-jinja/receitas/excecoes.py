# from jinja2 import Environment
# from filtros.converte_para_lista import converte_para_lista

# loader = FileSystemLoader('receitas/templates')

# environment = Environment(loader=loader)
# environment.filters['converte_para_lista'] = converte_para_lista

# template = environment.get_template('index.html')

# output = template.render(data)

# print(output)


from jinja2 import Environment, TemplateNotFound, FileSystemLoader

saudacoes = {
    'manha': 'Bom dia',
    'tarde': 'Boa tarde',
    'noite': 'Boa noite'
}

try:
    loader = FileSystemLoader('templates')

    environment = Environment(loader=loader)

    template = environment.get_template('saudacao.html')

    output = template.render(saudacao)
except TemplateNotFound as e:
    print(f'Erro: Template "{str(e)}" não encontrado')
except Exception as e:
    print(f'Erro: {str(e)}')
else:
    print(output)
finally:
    print("Fim do programa")
