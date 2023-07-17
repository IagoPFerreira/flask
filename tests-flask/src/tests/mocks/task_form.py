task_form = {
    'open': '<form method="post" class="new-task">',
    'name': '''<label for="name">Task
            <input type="text" name="name" id="name" required>
        </label>''',
    'status': '''<label for="status">Status
            <select name="status" id="status">
                <option value="Não iniciado">Não iniciado</option>
                <option value="Em progresso">Em progresso</option>
                <option value="Concluído">Concluído</option>
                <option value="Atrasado">Atrasado</option>
            </select>
        </label>''',
    'percentage': '''<label for="porcentagem">Porcentagem de conclusão
            <input type="number" name="porcentagem" id="porcentagem" required>
        </label>''',
    'description': '''<label for="descripton">Descrição da task
            <textarea type="text" name="descripton" id="descripton" required></textarea>
        </label>''',
    'date': '''<label for="deadline">Deadline limite
            <input type="date" name="deadline" id="deadline" required>
        </label>''',
    'responsible': '''<label for="responsible">Responsável
            <input type="text" name="responsible" id="responsible" required>
        </label>''',
    'send': '<button type="submit">Enviar</button>',
    'close': '</form>'
}

form_deadline = {
    'name': 'Restaurar project',
    'status': 'Não iniciado',
    'porcentagem': 0,
    'descripton': 'Restaurar project deletado',
    'deadline': '2023-07-15',
    'responsible': 'Thiago Silva'
}

added_task = {
    'open': '<section class="task-home">',
    'name': '<p>Restaurar project</p>',
    'status': '<p>Não iniciado</p>',
    'responsible': '<p>Thiago Silva</p>'
}
