import moviepy
#PARAMETER
#sample: path to original mp4
#text: The text you want to add to video
#horiz: horizontal position, try 'left', 'center', or 'right', pixel positions like 50 will also work
#verti: vertical position, try 'top', 'center', or 'bottom', pixel positions also work
def addWaterMark(sample, text, horiz, verti):
    try:
        clip = moviepy.VideoFileClip(sample)
        # Generate a text clip based on text
        # customize textclip method to edit what the text looks like
        txt_clip = moviepy.TextClip(font = "Arial", text = text, font_size=100, color="black", duration = clip.duration)
        txt_clip = txt_clip.with_position((horiz, verti))
        # Overlay the text clip on the first video clip
        video = moviepy.CompositeVideoClip([clip, txt_clip])
        video.write_videofile(f"watermarked_{sample}", audio_codec='aac')
    except Exception as e:
        print(f"Likely syntax error: {e}")
