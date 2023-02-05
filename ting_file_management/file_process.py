from ting_file_management.queue import Queue
from ting_file_management.file_management import txt_importer

def process(path_file, instance):
    if len(instance) > 0:
        for i in range(len(instance)):
            if instance.search(i)["nome_do_arquivo"] == path_file:
                return

    file_content = txt_importer(path_file)

    file_info = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(file_content),
        "linhas_do_arquivo": file_content,
    }

    print(file_info)
    instance.enqueue(file_info)


def remove(instance):
    if len(instance) < 1:
        print("Não há elementos")
        return

    file_removed = instance.dequeue()
    path_file = file_removed["nome_do_arquivo"]
    print(f"Arquivo {path_file} removido com sucesso")


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
