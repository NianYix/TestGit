from moviepy.editor import *

# 1、视频裁剪 subclip为秒数
# video =CompositeVideoClip([VideoFileClip("mmm.flv").subclip(30,40)])
# video.write_videofile("output.mp4")

# 2、更改分辨率
# clip1 = VideoFileClip("output.mp4").resize((1080, 720))
# clip1.write_videofile("output2.mp4")

# 3、提取音频
# audio = VideoFileClip('mmm.flv').audio
# audio.write_audiofile('output3.mp3')

# 4、视频拼接
clip1 = VideoFileClip("1.mp4")
clip2 = VideoFileClip("2.mp4").subclip(30, 40)
clip3 = VideoFileClip("3.mp4")

final_clip = concatenate_videoclips([clip1, clip2, clip3])
final_clip.write_videofile("output4.mp4")
