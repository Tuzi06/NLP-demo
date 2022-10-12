import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.io.wavfile import read
from scipy.fft import fft,fftfreq
import cv2

# # extract audio from video
# from moviepy.editor import *
# clip = VideoFileClip("./data/video.mp4")
# audio = clip.audio.write_audiofile('./data/audio.wav')


video = cv2.VideoCapture("data/video.mp4")
fps = video.get(cv2.CAP_PROP_FPS)     
frame_count = int(video.get(cv2.CAP_PROP_FRAME_COUNT))
length = int(frame_count//fps) # seconds
sampleRate,audio = read('data/audio.wav')
print(length,sampleRate)
audio =  np.array([s[0] for s in audio])
norm = np.int16((audio / audio.max()) * 32767)

x = fft(audio[:length*sampleRate])
# np.savetxt('data.csv',x,delimiter=',')
y = fftfreq(length*sampleRate,1/sampleRate)
print('audio',len(audio),'x',len(x),'\n','y',len(y))
plt.rcParams["figure.autolayout"] = True
# plt.plot(x,np.abs(y),'r')
plt.plot(np.abs(y),np.abs(x))
plt.show()
