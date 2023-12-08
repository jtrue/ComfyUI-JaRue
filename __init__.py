import importlib
import os

node_list = [ #Add list of .py files containing nodes here
    "jru_int2string",
    "jru_concatstringwithdelimiter",
    "jru_int2floatmultiply",
    "jru_imagesizer",
	"jru_float2string",
    "jru_concatstring",
    "jru_float2int",
    "jru_string2int",
    "jru_int2string"

]

NODE_CLASS_MAPPINGS = {}
NODE_DISPLAY_NAME_MAPPINGS = {}

for module_name in node_list:
    imported_module = importlib.import_module(".{}".format(module_name), __name__)

    NODE_CLASS_MAPPINGS = {**NODE_CLASS_MAPPINGS, **imported_module.NODE_CLASS_MAPPINGS}
    NODE_DISPLAY_NAME_MAPPINGS = {**NODE_DISPLAY_NAME_MAPPINGS, **imported_module.NODE_DISPLAY_NAME_MAPPINGS}

__all__ = ['NODE_CLASS_MAPPINGS', 'NODE_DISPLAY_NAME_MAPPINGS']
