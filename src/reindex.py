"""
RoboflowからDLしたデータセットに対して必要なラベルのみを残した場合、
ラベル順序を再定義するスクリプト
"""

import os
import random
import shutil

# ディレクトリのパスを設定
vegetable_train_path = "./add_dataset/Vegetable.v3i.yolov8/train/"
vegetable_test_path = "./add_dataset/Vegetable.v3i.yolov8/test/"
vegetable_valid_path = "./add_dataset/Vegetable.v3i.yolov8/valid/"


def reindex_labels(label_dir, label_map):
    for label_file in os.listdir(label_dir):
        label_path = os.path.join(label_dir, label_file)
        with open(label_path, "r") as file:
            lines = file.readlines()

        new_lines = []
        for line in lines:
            parts = line.split()
            class_id = int(parts[0])
            if class_id in label_map:
                new_class_id = label_map[class_id]
                parts[0] = str(new_class_id)
                new_lines.append(" ".join(parts) + "\n")
                print("new_lines", new_lines)

        with open(label_path, "w") as file:
            file.writelines(new_lines)


# ラベルマップの定義
vegetable_label_map = {
    0: 1,
    1: 14,
    2: 8,
}  # 例: 0: キャベツ, 1: トマト

# 各データセットのラベルを再インデックス
reindex_labels(os.path.join(vegetable_train_path, "labels"), vegetable_label_map)
reindex_labels(os.path.join(vegetable_test_path, "labels"), vegetable_label_map)
#reindex_labels(os.path.join(vegetable_valid_path, "labels"), vegetable_label_map)
