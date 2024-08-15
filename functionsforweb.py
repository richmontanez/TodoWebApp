FILEPATH = "todos.txt"


def get_todos(filepath=FILEPATH):
    with open(filepath) as file_local:
        todos_local = file_local.readlines()

    return todos_local


def write_todos(todos_arg, filepath=FILEPATH):
    with open(filepath, 'w') as file_write:
        file_write.writelines(todos_arg)


if __name__ == 'main':
    print("hello from functions")
