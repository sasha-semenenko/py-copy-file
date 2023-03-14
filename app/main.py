def copy_file(command: str) -> None:
    string, first_command, second_command = command.split(",")
    if string == "cp" and first_command != second_command:
        with open("first_command", "r") as first_file, \
                open("second_command", "w") as second_file:
            second_file.write(first_file.read())
