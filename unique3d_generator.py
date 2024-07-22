import os

if 'CUDA_VISIBLE_DEVICES' not in os.environ:
    os.environ['CUDA_VISIBLE_DEVICES'] = '0'
os.environ['TRANSFORMERS_OFFLINE'] = '0'
os.environ['DIFFUSERS_OFFLINE'] = '0'
os.environ['HF_HUB_OFFLINE'] = '0'
os.environ['GRADIO_ANALYTICS_ENABLED'] = 'False'
os.environ['HF_ENDPOINT'] = 'https://hf-mirror.com'

import torch

torch.set_float32_matmul_precision('medium')
torch.backends.cuda.matmul.allow_tf32 = True
torch.set_grad_enabled(True)

from app.gradio_3dgen import generate3dv2
from app.all_models import model_zoo


if __name__ == '__main__':
    image_name = "./app/examples/bag.png"
    remove_background = True

    model_zoo.init_models()
    mesh, video = generate3dv2(image_name, remove_background, 42)


