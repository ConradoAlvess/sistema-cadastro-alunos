# Sistema de Cadastro de Alunos

Projeto simples em Python desenvolvido para praticar lógica de programação, funções, listas, dicionários, estruturas de repetição e condicionais.

## Funcionalidades

- Cadastro de alunos
- Validação para impedir alunos duplicados
- Login de alunos
- Visualização dos alunos cadastrados
- Lançamento de notas
- Cálculo de média
- Exibição de aprovação ou reprovação

## Tecnologias utilizadas

- Python 3

## Estrutura do aluno

Cada aluno é armazenado em uma lista como um dicionário contendo:

- Nome
- Ano/Série
- Senha
- Notas

Exemplo:

```python
{
    "nome": "Gustavo",
    "ano": "2º ano",
    "senha": "1234",
    "notas": [7.0, 8.5, 6.0]
}
