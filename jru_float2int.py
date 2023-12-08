class Float2Int_jru:

    def __init__(self):
        pass
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "float_a": ("FLOAT", {"forceInput":True,"default":1,"min": 0}),
            }
        }




    RETURN_TYPES = ("INT", )
    FUNCTION = "fFloat2Int"

    CATEGORY = "JaRue"

    def fFloat2Int(self, float_a):
        c = int(float_a)
        return (c,)




# A dictionary that contains all nodes you want to export with their names
# NOTE: names should be globally unique
NODE_CLASS_MAPPINGS = {
    "Float2Int_jru": Float2Int_jru
}

# A dictionary that contains the friendly/humanly readable titles for the nodes
NODE_DISPLAY_NAME_MAPPINGS = {
    "Float2Int_jru": "Convert Float to Integer"
}