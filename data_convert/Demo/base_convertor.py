from data_convert.Module.example_convertor import ExampleConvertor


def demo():
    work_space = "./data/"
    source_root_folder_path = work_space + "mesh/"
    target_root_folder_path = work_space + "mesh_type/"
    source_data_type = ".obj"
    target_data_type = ".txt"
    output_freq = 1.0

    example_convertor = ExampleConvertor(
        source_root_folder_path, target_root_folder_path
    )
    example_convertor.convertAll(source_data_type, target_data_type, output_freq)
    return True
