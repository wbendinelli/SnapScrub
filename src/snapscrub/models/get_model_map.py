import logging
import torch
from torchvision import models, transforms
from tensorflow.keras.applications import (
    MobileNetV3Large, InceptionResNetV2, ResNet101, EfficientNetB7, DenseNet201
)
from tensorflow.keras.applications.mobilenet_v3 import preprocess_input as mobilenetv3_preprocess
from tensorflow.keras.applications.inception_resnet_v2 import preprocess_input as inceptionresnet_preprocess
from tensorflow.keras.applications.resnet import preprocess_input as resnet_preprocess
from tensorflow.keras.applications.efficientnet import preprocess_input as efficientnet_preprocess
from tensorflow.keras.applications.densenet import preprocess_input as densenet_preprocess

def get_model_map(framework="tensorflow"):
    """
    Load and return pre-trained models and their corresponding preprocessors.

    Parameters:
        framework (str): Either 'tensorflow' or 'pytorch'.

    Returns:
        dict: A dictionary of models and their preprocessors.
    """
    logging.info(f"Loading models for framework: {framework}")

    if framework == "tensorflow":
        model_map = {
            "MobileNetV3": (MobileNetV3Large(weights="imagenet", include_top=False, pooling="avg"), mobilenetv3_preprocess),
            "InceptionResNetV2": (InceptionResNetV2(weights="imagenet", include_top=False, pooling="avg"), inceptionresnet_preprocess),
            "ResNet101": (ResNet101(weights="imagenet", include_top=False, pooling="avg"), resnet_preprocess),
            "EfficientNetB7": (EfficientNetB7(weights="imagenet", include_top=False, pooling="avg"), efficientnet_preprocess),
            "DenseNet201": (DenseNet201(weights="imagenet", include_top=False, pooling="avg"), densenet_preprocess),
        }
    elif framework == "pytorch":
        preprocess = transforms.Compose([
            transforms.Resize((224, 224)),
            transforms.ToTensor(),
            transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
        ])
        model_map = {
            "resnet18": (models.resnet18(pretrained=True), preprocess),
            "resnet34": (models.resnet34(pretrained=True), preprocess),
            "efficientnet_b0": (models.efficientnet_b0(pretrained=True), preprocess),
            "vision_transformer": (models.vit_b_16(pretrained=True), preprocess)
        }
    else:
        raise ValueError("Unsupported framework. Choose 'tensorflow' or 'pytorch'.")

    return model_map