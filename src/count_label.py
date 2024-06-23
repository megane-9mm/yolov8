"""
ラベルの数をカウント
学習データ数をそろえる際などに使用
"""

import os
from collections import defaultdict


def count_labels(label_dir):
    label_counts = defaultdict(int)

    # ラベルディレクトリ内のすべてのファイルをスキャン
    for label_file in os.listdir(label_dir):
        label_path = os.path.join(label_dir, label_file)

        # ファイルを開いてラベルを読み取る
        with open(label_path, "r") as file:
            lines = file.readlines()
            for line in lines:
                parts = line.split()
                label = int(parts[0])  # 最初の要素がクラスラベル
                label_counts[label] += 1

    return label_counts


# トレーニングラベルのディレクトリ
label_dir = "./YOLO/dataset/train/labels/"

# ラベルをカウント
label_counts = count_labels(label_dir)

# 結果を表示
for label, count in label_counts.items():
    print(f"Label {label}: {count} instances")
