class ConcatStringWithDelimiter_jru:

    def __init__(self):
        pass
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "string_a": ("STRING", {"forceInput":True,"default":"","multiline": False}),
                "string_b": ("STRING", {"forceInput":True,"default":"","multiline": False}),
                "string_c": ("STRING", {"forceInput":True,"default":"_","multiline": False}),
            }
        }




    RETURN_TYPES = ("STRING", )
    FUNCTION = "concat"

    CATEGORY = "JaRue"

    def concat(self, string_a, string_b, string_c):
        c = string_a + string_c + string_b
        return (c,)




# A dictionary that contains all nodes you want to export with their names
# NOTE: names should be globally unique
NODE_CLASS_MAPPINGS = {
    "ConcatStringWithDelimiter_jru": ConcatStringWithDelimiter_jru
}

# A dictionary that contains the friendly/humanly readable titles for the nodes
NODE_DISPLAY_NAME_MAPPINGS = {
    "ConcatStringWithDelimiter_jru": "Concat Strings w/ Delimiter"
}