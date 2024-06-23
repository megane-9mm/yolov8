"""
imagesとlabelsで片方にしか存在しないデータを削除する
"""

import os


def get_file_stems(directory, extension):
    """Returns a set of file stems (filename without extension) in the given directory."""
    return set(
        os.path.splitext(f)[0] for f in os.listdir(directory) if f.endswith(extension)
    )


def delete_unmatched_files(images_dir, labels_dir, image_ext=".jpg", label_ext=".txt"):
    """Deletes files that don't have a corresponding match in the other directory."""
    image_stems = get_file_stems(images_dir, image_ext)
    label_stems = get_file_stems(labels_dir, label_ext)

    # Files to delete
    images_to_delete = image_stems - label_stems
    labels_to_delete = label_stems - image_stems

    # Delete unmatched images
    for stem in images_to_delete:
        file_path = os.path.join(images_dir, f"{stem}{image_ext}")
        if os.path.exists(file_path):
            os.remove(file_path)
            print(f"Deleted unmatched image: {file_path}")

    # Delete unmatched labels
    for stem in labels_to_delete:
        file_path = os.path.join(labels_dir, f"{stem}{label_ext}")
        if os.path.exists(file_path):
            os.remove(file_path)
            print(f"Deleted unmatched label: {file_path}")


# ディレクトリのパスを設定
images_dir = "./YOLO/dataset/valid/images/"
labels_dir = "./YOLO/dataset/valid/labels/"

delete_unmatched_files(images_dir, labels_dir)
