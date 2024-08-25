def print_dict_content(d, depth_level=0):
    indent = "    " * depth_level  # Create indentation based on depth_level

    for key, value in d.items():
        if value == "file":
            print(f"{indent}file: {key}")
        elif value == "empty directory":
            print(f"{indent}empty directory: {key}")
        else:
            if depth_level == 0:
                print(f"{indent}directory: {key}")
            else:
                print(f"{indent}{'sub_' * depth_level}directory: {key}")

            print_dict_content(value, depth_level + 1)  # Recursive call
