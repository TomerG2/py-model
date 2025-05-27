from torchvision import models, transforms
import torch
from PIL import Image

model = models.mobilenet_v2(pretrained=True)
model.eval()

transform = transforms.Compose([
    transforms.Resize(256),
    transforms.CenterCrop(224),
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.485, 0.456, 0.406],
                         std=[0.229, 0.224, 0.225])
])

# Rough approximation: ImageNet class indices for cats
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