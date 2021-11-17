# databricks-page-exam

Repositório com o projeto de simulado da prova para certificação Databricks.

Neste momento, somente a versão par ser usada no prompt ou shell está dispoinível.

## Tecnologias

* Python 3

## Usuários

Para usar o programa é recomendado possuir conhecimentos básicos em Python 3 e Inglês.

## Dados da prova

Na pasta `exam_db` contém:

 - 1 arquivo de texto com as perguntas;
 - 1 arquivo de texto com as respostas (1 por linha);
 - 1 arquivo python que converte o conteúdo do arquivo com as questões no formato json e salva em um outro arquivo. Esse arquivo poderá ser usado para aplicação do simulado.

## Simulados

Assim como na prova real, são um conjunto de 60 questões, o usuário precisa fazer a prova em 2 horas.

### Versão para prompt de comando ou Shell

Na pasta src/python contém o código fonte para execução do simulado da prova usando da python no prompt de comando ou shell do sistema operacional.

#### Arquivos da pasta src/python

- classes/exam.py: Código do correspondente a classe que representa o teste
- main.py: Arquivo que simula o teste.
- data/*: Arquivos de dados com as questões.

#### Formatos de arquivos de dados

**Arquivo com as questões**

```json
{
    "questions": [
        {
            "id": 1,
            "options": [
                "A. Option",
                "B. Option",
                "C. Option",
                "D. Option",
                "E. Option"
            ],
            "description": ""
        },
    ]
}
```

**Arquivo com as respostas**

```
1. A
2. B
...
```

## Classe *Exam*

A Classe é o que permite a execução do simulado.  
Em temp ode execução ela apresenta 3 estados:

- "I" (Init), quando o objeto da classe é criado.
- "R" (Running), quando o teste é iniciado, `startExam()`
- "F" (Finished), quando o teste é finalizado, `stopExam()`

