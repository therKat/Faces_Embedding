from keras_facenet import FaceNet
import os
import numpy as np
import cv2

faces_dir = "faces"
embed_dir = "faces_embedded"
IMG_SIZE = 160

facenet = FaceNet()

embeddeds = []
for sub in os.listdir(faces_dir):
    sub_dir = os.path.join(faces_dir, sub)
    imgs = []
    for file_name in os.listdir(sub_dir):
        file_path = os.path.join(sub_dir, file_name)
        img = cv2.imread(file_path)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        img = cv2.resize(img, (IMG_SIZE, IMG_SIZE))
        # print(img.shape)
        imgs.append(img)

    img_embed = facenet.embeddings(imgs)
    embed_dir = os.path.join(sub_dir, sub)
    embed_file = os.path.join(embed_dir, f"{sub}_embedding.npy")

    if not os.path.exists(embed_dir):
        os.makedirs(embed_dir)

    np.save(embed_file, embeddeds)
    # print(img_embed.shape)
    embeddeds.append(img_embed)

np.save("faces_embedding", embeddeds)

