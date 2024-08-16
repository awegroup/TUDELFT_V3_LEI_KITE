import TUDELFT_V3_LEI_KITE
from TUDELFT_V3_LEI_KITE.extract_package_contents import extract_package_contents
from TUDELFT_V3_LEI_KITE.print_dict_content import print_dict_content

package_content = extract_package_contents(TUDELFT_V3_LEI_KITE)
print_dict_content(package_content)

print("\n")
print(f"--------------------------------")
print(f"Surfplan-export package content")
print(f"--------------------------------")
print_dict_content(package_content["surfplan_export"])
