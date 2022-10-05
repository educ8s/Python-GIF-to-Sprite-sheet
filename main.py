from PIL import Image

def open_gif():
	gif = Image.open("./icon.gif")
	print(f"Image Format: {gif.format_description}")
	print(f"Image Size: {gif.size}")
	print(f"Frames: {gif.n_frames}")
	return gif

output_size = (64,64)

gif = open_gif()

output = Image.new("1", (output_size[0] * gif.n_frames, output_size[1]), 0)

for frame in range(0,gif.n_frames):
	gif.seek(frame)
	extracted_frame = gif.resize((output_size[0], output_size[1]))
	position = (output_size[0]*frame, 0)
	output.paste(extracted_frame, position)
	output_filename = f"icon_{gif.n_frames}_frames.bmp"
	output.save(output_filename)