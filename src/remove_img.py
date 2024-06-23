"""
RoboflowからDLしたデータセットに対して、
必要なラベルのデータセットのみを残す
"""

import os
import random
import shutil


import os

# ディレクトリのパスを設定
images_dir = "./add_dataset/green.v1i.yolov8/train/images/"
labels_dir = "./add_dataset/green.v1i.yolov8/train/labels/"

# 残すラベルを指定（例: 0 と 2 のラベルを残す）
# required_labels = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
# required_labels = {0, 1, 3, 5, 7, 8, 10, 11}
required_labels = {3}

# ファイルの処理
for label_file in os.listdir(labels_dir):
    label_path = os.path.join(labels_dir, label_file)

    with open(label_path, "r") as file:
        lines = file.readlines()

    # 残すべきラベルのみを含む行を保持
    new_lines = [line for line in lines if int(line.split()[0]) in required_labels]

    if new_lines:
        # ラベルファイルを更新
        with open(label_path, "w") as file:
            file.writelines(new_lines)
    else:
        # ラベルファイルを削除
        os.remove(label_path)

        # 対応する画像ファイルを削除
        image_file = label_file.replace(
            ".txt", ".jpg"
        )  # 画像の拡張子が異なる場合は修正
        image_path = os.path.join(images_dir, image_file)

        if os.path.exists(image_path):
            os.remove(image_path)

print("Specified labels retained, others removed.")
