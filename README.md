# SnapScrub - Automated Image Classification

## 📌 Overview
**SnapScrub** automates the process of selecting and organizing high-quality images using advanced AI models. The pipeline evaluates images based on sharpness, exposure, and similarity, ensuring the best selection for photography, social media, and digital marketing.

---

## 🎯 Key Features

- **Automatic Image Processing:** Resize, rename, and clean images.
- **Quality Assessment:** Sharpness and exposure scoring.
- **Duplicate Removal:** SSIM-based and deep learning embedding comparisons.
- **Cross-Framework Compatibility:** Supports TensorFlow and PyTorch models.
- **Configurable Pipeline:** Adjustable via `config.yaml`.
- **AI-Based Scoring:** Deep learning models to rank images by visual quality.
- **Customizable Selection:** Configurable thresholds to fine-tune image selection.

---

## 📁 Project Structure

```
SnapScrub/
├── notebooks/       # Jupyter notebooks for exploratory analysis
├── scripts/         # Auxiliary scripts for specific tasks
├── src/             # Main source code for image processing
│   ├── data/        # Modules for data manipulation and preparation
│   ├── evaluation/  # Modules for image quality assessment
│   ├── models/      # AI model implementations for prediction
│   ├── results/     # Modules for results management
│   └── utils/       # Utility and helper functions
├── .gitignore       # Specifies files/folders to ignore in Git
├── LICENSE          # Project license information
├── README.md        # Project documentation
├── clear_data.py    # Data cleanup script
├── environment.yml  # Conda environment configuration file
├── main.py          # Main script to run the pipeline
└── setup.py         # Project installation script
```

---

## 🛠 Installation

### Prerequisites
- Python 3.8+
- TensorFlow 2.x
- PyTorch 1.x
- OpenCV
- Pandas and NumPy

### Installation Steps

```bash
git clone https://github.com/wbendinelli/SnapScrub.git
cd SnapScrub
pip install -r requirements.txt
```

To install using Conda:

```bash
conda env create -f environment.yml
conda activate snapscrub
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

### Run the full pipeline:
```bash
python main.py
```

### Run specific stages:
```bash
python main.py --stage resize
python main.py --stage evaluate
python main.py --stage select
```

---

## 🔍 Evaluation Metrics

- **Sharpness:** Measures image clarity and detail level.
- **Exposure:** Detects under/over-exposure in images.
- **Similarity:** Detects and removes duplicate images using multiple algorithms.

---

## 🧪 Running Tests

To run unit tests, execute:

```bash
pytest tests/
```

---

## 📊 Results

Final selected images are stored in the `results/` folder, organized by framework and model.

---

## 📚 References

- Wang, Z., Bovik, A. C., Sheikh, H. R., & Simoncelli, E. P. (2004). "Image quality assessment: from error visibility to structural similarity". IEEE Transactions on Image Processing, 13(4), 600-612.
- He, K., Zhang, X., Ren, S., & Sun, J. (2016). "Deep residual learning for image recognition". In Proceedings of the IEEE conference on computer vision and pattern recognition (pp. 770-778).
- Howard, A. G., et al. (2017). "MobileNets: Efficient Convolutional Neural Networks for Mobile Vision Applications". arXiv preprint arXiv:1704.04861.
- [TensorFlow Documentation](https://www.tensorflow.org/api_docs)
- [PyTorch Documentation](https://pytorch.org/docs/stable/index.html)

---

## 💡 Future Improvements

- GPU acceleration support for faster processing.
- Web-based user interface for image preview and selection.
- AI-driven aesthetic scoring using social media engagement prediction.
- Integration with cloud storage services (AWS, GCP).

---

## 🤝 Contributing

We welcome contributions! Follow these steps:

1. Fork the repository.
2. Create a new feature branch (`git checkout -b feature-branch`).
3. Commit your changes (`git commit -m "Add new feature"`).
4. Push the changes (`git push origin feature-branch`).
5. Open a Pull Request for review.

---

## 📄 License

This project is licensed under the MIT License.

---

## 📬 Contact

For inquiries or support, please open a [GitHub Issue](https://github.com/wbendinelli/SnapScrub/issues).
