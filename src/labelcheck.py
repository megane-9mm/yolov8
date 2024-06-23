"""
検出用以外のラベルが含まれるテキストと画像を削除
"""

import os


def delete_segmentation_labels_and_images(image_dir, label_dir):
    # ラベルディレクトリ内の全てのファイルをチェック
    for label_file in os.listdir(label_dir):
        label_path = os.path.join(label_dir, label_file)

        with open(label_path, "r") as file:
            lines = file.readlines()

        # セグメンテーション用のラベルが含まれているかチェック
        is_segmentation = False
        for line in lines:
            parts = line.split()
            if len(parts) != 5:  # 物体検出用のアノテーションは通常5つの要素
                is_segmentation = True
                break

        if is_segmentation:
            # 該当するラベルファイルと対応する画像ファイルを削除
            print(f"Deleting segmentation label and corresponding image: {label_file}")
            os.remove(label_path)

            # 対応する画像ファイルを削除（拡張子が .jpg であることを仮定）
            image_file = label_file.replace(".txt", ".jpg")
            image_path = os.path.join(image_dir, image_file)
            if os.path.exists(image_path):
                os.remove(image_path)
                print(f"Deleted image: {image_file}")
            else:
                print(f"Image file not found: {image_file}")


# ディレクトリのパスを設定
image_dir = "./add_dataset/dataset_add/valid/labels"
label_dir = "./add_dataset/dataset_add/valid/labels"

delete_segmentation_labels_and_images(image_dir, label_dir)
