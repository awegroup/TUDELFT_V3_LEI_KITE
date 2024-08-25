import importlib
import pprintpp
from importlib.resources import files
from typing import List, Dict, Union


def extract_package_contents(package, top_level=True) -> Dict[str, Union[str, Dict]]:
    package_path = files(package)
    package_name = package.__name__.split(".")[0]
    contents = {}

    for item in package_path.iterdir():
        if item.is_file():
            contents[item.name] = "file"
        elif item.is_dir():
            try:
                subpackage = importlib.import_module(f"{package.__name__}.{item.name}")
                subcontents = extract_package_contents(subpackage, top_level=False)
                contents[item.name] = subcontents
            except ImportError:
                # If it's not a valid Python package, just add it as an empty directory
                contents[item.name] = "empty directory"

    if top_level:
        print(f"{package_name} package content extracted from path:")
        print(f"    {package_path}")
        print(f"--------------------------------")
    return contents


if __name__ == "__main__":
    import TUDELFT_V3_LEI_KITE
    from TUDELFT_V3_LEI_KITE.print_dict_content import print_dict_content

    package_content = extract_package_contents(TUDELFT_V3_LEI_KITE)
    print_dict_content(package_content)
