import cv2
import os
from skimage.metrics import structural_similarity as ssim
from datetime import datetime

def load_images_from_folder(folder):
    images = []
    filenames = []
    for filename in os.listdir(folder):
        img = cv2.imread(os.path.join(folder, filename))
        if img is not None:
            images.append(img)
            filenames.append(filename)
    return images, filenames

def compare_images(imageA, imageB):
    height, width = imageA.shape[:2]
    imageB = cv2.resize(imageB, (width, height))

    grayA = cv2.cvtColor(imageA, cv2.COLOR_BGR2GRAY)
    grayB = cv2.cvtColor(imageB, cv2.COLOR_BGR2GRAY)
    score, _ = ssim(grayA, grayB, full=True)
    return score

def delete_similar_images(folder, threshold=0.98):
    images, filenames = load_images_from_folder(folder)
    to_delete = set()
    try:
        for i in range(len(images)):
            if filenames[i] in to_delete:
                continue
            for j in range(i + 1, len(images)):
                if filenames[j] in to_delete:
                    continue
                score = compare_images(images[i], images[j])
                if score > threshold:
                    to_delete.add(filenames[j])
        for filename in to_delete:
            os.remove(os.path.join(folder, filename))
            print(f"Deleted: {filename}")
    except Exception as e:
        print(f"{folder}: {e}")
        with open("export_log.txt", 'a') as file:
            now = datetime.now()
            current_time = now.strftime("%Y-%m-%d %H:%M:%S")
            line = f"{current_time}\t{folder}: {e}"
            file.write(f'{line}\n')

# folder_path = 'path_to_your_folder'
# delete_similar_images(folder_path)

target_dir = 'faces'

for idx, ms in enumerate(os.listdir(target_dir)):
    ms_dir = os.path.join(target_dir, ms)
    if len(os.listdir(ms_dir)) > 12:
        delete_similar_images(ms_dir, threshold=0.5)