import os


def read_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.readlines()
    return content


def merge_files(dir, output_file):
    files = os.listdir(dir)    
    files_content = []

    for file_name in files:
        file_path = os.path.join(dir, file_name)
        content = read_file(file_path)
        files_content.append((file_name, len(content), content))

    files_content.sort(key=lambda x: x[1])
    
    with open(output_file, 'w', encoding='utf-8') as outfile:
        for file_name, num_lines, content in files_content:
            outfile.write(f"{file_name}\n{num_lines}\n")
            outfile.writelines(content)
            outfile.write("\n")

    print_result(output_file)


def print_result(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
        print(content)


merge_files('files', 'result.txt')
