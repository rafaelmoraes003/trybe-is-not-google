<h1 align="left">Trybe Is Not Google (TING)</h1>

###

<p align="left">In this project, a program was implemented to simulate a document indexing algorithm similar to Google's. The program is able to identify occurrences of terms in TXT files.</p>

###

<h2 align="left">Technologies used</h2>

###

<div align="left">
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg" height="50" width="62" alt="python logo"  />
</div>

###

<h2 align="left">How to use the application</h2>

###

Clone the application using the git clone command. After that, enter the project folder using the command `cd trybe-is-not-google`.

###

<h2 align="left">How to run the application</h2>

###

1. Create the virtual environment for the project
 - `python3 -m venv .venv && source .venv/bin/activate`
 
2. Install the dependencies
- `python3 -m pip install -r dev-requirements.txt`

###

<h2 align="left">Using the indexing tool</h2>

Use the `python3 -m ting_word_searches.word_search` command to be able to use the tool.

<h3 align="left">Explanation</h3>

The process function is responsible for adding data from files in the queue (this function takes as arguments `the path of the file with the data` and an `instance of the Queue class`.

After the class instance has passed the `process` function, it can be used in the search tool.

The `exists_word` and `search_by_word` functions take two arguments: `the word to be searched for` and an `instance of the Queue class`.

The return of the `exists_word("sistema", queue_instance)` function is something like:

```Python
[
  {
    "palavra": "sistema",
    "arquivo": "statics/new_globalized_paradigm-min.txt",
    "ocorrencias": [
        {"linha": 12},
        {"linha": 18}
     ],
  },
]
```

Similarly, the return of the `search_by_word("sistema", queue_instance)` function is something like:

```Python
[
  {
    "palavra": "sistema", 
    "arquivo": "statics/novo_paradigma_globalizado-min.txt", 
    "ocorrencias": [
        {
          "linha": 12, 
          "conteudo": "Neste sentido [...] do sistema [...]",
        }, 
        {
          "linha": 18, 
          "conteudo": "No mundo atual, [...] estabelecimento do sistema [...]",
        },
    ],
  },
]
```
