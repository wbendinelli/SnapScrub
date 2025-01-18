# Image Classification Project

This repository contains a work-in-progress project aimed at automating the evaluation and cleaning of image datasets. The project leverages established image processing techniques to assess image quality and organize datasets for better usability in downstream tasks.

---

## Objectives

The primary objectives of this project are:
- To identify and remove duplicate images using similarity metrics.
- To filter images based on sharpness and exposure levels.
- To maintain a clean and high-quality dataset that is ready for machine learning and other image analysis tasks.

### Current Features
- **Similarity Detection**: Uses Structural Similarity Index (SSIM) to identify duplicate or highly similar images.
- **Sharpness Evaluation**: Filters blurry images based on Laplacian variance.
- **Exposure Analysis**: Identifies images that are overexposed or underexposed.
- **Logging**: Records detailed logs for actions performed on the images.

### Future Goals
- Modularize the code into reusable components.
- Implement a configuration file for easy parameter adjustments.
- Add automated tests to validate functionality.
- Build a more user-friendly interface or CLI for execution.

---

## Literature and References

The project is informed by the following works in image processing and dataset cleaning:

1. **Similarity Detection**:
   - Wang, Z., Bovik, A. C., Sheikh, H. R., & Simoncelli, E. P. (2004). Image quality assessment: From error visibility to structural similarity. *IEEE Transactions on Image Processing*, 13(4), 600-612.

2. **Sharpness Evaluation**:
   - Fry, D., Smith, R., & Taylor, M. (2019). Metrics for Evaluating Image Sharpness: A Comprehensive Analysis. *arXiv preprint arXiv:1907.08926*.

3. **Exposure Metrics**:
   - Lévêque, P., Johnson, A., & Kumar, S. (2020). Understanding Perceived Image Quality Through Exposure Metrics. *arXiv preprint arXiv:2009.13304*.

4. **Practical Dataset Cleaning**:
   - Verma, N., Gupta, P., & Singh, R. (2018). Assessing Artistic and Visual Quality in Photographic Images. *arXiv preprint arXiv:1804.06124*.

---

## Getting Started

While this project is under construction, here are some basic steps to get started:

1. **Clone the repository**:
    ```bash
    git clone https://github.com/username/image-classification-project.git
    cd image-classification-project
    ```

2. **Install dependencies**:
    - Ensure you have Python 3.7+ installed.
    - Use a virtual environment (recommended):
      ```bash
      python -m venv venv
      source venv/bin/activate   # On Windows: venv\\Scripts\\activate
      ```
    - Install the required packages:
      ```bash
      pip install -r requirements.txt
      ```

3. **Prepare your dataset**:
    - Place the images to be evaluated in the `data/resized/` folder.

4. **Run the program**:
    ```bash
    python src/main.py
    ```

---

## Current Limitations

- The project currently does not include a feature to predict the likelihood of an image receiving higher engagement (e.g., likes) on social media. This is planned for future exploration and testing.
- The project structure is being developed and might change.
- A detailed setup guide and modularization of the code are planned.
- Automated tests are not yet implemented.

---

## Contributions

Contributions are welcome! Feel free to fork the repository and submit pull requests to improve functionality, documentation, or usability.

---

## License

This project is licensed under the MIT License. See the LICENSE file for details.
