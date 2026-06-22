import requests
import os


def download_image(url, filename):

    if not url:
        return None

    # Skip Base64 placeholder images
    if url.startswith("data:image"):
        return None

    os.makedirs("data/raw/images", exist_ok=True)

    filepath = f"data/raw/images/{filename}"

    try:
        response = requests.get(url, timeout=10)

        if response.status_code == 200:
            with open(filepath, "wb") as f:
                f.write(response.content)

            return filepath

    except Exception as e:
        print("Image download failed:", e)

    return None