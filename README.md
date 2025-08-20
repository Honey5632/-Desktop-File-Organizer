# 🗂️Desktop-File-Organizer
A simple Python script that automatically organizes files on your desktop into categorized folders (Images, Documents, Music, Web Files, etc.).

# ✨ Features

- Automatically detects file types based on extensions.
- Moves files into categorized folders:
- 🖼️ Images (.png, .jpg, .jpeg)
- 📄 Documents (.pdf, .docx, .txt)
- 🌐 Web Files (.html, .js, .url, .php, .css)
- 🔗 Shortcuts (.lnk)
- 📦 Compressed Files (.zip)
- 🎵 Music (.mp3)
- 📁 Other Files/Folders (left untouched)
- Creates folders automatically if they don’t exist.
- Prints a summary of all organized files.

# 🚀 Getting Started

## 1️⃣ Prerequisites

- Python 3.6+ installed on your system.
- Works on Windows (default paths use Desktop).

## 2️⃣ Installation

Clone the repository:
```bash
git clone https://github.com/your-username/desktop-file-organizer.git
cd desktop-file-organizer
```

## 3️⃣ Usage

1. Open the script in your editor and update the path to your desktop:
```python
os.chdir('C:/Users/YourUsername/Desktop')
```
Replace YourUsername with your actual Windows username.

2. Run the script:
```bash
python organizer.py
```

3. Watch your desktop get neatly organized 🎉

Example Output
```less
File picture.jpg Moved
File resume.pdf Moved
File song.mp3 Moved

🖼️ Images: ['picture.jpg']
📄 Documents: ['resume.pdf']
🎵 Music: ['song.mp3']
```

# ⚠️ Notes

- Double-check file movements: this script moves files, it does not copy them.
- If you already organized your desktop, the script will print "already cleaned!" for empty categories.
- Works best on Windows, but can be adapted for Linux/Mac by changing paths.

# 🛠️ Future Improvements
- Add support for more file types (e.g., videos .mp4, .avi).
- Add configuration file for custom folder names.
- GUI version with drag-and-drop support.

# 📜 License

This project is licensed under the MIT License — free to use and modify.
