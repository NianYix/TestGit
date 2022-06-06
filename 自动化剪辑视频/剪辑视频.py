from moviepy.editor import *

# 1、视频裁剪 subclip为秒数
video =CompositeVideoClip([VideoFileClip("dance.mp4").subclip(30,33)])
video.write_videofile("OutDance.mp4")

# 2、更改分辨率
# clip1 = VideoFileClip("output.mp4").resize((1080, 720))
# clip1.write_videofile("output2.mp4")

# 3、提取音频
# audio = VideoFileClip('mmm.flv').audio
# audio.write_audiofile('output3.mp3')

# 4、视频拼接
# clip1 = VideoFileClip("pinjie1.mp4")
# clip2 = VideoFileClip("pinjie2.mp4").set_start(9).crossfadein(1)
# clip3 = VideoFileClip("pinjie3.mp4").set_start(18).crossfadein(1)
# 
# final_clip = CompositeVideoClip([clip1, clip2, clip3])
# final_clip.write_videofile("pinjieTotal.mp4")


