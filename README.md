![Python](https://img.shields.io/badge/Python-3.12-blue?logo=python)
![License](https://img.shields.io/badge/License-MIT-green)
![Status](https://img.shields.io/badge/Status-Active-brightgreen)
![Made With](https://img.shields.io/badge/Made%20With-Pillow%2C%20NumPy%2C%20scikit--learn-blue)

# 🎨 Color Palette Extractor

Extract dominant colors from any image, generate a clear color palette image, and export RGB values for design or analysis purposes.

---

## 📌 Features

✅ Extract **N dominant colors** from images using KMeans clustering.  
✅ Generates a **visual color palette image** for easy reference.  
✅ Saves RGB values in a clean `.txt` file.  
✅ Automatically opens outputs after generation.  
✅ Beginner-friendly, well-commented, modular Python code for learning.

---

## 🖼️ Example Outputs

- **Input:** An image of your choice (JPG, PNG, etc.)
- **Output:**
  - `palette_output.txt` with extracted RGB values.
  - `palette_output_image.png` showing color swatches.

![Palette Example](assets/palette_example.png)

---

## 🚀 Installation

1️⃣ **Clone the repository:**

```bash
git clone https://github.com/sganeshe/color-palette-extractor.git
cd color-palette-extractor
```

2️⃣ **Install dependencies:**

```bash
pip install pillow numpy scikit-learn
```

---

## ⚙️ Usage

Run the extractor:

```bash
python palette_extractor.py
```

You will be prompted to:
- Enter the **path to the image** you want to process.
- Enter **number of colors** to extract.
- Choose where to save outputs.

The script will generate:
- A `.txt` file containing RGB color values.
- A `.png` palette image displaying swatches of the extracted colors.
- Automatically open the outputs for immediate review.

---

## 📂 Project Structure

```
color-palette-extractor/
├── palette_extractor.py
├── README.md
└── assets/
    ├── input_example.jpg
    └── palette_example.png
```

---

## 🛠️ Technologies Used

- **Python 3.12**
- **Pillow (PIL)**: Image loading, conversion, and saving.
- **NumPy**: Efficient image pixel data handling.
- **scikit-learn (KMeans)**: Clustering to find dominant colors.
- **OS Module**: Path management and file operations.

---

## 📚 Learning Outcomes

This project will help you learn:
- How images are represented as RGB arrays.
- How KMeans clustering can extract dominant colors.
- Basic image processing using Pillow.
- File handling and OS path operations in Python.
- Generating clean visual outputs programmatically.

---

## 💡 Future Enhancements

- [ ] Add hex code export for web and UI designers.
- [ ] CLI improvements using `argparse` for flags.
- [ ] Drag-and-drop GUI using Tkinter.
- [ ] Error handling and input validation improvements.

---

## 🤝 Contributing

Contributions are welcome! Feel free to fork, improve, and submit PRs to enhance this project for other learners.

---

## 📄 License

This project is released under the **MIT License**. Feel free to use, modify, and share.

---

## 🙏 Acknowledgements

- [Pillow Documentation](https://pillow.readthedocs.io/en/stable/)
- [NumPy Documentation](https://numpy.org/doc/stable/)
- [scikit-learn Documentation](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.KMeans.html)

---

## 📬 Contact

For questions or collaborations:
- GitHub: [sganeshe](https://github.com/sganeshe)
- Email: saumyaganeshe@gmail.com

---

✨ **Happy coding and color extracting!** 🎨
