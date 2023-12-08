class Int2FloatMultiply_jru:
    def __init__(self):
        pass
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "int_a": ("INT", {"forceInput":True,"default":0,"min": 0}),
                "float_b": ("FLOAT", {"forceInput":True,"default":1.0}),
            }
        }




    RETURN_TYPES = ("FLOAT", )
    FUNCTION = "int2floatmlt"

    CATEGORY = "JaRue"

    def int2floatmlt(self, int_a, float_b):
        c = int_a * float_b
        return (c,)




# A dictionary that contains all nodes you want to export with their names
# NOTE: names should be globally unique
NODE_CLASS_MAPPINGS = {
    "Int2FloatMultiply_jru": Int2FloatMultiply_jru
}

# A dictionary that contains the friendly/humanly readable titles for the nodes
NODE_DISPLAY_NAME_MAPPINGS = {
    "Int2FloatMultiply_jru": "Convert Integer to Float w/ multiply"
}