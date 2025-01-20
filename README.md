# Image Classification Project

## 📌 Overview
The **Image Classification** project automates the process of selecting and organizing high-quality images using advanced AI models. It evaluates images based on sharpness, exposure, and similarity, ensuring optimal selection.

### 🎯 Key Features
- **Automatic Image Processing:** Resize, rename, and clean images.
- **Quality Assessment:** Sharpness and exposure scoring.
- **Duplicate Removal:** SSIM-based and deep learning embedding comparisons.
- **Cross-Framework Compatibility:** Supports TensorFlow and PyTorch models.
- **Configurable Pipeline:** Adjustable via `config.yaml`.

---

## 📁 Project Structure

```
Image_Classification/
📂 src/         # Source code for image processing
📂 tests/       # Test scripts
📂 data/        # Raw and processed images
📂 results/     # Final output images
📂 notebooks/   # Jupyter notebooks for analysis
📄 requirements.txt
📄 README.md
```

---

## 🛠 Installation

### Prerequisites
- Python 3.8+
- TensorFlow 2.x
- PyTorch 1.x
- OpenCV
- Pandas and NumPy

### Steps
```bash
git clone https://github.com/yourusername/image-classification.git
cd image-classification
pip install -r requirements.txt
```

---

## ⚙️ Configuration
Modify `config.yaml` to adjust processing parameters:

```yaml
image_processing:
  resize_width: 512
  resize_height: 512

evaluation_criteria:
  similarity_threshold: 0.85
  sharpness_threshold: 100
  exposure_tolerance: 0.2
```

---

## 🚀 Usage

### Run full pipeline:
```bash
python src/main.py --stage all
```

### Run specific stages:
```bash
python src/main.py --stage resize
python src/main.py --stage evaluate
python src/main.py --stage select
```

---

## 🔍 Evaluation Metrics

- **Sharpness:** Measures image clarity.
- **Exposure:** Detects under/over-exposure.
- **Similarity:** Removes duplicates.

---

## 🧪 Running Tests
```bash
pytest tests/
```

---

## 📊 Results
Final selected images are stored in the `results/` folder.

---

## 📚 References

- Wang, Z., Bovik, A. C., Sheikh, H. R., & Simoncelli, E. P. (2004). "Image quality assessment: from error visibility to structural similarity". IEEE Transactions on Image Processing, 13(4), 600-612.
- He, K., Zhang, X., Ren, S., & Sun, J. (2016). "Deep residual learning for image recognition". In Proceedings of the IEEE conference on computer vision and pattern recognition (pp. 770-778).
- Howard, A. G., et al. (2017). "MobileNets: Efficient Convolutional Neural Networks for Mobile Vision Applications". arXiv preprint arXiv:1704.04861.
- TensorFlow Documentation: https://www.tensorflow.org/api_docs
- PyTorch Documentation: https://pytorch.org/docs/stable/index.html

---

## 💡 Future Improvements
- GPU acceleration support.
- Web-based UI for preview.
- AI-driven enhancements.

---

## 🤝 Contributing

1. Fork the repository.
2. Create a feature branch.
3. Commit changes and create a pull request.

---

## 📄 License

This project is licensed under the MIT License.

---

## 📬 Contact
For inquiries, please reach out via [GitHub Issues](https://github.com/yourusername/image-classification/issues).

---

