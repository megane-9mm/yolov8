"""
1以上のバウンディングボックス値がある場合は削除
"""

import os


def check_and_correct_labels(label_dir):
    for label_file in os.listdir(label_dir):
        label_path = os.path.join(label_dir, label_file)
        if label_path.endswith(".txt"):
            with open(label_path, "r") as file:
                lines = file.readlines()

            valid_lines = []
            for line in lines:
                parts = line.split()
                if len(parts) == 5:
                    class_id = parts[0]
                    x_center = float(parts[1])
                    y_center = float(parts[2])
                    width = float(parts[3])
                    height = float(parts[4])

                    # 座標が範囲内にあるか確認
                    if (
                        0 <= x_center <= 1
                        and 0 <= y_center <= 1
                        and 0 <= width <= 1
                        and 0 <= height <= 1
                    ):
                        valid_lines.append(line)
                    else:
                        print(
                            f"Out of bounds coordinates in {label_file}: {line.strip()}"
                        )

            # 有効な行がある場合のみファイルを上書き
            if valid_lines:
                with open(label_path, "w") as file:
                    file.writelines(valid_lines)
            else:
                print(f"Ignoring file with all out of bounds coordinates: {label_file}")
                os.remove(label_path)


# ラベルディレクトリのパスを設定
label_dir = "./add_dataset/dataset_add/train/labels"
check_and_correct_labels(label_dir)

label_dir = "./add_dataset/dataset_add/test/labels"
check_and_correct_labels(label_dir)

label_dir = "./add_dataset/dataset_add/valid/labels"
check_and_correct_labels(label_dir)
