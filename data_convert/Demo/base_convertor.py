from data_convert.Module.base_convertor import BaseConvertor


class ExampleConvertor(BaseConvertor):
    def __init__(
        self,
        source_root_folder_path: str,
        target_root_folder_path: str,
    ) -> None:
        super().__init__(source_root_folder_path, target_root_folder_path)
        return

    def convertData(self, source_path: str, target_path: str) -> bool:
        """
        you can only focus on the kernel convert script here
        just process the source file at source_path
        and then save the target file at target_path
        """
        source_type = source_path.split(".")[-1]
        if source_type in ["obj", "ply"]:
            with open(target_path, "w") as f:
                f.write("source type is :" + source_type + "\n")
        return True


def demo():
    source_root_folder_path = "/Users/chli/chLi/Dataset/vae-eval/mesh/"
    target_root_folder_path = "/Users/chli/chLi/Dataset/vae-eval/mesh_type/"
    source_data_type = ".obj"
    target_data_type = ".txt"
    output_freq = 1.0

    example_convertor = ExampleConvertor(
        source_root_folder_path, target_root_folder_path
    )
    example_convertor.convertAll(source_data_type, target_data_type, output_freq)
    return True
