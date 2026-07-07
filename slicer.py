import os
import shutil
import random

def split_and_save_dataset(src_root, output_base, split_ratios):
    """
    Slices a root dataset into distinct physical folders on disk based on target ratios.
    
    Structure created:
    output_base/
      ├── Split_50_50/
      │     ├── train/ (with emotion folders)
      │     └── test/  (with emotion folders)
      ├── Split_70_30/ ...
    """
    # Find all emotion class subdirectories
    classes = [d for d in os.listdir(src_root) if os.path.isdir(os.path.join(src_root, d))]
    print(f"Found classes: {classes}")

    for ratio_name, train_pct in split_ratios.items():
        print(f"\nDistributing files for configuration physical layout: {ratio_name}...")
        
        # Build paths for this specific experiment split
        exp_root = os.path.join(output_base, f"Split_{ratio_name.replace(':', '_')}")
        train_root = os.path.join(exp_root, "train")
        test_root = os.path.join(exp_root, "test")
        
        # Process every emotion category independently to preserve stratified balance
        for cls in classes:
            cls_src_dir = os.path.join(src_root, cls)
            all_images = [f for f in os.listdir(cls_src_dir) if f.lower().endswith(('.png', '.jpg', '.jpeg'))]
            
            # Shuffle deterministically so your splits are uniform
            random.seed(42)
            random.shuffle(all_images)
            
            # Calculate the explicit file index boundary split point
            split_idx = int(len(all_images) * train_pct)
            train_images = all_images[:split_idx]
            test_images = all_images[split_idx:]
            
            # Create target structural class directories on storage drive
            os.makedirs(os.path.join(train_root, cls), exist_ok=True)
            os.makedirs(os.path.join(test_root, cls), exist_ok=True)
            
            # Physically copy images over to the training partition destination
            for img in train_images:
                shutil.copy2(os.path.join(cls_src_dir, img), os.path.join(train_root, cls, img))
                
            # Physically copy images over to the testing partition destination
            for img in test_images:
                shutil.copy2(os.path.join(cls_src_dir, img), os.path.join(test_root, cls, img))
                
        print(f"Successfully generated structured folders at: {exp_root}")

if __name__ == "__main__":
    # Target configurations to test
    RATIOS = {
        "50_50": 0.50,
        "70_30": 0.70,
        "90_10": 0.90
    }
    
    # EDIT THESE PATHS
    RAW_DATASET_PATH = "data/affectnet"
    EXPORT_TARGET_PATH = "data/affectnet_splits"
    
    split_and_save_dataset(RAW_DATASET_PATH, EXPORT_TARGET_PATH, RATIOS)
    print("\n All physical splits have been created and saved to disk safely!")