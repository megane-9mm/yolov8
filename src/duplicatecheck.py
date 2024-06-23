"""
重複するラベルがある場合は削除
"""

import os


def remove_duplicate_labels(label_dir):
    for label_file in os.listdir(label_dir):
        label_path = os.path.join(label_dir, label_file)
        if label_path.endswith(".txt"):
            with open(label_path, "r") as file:
                lines = file.readlines()

            unique_lines = list(set(lines))  # 重複行を削除

            if len(unique_lines) != len(lines):
                print(f"Removing duplicates in {label_file}")

            with open(label_path, "w") as file:
                file.writelines(unique_lines)


# ラベルディレクトリのパスを設定
label_dir = "./add_dataset/dataset_add/valid/labels"

remove_duplicate_labels(label_dir)
