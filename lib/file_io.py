def write_file(file_name, file_content):
    full_name = f"{file_name}.txt"
    with open(full_name, mode="w", encoding="utf-8") as text_file:
        text_file.write(file_content)


def append_file(file_name, append_content):
    full_name = f"{file_name}.txt"
    with open(full_name, mode="a", encoding="utf-8") as text_file:
        text_file.write(append_content)



def read_file(file_name):
    full_name = f"{file_name}.txt"
    content = ""
    with open(full_name, mode="r", encoding="utf-8") as text_file:
        for line in text_file:
            content += line
    return content
