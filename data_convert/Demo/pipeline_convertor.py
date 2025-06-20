from data_convert.Module.example_convertor import ExampleConvertor
from data_convert.Module.pipeline_convertor import PipelineConvertor


def demo():
    work_space = "./data/"

    convertor_list = [
        ExampleConvertor(work_space + "mesh/", work_space + "mesh_type/"),
        ExampleConvertor(work_space + "mesh_type/", work_space + "mesh_type_2/"),
        ExampleConvertor(work_space + "mesh_type_2/", work_space + "mesh_type_3/"),
    ]

    data_type_list = [
        ".obj",
        ".txt",
        ".txt",
        ".txt",
    ]

    pipeline_convertor = PipelineConvertor(convertor_list)

    pipeline_convertor.convertAll(data_type_list)
    return True
