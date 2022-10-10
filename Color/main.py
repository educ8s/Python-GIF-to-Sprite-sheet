from PIL import Image

FILENAME = "clock.gif"
output_size = (50,50)

def open_gif():
	gif = Image.open(FILENAME)
	print(f"Image Format: {gif.format_description}")
	print(f"Image Size: {gif.size}")
	print(f"Frames: {gif.n_frames}")
	return gif

gif = open_gif()

output = Image.new("RGB", (output_size[0] * gif.n_frames, output_size[1]))
output_filename = f"icon_{gif.n_frames}_frames.bmp"

for frame in range(0,gif.n_frames):
	gif.seek(frame)
	extracted_frame = gif.resize(output_size)
	position = (output_size[0]*frame, 0)
	output.paste(extracted_frame, position)

output = output.convert("P", colors = 8)
output.save(output_filename)