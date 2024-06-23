"""
RoboflowからDLしたデータセットに対して、
validやtestデータが無い場合に、trainデータから数枚ランダムで移動させるスクリプト
"""

import os
import random
import shutil

# ディレクトリのパスを設定
train_images_dir = "./add_dataset/napa.v4i.yolov8/train/images"
train_labels_dir = "./add_dataset/napa.v4i.yolov8/train/labels"
test_images_dir = "./add_dataset/napa.v4i.yolov8/test/images"
test_labels_dir = "./add_dataset/napa.v4i.yolov8/test/labels"

# 移動するファイルの数
num_files_to_move = 15

# 画像ファイルリストの取得
image_files = [
    f for f in os.listdir(train_images_dir) if f.endswith(".jpg")
]  # 画像の拡張子が異なる場合は修正
random.shuffle(image_files)

# ランダムにnum_files_to_move枚選択
files_to_move = image_files[:num_files_to_move]

# 必要なディレクトリを作成
os.makedirs(test_images_dir, exist_ok=True)
os.makedirs(test_labels_dir, exist_ok=True)

# ファイルの移動
for image_file in files_to_move:
    label_file = image_file.replace(
        ".jpg", ".txt"
    )  # ラベルファイルの拡張子が異なる場合は修正

    # 画像ファイルの移動
    shutil.move(
        os.path.join(train_images_dir, image_file),
        os.path.join(test_images_dir, image_file),
    )

    # ラベルファイルの移動
    shutil.move(
        os.path.join(train_labels_dir, label_file),
        os.path.join(test_labels_dir, label_file),
    )

print(
    f"Moved {num_files_to_move} images and their corresponding labels from train to test."
)
