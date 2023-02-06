from ting_file_management.queue import Queue
from ting_file_management.file_process import process


def get_line_info(word, file_lines, occurrences, show_content):
    add_file = False
    for j in range(len(file_lines)):
        if word.lower() in file_lines[j].lower():
            line_info = {"linha": j + 1}

            if show_content:
                line_info["conteudo"] = file_lines[j]

            occurrences.append(line_info)
            add_file = True
    return add_file


def exists_word(word, instance: Queue, show_content=False):
    word_occurrences = []

    for i in range(len(instance)):
        file = instance.search(i)
        file_lines = file["linhas_do_arquivo"]
        occurrences = []

        add_file = get_line_info(word, file_lines, occurrences, show_content)

        if add_file:
            word_occurrences.append({
                "palavra": word,
                "arquivo": file["nome_do_arquivo"],
                "ocorrencias": occurrences
            })

    return word_occurrences


def search_by_word(word, instance):
    word_occurrences = exists_word(word, instance, show_content=True)
    return word_occurrences

if __name__ == "__main__":
    word = "sistema"
    project = Queue()
    process("statics/novo_paradigma_globalizado-min.txt", project)

    word_occurrences = exists_word(word, project)
    word_occurrences_with_content = search_by_word(word, project)

    print(word_occurrences)

    print("-------------------------------------------")

    print(word_occurrences_with_content)
