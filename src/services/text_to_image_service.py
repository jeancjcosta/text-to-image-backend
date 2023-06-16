import uuid
import base64
import torch
import os
from diffusers import StableDiffusionPipeline


class TextToImageService:

    def __init__(self):
        pass

    def generate_with_diffusers(self, texts: []):
        dirname = os.path.dirname(__file__)
        dirname = dirname.replace("src\\services", "")
        dirname = dirname.replace("\\", "/")

        model_id = "runwayml/stable-diffusion-v1-5"
        pipe = StableDiffusionPipeline.from_pretrained(model_id, torch_dtype=torch.float16)
        pipe = pipe.to("cuda")

        image = pipe(texts[0]).images[0]

        imagesb64 = []
        filename = dirname + 'generated_images/image' + str(uuid.uuid4()) + '.png'
        image.save(filename)
        with open(filename, "rb") as img_file:
            b64_string = base64.b64encode(img_file.read())
        imagesb64.append(b64_string)
        print(filename)
        return imagesb64


text_to_image_service = TextToImageService()
