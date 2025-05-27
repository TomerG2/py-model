# py-model (Mocked Python version)

This Python version simulates an AI model that predicts whether an image is a cat based on its shape.

## Run locally
```bash
podman build -t py-model .
podman run -p 8080:8080 py-model
```

Then open http://localhost:8080