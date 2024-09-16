import os
from tensorflow.keras.preprocessing.image import ImageDataGenerator, img_to_array, load_img

# Create an instance of ImageDataGenerator with desired augmentations
datagen = ImageDataGenerator(
    rotation_range=15,
    shear_range=0.2,
    zoom_range=0.1,
    horizontal_flip=True,
    vertical_flip=True,
    fill_mode='constant'
)

images_dir = 'faces'
dest_len = 12

for fol in os.listdir(images_dir):
    fol_dir = os.path.join(images_dir, fol)
    if len(os.listdir(fol_dir)) < dest_len:
        print(fol_dir)
        while (len(os.listdir(fol_dir)) < dest_len):
            for file_name in os.listdir(fol_dir):
                file_path = os.path.join(fol_dir, file_name)
                img = load_img(file_path)
                x = img_to_array(img)
                x = x.reshape((1,) + x.shape)  # Reshape to (1, height, width, channels)

                # Directory to save augmented images
                save_dir = fol_dir
                os.makedirs(save_dir, exist_ok=True)

                # Generate and save 20 augmented images
                i = 0
                for batch in datagen.flow(x, batch_size=1, save_to_dir=save_dir, save_prefix='z_aug', save_format='jpeg'):
                    i += 1
                    if i >= 1 or len(os.listdir(fol_dir)) > (dest_len-1):
                        break
                if len(os.listdir(fol_dir)) > (dest_len-1):
                        break