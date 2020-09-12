import moviepy.editor as mp 
import wave  
# Insert Local Video File Path  
clip = mp.VideoFileClip(r"vid5.mp4") 
  
# Insert Local Audio File Path 
clip.audio.write_audiofile(r"try1.wav")

