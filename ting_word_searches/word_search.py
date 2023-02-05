from ting_file_management.queue import Queue
from ting_file_management.file_process import process

def exists_word(word, instance: Queue):
    word_occurrencies = []

    for i in range(len(instance)):
        file = instance.search(i)
        file_lines =  file["linhas_do_arquivo"]
        occurencies = []
        add_file = False

        for j in range(len(file_lines)):
            if word.lower() in file_lines[j].lower():
                occurencies.append({"linha": j + 1})
                add_file = True

        if add_file:
            word_occurrencies.append({
                "palavra": word,
                "arquivo": file["nome_do_arquivo"],
                "ocorrencias": occurencies
            })

    return word_occurrencies


def search_by_word(word, instance):
    """Aqui irá sua implementação"""
