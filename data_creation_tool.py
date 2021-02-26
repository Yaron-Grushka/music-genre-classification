import os
import librosa
import soundfile as sf
import librosa.display
import numpy as np
import matplotlib.pyplot as plt
SLICE_SIZE = 3.0
SAMPLE_SIZE = 30.0

def audio_to_spectrogram_slices(directory,dest,filename):
  i=0;
  for offset in range(0,SAMPLE_SIZE,SLICE_SIZE):
    y, sr = librosa.load(directory+'/'+filename,offset=offset,duration=SLICE_SIZE)
    S = librosa.feature.melspectrogram(y=y, sr=sr,n_mels=128)
    librosa.display.specshow(librosa.amplitude_to_db(S, ref=np.max))
    plt.savefig(f'{dest}/{filename[:-4]}{i}.png')
    i+=1

def convert_all_samples(source,dest):
  for subdir in ['blues','classical','countery','disco','hiphop','jazz','metal','pop','reggae','rock']:
  directory = f'{source}/{{subdir}'
  for filename in os.listdir(directory):
      if filename.endswith(".wav") or filename.endswith(".mp3"):
          print(os.path.join(directory, filename))
          audio_to_spectrogram_slices(directory,dest,filename)
