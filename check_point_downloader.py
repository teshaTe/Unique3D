import os
from huggingface_hub import snapshot_download

if __name__ == '__main__':
    checkpoint_dir = os.path.join(os.curdir, "ckpt")
    if not os.path.exists(checkpoint_dir):
        os.mkdir(checkpoint_dir)

    snapshot_download(repo_id="Wuvin/Unique3D", local_dir=checkpoint_dir, repo_type="space")
