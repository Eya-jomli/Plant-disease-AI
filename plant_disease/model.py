import torch
import torch.nn as nn
import torchvision.models as models
import torchvision.transforms as transforms
from PIL import Image
import io
import os

# Defining the plant disease model architecture
class Plant_Disease_Model(nn.Module):

    def __init__(self):
        super().__init__()
        # Load the pretrained ResNet34 model
        self.network = models.resnet34(pretrained=True)
        num_ftrs = self.network.fc.in_features
        self.network.fc = nn.Linear(num_ftrs, 38)  # 38 classes

    def forward(self, xb):
        out = self.network(xb)
        return out

# Define image transformations for the input image
transform = transforms.Compose([
    transforms.Resize(size=128),
    transforms.ToTensor()
])

# List of plant disease classes
num_classes = ['Apple___Apple_scab', 'Apple___Black_rot', 'Apple___Cedar_apple_rust', 'Apple___healthy', 
               'Blueberry___healthy', 'Cherry_(including_sour)___Powdery_mildew', 'Cherry_(including_sour)___healthy', 
               'Corn_(maize)___Cercospora_leaf_spot Gray_leaf_spot', 'Corn_(maize)___Common_rust_', 
               'Corn_(maize)___Northern_Leaf_Blight', 'Corn_(maize)___healthy', 'Grape___Black_rot', 
               'Grape___Esca_(Black_Measles)', 'Grape___Leaf_blight_(Isariopsis_Leaf_Spot)', 'Grape___healthy', 
               'Orange___Haunglongbing_(Citrus_greening)', 'Peach___Bacterial_spot', 'Peach___healthy',
               'Pepper,_bell___Bacterial_spot', 'Pepper,_bell___healthy', 'Potato___Early_blight', 
               'Potato___Late_blight', 'Potato___healthy', 'Raspberry___healthy', 'Soybean___healthy', 
               'Squash___Powdery_mildew', 'Strawberry___Leaf_scorch', 'Strawberry___healthy', 'Tomato___Bacterial_spot', 
               'Tomato___Early_blight', 'Tomato___Late_blight', 'Tomato___Leaf_Mold', 'Tomato___Septoria_leaf_spot', 
               'Tomato___Spider_mites Two-spotted_spider_mite', 'Tomato___Target_Spot', 
               'Tomato___Tomato_Yellow_Leaf_Curl_Virus', 'Tomato___Tomato_mosaic_virus', 'Tomato___healthy']

# Initialize and load the model
model = Plant_Disease_Model()

# Load model weights
model_path = os.path.join(os.path.dirname(__file__), 'Models/plantDisease-resnet34.pth')
model.load_state_dict(torch.load(model_path, map_location=torch.device('cpu')))
model.eval()  # Set the model to evaluation mode

# Function to predict the disease from an image
def predict_image(img):
    try:
        # Convert image to PIL format and apply transformations
        img_pil = Image.open(io.BytesIO(img))
        tensor = transform(img_pil)
        xb = tensor.unsqueeze(0)  # Add batch dimension

        # Get model predictions
        yb = model(xb)
        _, preds = torch.max(yb, dim=1)

        # Return predicted class
        return num_classes[preds[0].item()]
    except Exception as e:
        print(f"Error predicting image: {e}")
        return None
