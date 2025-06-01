from torchvision.models import squeezenet1_1, SqueezeNet1_1_Weights
from torchvision import transforms
import torch
from PIL import Image

weights = SqueezeNet1_1_Weights.DEFAULT
model = squeezenet1_1(weights=weights)
model.eval()

transform = weights.transforms()

# ImageNet class IDs for various cat breeds
cat_class_ids = list(range(281, 286))

def is_cat_image(image: Image.Image) -> str:
    img_t = transform(image).unsqueeze(0)
    with torch.no_grad():
        output = model(img_t)
    probabilities = torch.nn.functional.softmax(output[0], dim=0)
    top1 = torch.argmax(probabilities).item()
    if top1 in cat_class_ids:
        return "Yes, this is a cat."
    else:
        return "No, this is not a cat."