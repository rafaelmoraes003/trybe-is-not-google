import sys


def txt_importer(path_file):
    file_extension = path_file.split(".")[-1]

    if file_extension != "txt":
        print("Formato inválido", file=sys.stderr)
        return

    try:
        with open(path_file, mode="r") as file:
            content = file.read()
        return content.split("\n")
    except FileNotFoundError:
        print(f"Arquivo {path_file} não encontrado", file=sys.stderr)
