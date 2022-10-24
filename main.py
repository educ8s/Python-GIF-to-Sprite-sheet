from PIL import Image

OUTPUT_SIZE = (64,64) # The output size of each frame (or tile or Sprite) of the animation
FILENAME = "clock.gif" # The file to convert
MONOCHROME = False # Do you want the output file to be b/w?

def open_gif():
	gif = Image.open(FILENAME)
	print(f"Image Format: {gif.format_description}")
	print(f"Image Size: {gif.size}")
	print(f"Frames: {gif.n_frames}")
	return gif

gif = open_gif()

if MONOCHROME:
	output = Image.new("1", (OUTPUT_SIZE[0] * gif.n_frames, OUTPUT_SIZE[1]), 0)
else:
	output = Image.new("RGB", (OUTPUT_SIZE[0] * gif.n_frames, OUTPUT_SIZE[1]))

output_filename = f"icon_{gif.n_frames}_frames.bmp"

for frame in range(0,gif.n_frames):
	gif.seek(frame)
	extracted_frame = gif.resize(OUTPUT_SIZE)
	position = (OUTPUT_SIZE[0]*frame, 0)
	output.paste(extracted_frame, position)

if not MONOCHROME:
	output = output.convert("P", colors = 8)
output.save(output_filename)