from ting_file_management.queue import Queue


def exists_word(word, instance: Queue, show_content=False):
    word_occurrencies = []

    for i in range(len(instance)):
        file = instance.search(i)
        file_lines = file["linhas_do_arquivo"]
        occurencies = []
        add_file = False

        for j in range(len(file_lines)):
            if word.lower() in file_lines[j].lower():
                line_info = {"linha": j + 1}

                if show_content:
                    line_info["conteudo"] = file_lines[j]

                occurencies.append(line_info)
                add_file = True

        if add_file:
            word_occurrencies.append({
                "palavra": word,
                "arquivo": file["nome_do_arquivo"],
                "ocorrencias": occurencies
            })

    return word_occurrencies


def search_by_word(word, instance):
    word_occurrencies = exists_word(word, instance, show_content=True)
    return word_occurrencies
