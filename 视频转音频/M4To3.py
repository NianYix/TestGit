from ffmpy import FFmpeg
import os
import uuid
import sys
sys.path.append('..')
# sys.path.append(r'F:\Work\JerryStudy\Python\ZiLiao\Code') 
import entry


def extract(video_path: str, tmp_dir: str, ext: str):
    file_name = '.'.join(os.path.basename(video_path).split('.')[0:-1])
    print('文件名:{}，提取音频'.format(file_name))
    return run_ffmpeg(video_path, os.path.join(tmp_dir, r'{}.{}'.format(uuid.uuid4(), ext)), ext)

def run_ffmpeg(video_path: str, audio_path: str, format: str):
    ff = FFmpeg(executable=r'C:\KMPlayer\ffmpeg.exe',inputs={video_path: None},
                outputs={audio_path: r'-f {} -vn'.format(format)})
    ff.run()
    return audio_path

_fileName=''
_filePath=''
def get_fileName(fileName):
    _fileName=fileName
    print(f'_fileName:{_fileName}-')
    entry.get_saveFilePath(get_file)
    
def get_file(filePath):
    _filePath=filePath
    print(f'_fileName:{_fileName}-_filePath:{_filePath}')
    print(extract(_fileName, _filePath,'wav'))

if __name__ == '__main__':
#     entry.get_file('mp4',get_fileName)
    _fileName=r'F:/Work/JerryStudy/GitPos/TestGit/视频转音频/mmm.flv'
    _filePath=r'F:/Work/JerryStudy/GitPos/TestGit/视频转音频'
    print(extract(_fileName, _filePath,'wav'))
    