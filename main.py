import os
import shutil

os.chdir('C:/Users/Mohit/Desktop')
# The original list of filenames
file_list = os.listdir()

# Create empty lists for each category
images = []
documents = []
web_files = []
shortcuts = []
compressed_files = []
folders_and_other = []
Music = []

# Iterate through each item in the list
try:
    for item in file_list:
        # Use .endswith() with a tuple of possible extensions
        if item.endswith(('.png', '.jpg', '.jpeg')):
            os.makedirs('C:/Users/Mohit/Desktop/images', exist_ok=True)
            images.append(item)
            source_path = os.path.join('C:/Users/Mohit/Desktop/', item)
            destination_path = os.path.join('C:/Users/Mohit/Desktop/', 'images')
            shutil.move(source_path, destination_path)
            print(f"File {item} Moved")

        elif item.endswith(('.pdf', '.docx', '.txt')):
            documents.append(item)
            os.makedirs('C:/Users/Mohit/Desktop/text_doc', exist_ok=True)
            images.append(item)
            source_path = os.path.join('C:/Users/Mohit/Desktop/', item)
            destination_path = os.path.join('C:/Users/Mohit/Desktop/', 'text_doc')
            shutil.move(source_path, destination_path)
            print(f"File {item} Moved")

        elif item.endswith(('.html', 'js', '.url', '.php', '.css')):
            web_files.append(item)
            os.makedirs('C:/Users/Mohit/Desktop/web_files', exist_ok=True)
            images.append(item)
            source_path = os.path.join('C:/Users/Mohit/Desktop/', item)
            destination_path = os.path.join('C:/Users/Mohit/Desktop/', 'web_files')
            shutil.move(source_path, destination_path)
            print(f"File {item} Moved")

        elif item.endswith('.lnk'):
            shortcuts.append(item)
            os.makedirs('C:/Users/Mohit/Desktop/shortcuts', exist_ok=True)
            images.append(item)
            source_path = os.path.join('C:/Users/Mohit/Desktop/', item)
            destination_path = os.path.join('C:/Users/Mohit/Desktop/', 'shortcuts')
            shutil.move(source_path, destination_path)

        elif item.endswith('.zip'):
            compressed_files.append(item)
            os.makedirs('C:/Users/Mohit/Desktop/compressed_files', exist_ok=True)
            images.append(item)
            source_path = os.path.join('C:/Users/Mohit/Desktop/', item)
            destination_path = os.path.join('C:/Users/Mohit/Desktop/', 'compressed_files')
            shutil.move(source_path, destination_path)

        elif item.endswith('.mp3'):
            Music.append(item)
            os.makedirs('C:/Users/Mohit/Desktop/Music', exist_ok=True)
            images.append(item)
            source_path = os.path.join('C:/Users/Mohit/Desktop/', item)
            destination_path = os.path.join('C:/Users/Mohit/Desktop/', 'Music')
            shutil.move(source_path, destination_path)

        else:
            # If it doesn't match any category, treat it as a folder or other file
            folders_and_other.append(item)

except FileNotFoundError:
    print(f"Error: The source directory was not found.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")

# Print the separated lists
print("🖼️ Images:",end=' ')
if images:
    print(images)
else:
    print("already cleaned!")

print("\n📄 Documents:",end=' ')
if documents:
    print(documents)
else:
    print("already cleaned!")

print("\n🌐 Web Files:",end=' ')
if web_files:
    print(web_files)
else:
    print("already cleaned!")

print("\n🔗 Shortcuts:",end=' ')
if shortcuts:
    print(shortcuts)
else:
    print("already cleaned!")

print("\n📦 Compressed Files:",end=' ')
if compressed_files:
    print(compressed_files)

print("\n📁 Folders and Other Files:",end=' ')
if folders_and_other:
    print(folders_and_other)
print("\n Music")
if Music:
    print(Music)