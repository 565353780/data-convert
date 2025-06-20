from data_convert.Module.example_convertor import ExampleConvertor
from data_convert.Module.pipeline_convertor import PipelineConvertor


def demo():
    data_space = "./data/"
    output_space = "./output/data/"

    convertor_list = [
        ExampleConvertor(data_space + "mesh/", output_space + "mesh_type/"),
        ExampleConvertor(output_space + "mesh_type/", output_space + "mesh_type_2/"),
        ExampleConvertor(output_space + "mesh_type_2/", output_space + "mesh_type_3/"),
    ]

    data_type_list = [
        ".obj",
        ".txt",
        ".txt",
        ".txt",
    ]

    pipeline_convertor = PipelineConvertor(convertor_list)

    rel_base_path = "0"
    pipeline_convertor.convertOneShape(rel_base_path, data_type_list)

    pipeline_convertor.convertAll(data_type_list)
    return True
