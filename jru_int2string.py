class Int2String_jru:
    def __init__(self):
        pass
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "int_a": ("INT", {"forceInput":True,"default":0,"min": 0}),
            }
        }




    RETURN_TYPES = ("STRING", )
    FUNCTION = "concat"

    CATEGORY = "JaRue"

    def concat(self, int_a):
        c = str(int_a)
        return (c,)




# A dictionary that contains all nodes you want to export with their names
# NOTE: names should be globally unique
NODE_CLASS_MAPPINGS = {
    "Int2String_jru": Int2String_jru
}

# A dictionary that contains the friendly/humanly readable titles for the nodes
NODE_DISPLAY_NAME_MAPPINGS = {
    "Int2String_jru": "Convert Integer to String"
}