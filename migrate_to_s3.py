import os
import re

# CONFIGURATION
# Replace this with your actual S3 or CloudFront distribution domain
S3_BASE_URL = "https://s3.us-west-2.amazonaws.com/multer.com/content"
CONTENT_DIR = "./content"

# REGEX PATTERNS
# 1. Matches standard Markdown images: ![alt text](filename.ext)
MD_IMAGE_REGEX = re.compile(r'!\[(.*?)\]\((.*?)\)')

# 2. Matches front matter key-value pairs: image = "filename.ext" or thumbnail = 'filename.ext'
# Supports spaces around '=', double or single quotes, and keys like image, thumbnail, cover, etc.
FRONT_MATTER_IMAGE_REGEX = re.compile(r'(\b(?:image|thumbnail|cover|avatar|banner)\s*=\s*["\'])([^"\']+\.(?:jpg|jpeg|png|webp|gif))(["\'])', re.IGNORECASE)

def update_markdown_file(file_path, rel_dir_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # --- Process Inline Markdown Images ---
    def replace_md_url(match):
        alt_text = match.group(1)
        img_src = match.group(2)

        if img_src.startswith(('http://', 'https://', '/')):
            return match.group(0)

        new_url = f"{S3_BASE_URL}/{rel_dir_path}/{img_src}"
        return f"![{alt_text}]({new_url})"

    processed_content = MD_IMAGE_REGEX.sub(replace_md_url, content)

    # --- Process Front Matter Configuration Images ---
    def replace_front_matter_url(match):
        prefix = match.group(1)   # e.g., 'image = "'
        img_src = match.group(2)  # e.g., 'photo.jpg'
        suffix = match.group(3)   # e.g., '"'

        if img_src.startswith(('http://', 'https://', '/')):
            return match.group(0)

        new_url = f"{S3_BASE_URL}/{rel_dir_path}/{img_src}"
        return f"{prefix}{new_url}{suffix}"

    final_content = FRONT_MATTER_IMAGE_REGEX.sub(replace_front_matter_url, processed_content)

    # Write changes back if migrations occurred
    if content != final_content:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(final_content)
        print(f"Updated: {file_path}")

def main():
    # Recursively traverse the content directory
    for root, dirs, files in os.walk(CONTENT_DIR):
        for file in files:
            if file.endswith(('.md', '.markdown')):
                file_path = os.path.join(root, file)

                # Get relative path starting from inside the 'content' directory
                # Example: content/posts/2023/my-post -> posts/2023/my-post
                rel_path = os.path.relpath(root, CONTENT_DIR).replace("\\", "/")

                update_markdown_file(file_path, rel_path)

if __name__ == "__main__":
    # BACK UP YOUR CONTENT FOLDER BEFORE RUNNING!
    print("Starting S3 URL migration...")
    main()
    print("Migration finished.")
