"""
Download 4 conference/meeting images from Unsplash and remove their backgrounds.
Saves as new1.png → new4.png in the same folder.
Requires: pip install rembg requests pillow
"""
import urllib.request
import sys
import os

# 4 high-quality meeting/conference images from Unsplash (direct download links)
IMAGES = [
    # Two people in business discussion / handshake
    ("https://images.unsplash.com/photo-1600880292089-90a7e086ee0c?w=800&q=90", "new1_raw.jpg"),
    # Conference room with people around table
    ("https://images.unsplash.com/photo-1556761175-4b46a572b786?w=800&q=90", "new2_raw.jpg"),
    # Two people talking / networking
    ("https://images.unsplash.com/photo-1573497491765-dccce02b29df?w=800&q=90", "new3_raw.jpg"),
    # Presenter at conference / speaking
    ("https://images.unsplash.com/photo-1561489396-888724a1543d?w=800&q=90", "new4_raw.jpg"),
]

OUTPUT = ["new1.png", "new2.png", "new3.png", "new4.png"]

print("Downloading images...")
for i, (url, fname) in enumerate(IMAGES):
    print(f"  [{i+1}/4] {fname}")
    urllib.request.urlretrieve(url, fname)

# Try rembg for background removal
try:
    from rembg import remove
    from PIL import Image
    import io

    print("\nRemoving backgrounds with rembg...")
    for i, (_, raw) in enumerate(IMAGES):
        print(f"  [{i+1}/4] Processing {raw} → {OUTPUT[i]}")
        with open(raw, "rb") as f:
            inp = f.read()
        out = remove(inp)
        with open(OUTPUT[i], "wb") as f:
            f.write(out)
        os.remove(raw)
    print("\nDone! Saved: " + ", ".join(OUTPUT))

except ImportError:
    print("\nrembg not installed. Installing...")
    os.system("pip install rembg[gpu] pillow")
    print("Please run this script again after installation.")
    print("\nAlternatively, manually go to https://www.remove.bg and upload these files:")
    for _, raw in IMAGES:
        print(f"  - {os.path.abspath(raw)}")
