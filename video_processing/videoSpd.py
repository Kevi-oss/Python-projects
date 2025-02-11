import moviepy as mv

#This operator takes in a mp4 and creates a speed-up version of the same mp4
#PARAM
#Sample: string path to the mp4 file of desire, for instance "Dog_KO.mp4" or s'./videos/something.mp4'
#playback: floating point playback speed
def spdChange(sample, playbackSpd):
    try:
        original = mv.VideoFileClip(sample)
        clip = original.with_speed_scaled(playbackSpd, int(original.duration/playbackSpd))
        clip.write_videofile(f"Spdchanged_{sample}", audio_codec='aac')
    except:
        print("ERROR: Make sure your operator is in the format of spdChange(path, playbackSpeed), and the playbackSpeed is bigger than 0")


#NOTE: At floating point speeds such as 1.5, some frames may be lost because frames are of type int
#do NOT make the playbackSpd 0 unless you want an error