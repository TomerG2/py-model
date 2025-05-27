# py-model

This project provides a minimal FastAPI application that lets you upload an image and determines whether it's a cat using a pre-trained MobileNetV2 model from torchvision.

## Run locally
```bash
podman build -t py-model .
podman run -p 8080:8080 py-model
```

Then visit http://localhost:8080