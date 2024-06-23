"""
ラベルの数を指定数まで減らす
"""

import os
import random
from collections import defaultdict


def reduce_label_instances(label_dir, image_dir, label_id, max_count):
    # ラベルごとのファイルリストを収集
    label_files = defaultdict(list)

    for label_file in os.listdir(label_dir):
        label_path = os.path.join(label_dir, label_file)
        with open(label_path, "r") as file:
            lines = file.readlines()
            for line in lines:
                parts = line.split()
                if int(parts[0]) == label_id:
                    label_files[label_id].append(label_file)
                    break

    # 指定されたラベルのファイルリストを取得
    files = label_files[label_id]

    if len(files) <= max_count:
        print(
            f"Label {label_id} has {len(files)} instances, which is less than or equal to the maximum count of {max_count}. No files will be removed."
        )
        return

    # ランダムに選択して削除
    files_to_remove = random.sample(files, len(files) - max_count)

    for file in files_to_remove:
        label_path = os.path.join(label_dir, file)
        image_path = os.path.join(
            image_dir, file.replace(".txt", ".jpg")
        )  # Assuming images are .jpg, adjust if different

        print(f"Removing {label_path} and {image_path}")
        os.remove(label_path)
        if os.path.exists(image_path):
            os.remove(image_path)


# パスの設定
label_dir = "./YOLO/dataset/train/labels/"
image_dir = "./YOLO/dataset/train/images/"
label_id_to_reduce = 2  # 減らしたいラベルのID
max_count = 5000  # ラベルの最大インスタンス数

reduce_label_instances(label_dir, image_dir, label_id_to_reduce, max_count)
