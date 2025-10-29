def copy_file(command: str) -> None:
    parts = command.split()
    if len(parts) != 3 or parts[0] != "cp":
        return

    input_name, output_name = parts[1], parts[2]

    if input_name == output_name:
        return

    try:
        with (open(input_name, "r") as file_in,
              open(output_name, "w") as file_out):
            for line in file_in:
                file_out.write(line)
    except Exception as e:
        print("Exception:", e)
