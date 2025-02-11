from os import remove
import cv2
import moviepy
import bgcolor

#Creates a new mp4 file that is a slightly different colored copy of the original file using opencv
#Changes to color/texture can be done in bgcolor file
#PARAM:
#sample: string path to the desired video
#NOTE: this is a horribly optimised way to do this, I'm trying to create a ver2 that is more optimized for large videos
def bgChange(sample):
    #get original video info
    cap = cv2.VideoCapture(sample)
    audio = moviepy.AudioFileClip(sample)
    o_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    o_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    n_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    o_FPS = int(cap.get(cv2.CAP_PROP_FPS))

    #Process video/make changes
    product = cv2.VideoWriter(f"copy_{sample}", cv2.VideoWriter_fourcc(*'mp4v'), o_FPS, (o_width, o_height))
    for frame in range(n_frames):
        ret, img = cap.read()
        if ret == False:
            break
        product.write(bgcolor.changeColor(img))

    #cleanup
    product.release()
    cv2.destroyAllWindows()
    
    #add audio
    new_video = moviepy.VideoFileClip(f"copy_{sample}")
    remove(f"copy_{sample}")
    new_video.audio= moviepy.CompositeAudioClip([audio])
    new_video.write_videofile(f"colorChanged_{sample}", audio_codec='aac')
