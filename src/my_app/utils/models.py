import torch
import torch.nn as nn
from torchvision import transforms
from torchvision.models import densenet121, DenseNet121_Weights
from PIL import Image
import os
from collections import OrderedDict


class ChestXRayModel:

    """
    An object-oriented wrapper for a DenseNet-based chest X-ray classifier.
    This loads the best_model.pth checkpoint and provides a `predict` method.

    """

    PATHOLOGIES = [
        "Atelectasis", "Cardiomegaly", "Effusion", "Infiltration", "Mass", "Nodule",
        "Pneumonia", "Pneumothorax", "Consolidation", "Emphysema", "Fibrosis",
        "Pleural_Thickening", "Hernia", "Edema", "No Finding"
    ]

    def __init__(self, model_path: str, device: str = None):
        self.device = device if device is not None else (
            "cuda" if torch.cuda.is_available() else "cpu"
        )
        self.model_path = model_path
        self.model = self._load_model()

        imagenet_mean = [0.485, 0.456, 0.406]
        imagenet_std = [0.229, 0.224, 0.225]
        self.transform = transforms.Compose([
            transforms.Resize(256),
            transforms.CenterCrop(224),
            transforms.ToTensor(),
            transforms.Normalize(mean=imagenet_mean, std=imagenet_std),
        ])

    def _load_model(self) -> nn.Module:

        model = densenet121(weights=DenseNet121_Weights.IMAGENET1K_V1)
        num_feats = model.classifier.in_features
        model.classifier = nn.Sequential(
        nn.Linear(num_feats, 1024),
        nn.BatchNorm1d(1024),
        nn.ReLU(inplace=True),
        nn.Dropout(0.3),
        nn.Linear(1024, 512),
        nn.BatchNorm1d(512),
        nn.ReLU(inplace=True),
        nn.Dropout(0.3),
        nn.Linear(512, len(self.PATHOLOGIES))
    )

        if not os.path.exists(self.model_path):
            raise FileNotFoundError(f"Model file not found at: {self.model_path}")

        original_state_dict = torch.load(self.model_path, map_location=self.device)
        new_state_dict = OrderedDict()
        for k, v in original_state_dict.items():
            name = k[7:] if k.startswith("module.") else k  # remove 'module.'
            new_state_dict[name] = v

        model.load_state_dict(new_state_dict)
    
        model = model.to(self.device)
        model.eval()
        return model

    def predict(self, image: Image.Image):
      
        x = self.transform(image).unsqueeze(0).to(self.device)

        with torch.no_grad():
            logits = self.model(x) 
            probs = torch.sigmoid(logits).cpu().numpy()[0]

        results = []
        for pathology, prob in zip(self.PATHOLOGIES, probs):
            binary_label = 1 if prob > 0.5 else 0
            results.append((pathology, float(prob), binary_label))
        return results
