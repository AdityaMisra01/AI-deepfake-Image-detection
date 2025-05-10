import os
from PIL import Image
from pathlib import Path

def clean_dataset(root_dir='dataset'):
    """Remove invalid files and corrupted images"""
    print("\n🧹 Cleaning dataset...")
    
    valid_exts = ('.jpg', '.jpeg', '.png')
    removed_count = 0

    for path in Path(root_dir).rglob('*'):
        # Skip directories
        if path.is_dir():
            continue
            
        # Check file extension
        if path.suffix.lower() not in valid_exts:
            print(f"Removing invalid file: {path}")
            os.remove(path)
            removed_count += 1
            continue

        # Verify image integrity
        try:
            with Image.open(path) as img:
                img.verify()
        except (IOError, SyntaxError) as e:
            print(f"Removing corrupted file: {path} - {str(e)}")
            os.remove(path)
            removed_count += 1

    print(f"\n✅ Removed {removed_count} invalid/corrupted files")

if __name__ == '__main__':
    clean_dataset()
    