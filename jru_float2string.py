class Float2String_jru:

    def __init__(self):
        pass
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "float_a": ("FLOAT", {"forceInput":True,"default":1,"min": 0}),
            }
        }




    RETURN_TYPES = ("STRING", )
    FUNCTION = "fFloat2String"

    CATEGORY = "JaRue"

    def fFloat2String(self, float_a):
        c = str(float_a)
        return (c,)




# A dictionary that contains all nodes you want to export with their names
# NOTE: names should be globally unique
NODE_CLASS_MAPPINGS = {
    "Float2String_jru": Float2String_jru
}

# A dictionary that contains the friendly/humanly readable titles for the nodes
NODE_DISPLAY_NAME_MAPPINGS = {
    "Float2String_jru": "Convert Float to String"
}