# ComfyUI-JaRue
Takes a YouTube Video ID and pulls a transcript (if available) from the YouTube server and delivers it in a format you can link to AnimatedDiff or any other ComfyUI batch animation. 
You will need the YouTube Transcript API Library installed. See link.  
https://pypi.org/project/youtube-transcript-api/

![YouTube2Transcript](https://github.com/jtrue/ComfyUI-JaRue/assets/5502214/0085d1bb-7f84-4155-b1b2-85f9f3fe51ee)

Installation
After following the install instructions for the plugin https://pypi.org/project/youtube-transcript-api/ you may discover an error in ComfyUI telling you the library is not found. To fix this issue you will need to copy the api library you installed into your ComfyUI custom_nodes directory. 

There is a Text2Image tool included with this library so you can superimpose the captions on top of the video but i am still working on the code to tie it all together. Right now, you can generate an image with the caption and manually connect that into a batch video. I hope to add this capability to make it easier as this tool grows.  

![t2icui](https://github.com/jtrue/ComfyUI-JaRue/assets/5502214/4587e0d7-0773-4537-ac20-8ca31ad09170)
