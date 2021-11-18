# databricks-page-exam

Repositório com o projeto de simulado da prova para certificação Databricks.

Neste momento, somente a versão par ser usada no prompt ou shell está dispoinível.

## Tecnologias

* Python 3

## Usuários

Para usar o programa é recomendado possuir conhecimentos básicos em Python 3, Databricks Community(opcional) e Inglês.

## Dados da prova

Na pasta `exam_db` contém:

 - 1 arquivo de texto com as perguntas;
 - 1 arquivo de texto com as respostas (1 por linha);
 - 1 arquivo python que converte o conteúdo do arquivo com as questões no formato json e salva em um outro arquivo. Esse arquivo poderá ser usado para aplicação do simulado.

## Simulados

Assim como na prova real, são um conjunto de 60 questões, o usuário precisa fazer a prova em 2 horas.  

### Versão Notebook do Databricks

Na pasta `src/notebooks` existem 2 arquivos referentes ao simulado, um arquivo Jupyter Notebook com 60 perguntas originárias das provas de certificação para consulta e outro arquivo no formato dbc.

O arquivo dbc  pode ser importado no ambiente da Databricks Community. Esse arquivo possui compactado os seguintes notebooks:

- include/exam: Arquivo com a implementação da classe `Exam` com os dados da pergunta. Serve como base para execução dos demais notebooks. A classe `Exam` do notebook foi implementada de forma semelhante a implementação da versão para prompt de comando desse simulado.
- Exam1A: Arquivo com todas as perguntas do exame de forma ordenada, onde o usuário pode responder as perguntas e verificar sua quantidade de acertos.  
- Exam1B: Exibe de forma aleatória 1 pergunta por vez. O usuário pode responder as perguntas e no final do exame verificar sua quantidade de acertos. Funciona de forma semelhante a versão para shell desse simulado.

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
Em tempo de execução ela apresenta 3 estados:

- "I" (Init), quando o objeto da classe é criado.
- "R" (Running), quando o teste é iniciado, `startExam()`
- "F" (Finished), quando o teste é finalizado, `stopExam()`

