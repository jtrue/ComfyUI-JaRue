class String2Int_jru:
    def __init__(self):
        pass
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "string_a": ("STRING", {"forceInput":True,"default":"","multiline": False}),
            }
        }




    RETURN_TYPES = ("INT", )
    FUNCTION = "concat"

    CATEGORY = "JaRue"

    def concat(self, string_a):
        c = int(string_a)
        return (c,)




# A dictionary that contains all nodes you want to export with their names
# NOTE: names should be globally unique
NODE_CLASS_MAPPINGS = {
    "String2Int_jru": String2Int_jru
}

# A dictionary that contains the friendly/humanly readable titles for the nodes
NODE_DISPLAY_NAME_MAPPINGS = {
    "String2Int_jru": "Convert String to Integer"
}