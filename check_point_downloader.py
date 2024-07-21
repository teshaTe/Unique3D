import os
import shutil
from huggingface_hub import snapshot_download


def delete_all_subfolders(directory, keep_directory):
    # Check if the directory exists
    if not os.path.exists(directory):
        print(f"The directory {directory} does not exist.")
        return

    # Iterate over the items in the directory
    for item in os.listdir(directory):
        item_path = os.path.join(directory, item)

        # If the item is a directory, delete it
        if os.path.isdir(item_path) and keep_directory not in item_path:
            try:
                shutil.rmtree(item_path)
                print(f"Deleted folder: {item_path}")
            except Exception as e:
                print(f"Failed to delete {item_path}. Reason: {e}")
        else:
            print(f"Skipping non-folder/selected to keep item: {item_path}")


def move_contents_to_parent(directory):
    # Check if the directory exists
    if not os.path.exists(directory):
        print(f"The directory {directory} does not exist.")
        return

    # Get the parent directory
    parent_directory = os.path.dirname(directory)

    # Iterate over the items in the directory
    for item in os.listdir(directory):
        source_path = os.path.join(directory, item)
        destination_path = os.path.join(parent_directory, item)

        # Move the item to the parent directory
        try:
            shutil.move(source_path, destination_path)
            print(f"Moved {source_path} to {destination_path}")
        except Exception as e:
            print(f"Failed to move {source_path}. Reason: {e}")

    # Optionally, remove the now-empty directory
    try:
        os.rmdir(directory)
        print(f"Removed the empty directory: {directory}")
    except Exception as e:
        print(f"Failed to remove the directory {directory}. Reason: {e}")


if __name__ == '__main__':
    checkpoint_dir = os.path.join(os.curdir, "ckpt")
    if not os.path.exists(checkpoint_dir):
        os.mkdir(checkpoint_dir)

    snapshot_download(repo_id="Wuvin/Unique3D", local_dir=checkpoint_dir, repo_type="space")
    delete_all_subfolders(checkpoint_dir, "ckpt")
    dir_to_move = os.path.join(checkpoint_dir, "ckpt")
    move_contents_to_parent(dir_to_move)

