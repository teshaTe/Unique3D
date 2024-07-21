import os

import torch
from PIL import Image

from app.gradio_3dgen import generate3dv2
from app.all_models import model_zoo


if __name__ == '__main__':
    image_name = "./app/examples/bag.png"
    remove_background = True

    model_zoo.init_models()
    mesh, video = generate3dv2(image_name, remove_background, 42)


