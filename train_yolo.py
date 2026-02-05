from ultralytics import YOLO

# Path to your dataset
data_yaml_path = "/blue/bsc4892/aileenlavelle/PBC_Object_Detection/Jupiter_Inlet/jupiter_inlet_yolo/data.yaml"

# Load YOLO26 model
model = YOLO('yolo26s.pt')

# Train the model
results = model.train(
    data=data_yaml_path,
    epochs=100,
    imgsz=2048,
    batch=4,
    rect=True,
    device=0,
    
    mosaic=0.5,
    scale=0.2,
    fliplr=0.5,
    flipud=0.0,
    
    patience=50,
    save=True,
    plots=True,
    
    project='jupiter_inlet',
    name='train',
)

print("Training complete!")
