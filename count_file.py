import os

target_dir = 'faces'

image_count = []

for ms in os.listdir(target_dir):
    ms_dir = os.path.join(target_dir, ms)
    len_dir = len(os.listdir(ms_dir))
    image_count.append(len_dir)
    if len_dir > 10:
        print(f"{ms_dir} - {len_dir}")

print(set(image_count))