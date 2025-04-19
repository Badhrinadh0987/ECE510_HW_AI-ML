import os

dataset_path = r'C:\Users\Student\Videos\COURSES\AI-ML\DDDS_Final_Pro\dataset'
valid_exts = ('.jpg', '.jpeg', '.png')

for class_name in os.listdir(dataset_path):
    class_dir = os.path.join(dataset_path, class_name)
    if os.path.isdir(class_dir):
        print(f"\n📁 Class: {class_name}")
        images = [f for f in os.listdir(class_dir) if f.lower().endswith(valid_exts)]
        for img in images:
            print(f"  - {img}")
        print(f"✅ Total valid images: {len(images)}")
