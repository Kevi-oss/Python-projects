import moviepy as mv

original = mv.VideoFileClip("Dog_KO.mp4")
speed = 2.5
clip = original.with_speed_scaled(speed, int(original.duration/speed))
clip.write_videofile("test.mp4", audio_codec='aac')
