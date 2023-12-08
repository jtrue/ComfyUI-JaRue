import os
#import shutil
import json
from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api.formatters import JSONFormatter
#https://pypi.org/project/youtube-transcript-api/

class YouTube2Prompt_jru:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "video_id": ("STRING", {"default":"VjMoRb5f-EQ","multiline": False}),
                "fps": ("INT", {"default":10,"min":1,"max": 1000}),
                "begin": ("INT", {"default":0,"min":0,"max": 10000000}),
                "cache": (["enable", "disable"], {"default": "enable"}),
#                "cache_reset":("BOOLEAN", {"default": False}),# "forceInput": True}),},
            }
        }
    RETURN_TYPES = ("STRING", )
    FUNCTION = "fetchIt2"
    CATEGORY = "JaRue"
    def fetchIt2(self, video_id, fps, begin, cache):
        my_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "transcripts")
        if not os.path.exists(my_path):
            os.makedirs(my_path)
        wr = os.path.join(my_path, video_id+".json")
        if os.path.exists(wr) and cache == False:
            print('We have deleted the cache!')
            os.remove(wr)
#            shutil.rmtree(wr)
        if os.path.exists(wr) and cache == "enable":
            print('We have cache!')
        else:
            print('We must YouTube it!')
            transcript = YouTubeTranscriptApi.get_transcript(video_id)
            formatter = JSONFormatter()
            json_formatted = formatter.format_transcript(transcript)
            with open(wr, 'w', encoding='utf-8') as json_file:
                json_file.write(json_formatted)
        f = open(wr)
        data = json.load(f)
        print("data length="+str(len(data)))
        outTxt = ""
        cnt = 0
        for d in data:
            fr = d['start']*fps
            if (begin > -1):
                fr = fr-begin
                if (fr < 0):
                    continue
#            print(str(fr)+"..."+str(d['start'])+"="+str(d['text']))
            cnt += 1
            comma = ","
            if cnt == len(data):
                comma = ""
            outTxt += "\""+str(int(fr))+"\": \""+str(d['text'])+"\""+comma+"\n"
        f.close()
        return {"ui": {"text":  outTxt}, "result": ( outTxt,)}

NODE_CLASS_MAPPINGS = {
    "YouTube2Prompt_jru": YouTube2Prompt_jru
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "YouTube2Prompt_jru": "YouTube to Prompt"
}
