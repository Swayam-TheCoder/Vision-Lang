<div align="center">

# 🩺 Medical Prescription OCR Testing

This project is a testing ground for reading text from medical prescription images. It runs OCR on sample prescriptions, reports how confident the model is, and explores document layout detection as a separate experiment.

| Component | Purpose |
|---|---|
| 🔤 **PaddleOCR** | Text detection and recognition |
| 🧠 **PP-OCRv5** | Server-grade detection + recognition models |
| 🗂️ **PP-DocLayout-L** | Document layout region detection |
| 🐍 **Python 3.11** | Runtime |
| 📦 **PaddlePaddle** | Deep learning backend |

---

## 📁 Project Structure

```text
google vision/
│
├── test_ocr.py              # Main OCR testing script
├── test_layout.py           # Document layout testing
│
├── prescription.jpg         # Sample prescription image
├── pre1.jpg                 # Sample image
├── pre2.jpg                 # Sample image
│
├── .gitignore
└── README.md
```

---

## 🛠️ Requirements

| Requirement | Version / Notes |
|---|---|
| Python | **3.11.x** |
| Git | Any recent version |
| Terminal | Windows PowerShell or Terminal |

Check your Python version:

```powershell
python --version
```

Expected output:

```text
Python 3.11.x
```

> [!WARNING]
> Python 3.13 may cause compatibility problems with some PaddlePaddle packages. Use **Python 3.11** for this project.

---

## 🚀 Installation

### 1️⃣ Clone the repository

```powershell
git clone <YOUR_GITHUB_REPOSITORY_URL>
cd <PROJECT_FOLDER>
```

### 2️⃣ Create a virtual environment

```powershell
py -3.11 -m venv paddle-venv
```

Activate it:

```powershell
.\paddle-venv\Scripts\activate
```

You should now see `(paddle-venv)` at the beginning of your terminal prompt.

### 3️⃣ Upgrade pip

```powershell
python -m pip install --upgrade pip
```

### 4️⃣ Install PaddlePaddle (CPU)

```powershell
python -m pip install paddlepaddle==3.2.0 -i https://www.paddlepaddle.org.cn/packages/stable/cpu/
```

Verify the installation:

```powershell
python -c "import paddle; print(paddle.__version__)"
```

Expected output:

```text
3.2.0
```

### 5️⃣ Install PaddleOCR

```powershell
python -m pip install paddleocr
```

### 6️⃣ Install PaddleX

The layout model uses PaddleX.

```powershell
python -m pip install -U paddlex
```

---

## 🔍 Running OCR

**1.** Make sure the virtual environment is activated:

```powershell
.\paddle-venv\Scripts\activate
```

**2.** Place your prescription image in the project folder, for example `prescription.jpg`.

**3.** Run the script:

```powershell
python test_ocr.py
```

### 🤖 Models used (PP-OCRv5)

| Stage | Model |
|---|---|
| Text detection | `PP-OCRv5_server_det` |
| Text recognition | `PP-OCRv5_server_rec` |

> [!NOTE]
> On the first run, PaddleOCR may automatically download the required model files, which can take some time. Models are cached locally, so later runs should not download them again.

---

## 📄 OCR Output

The OCR script produces three kinds of output.

### 1. Detected text

The raw text found in the prescription image.

### 2. OCR confidence

The script calculates the average recognition confidence across all detected text regions.

```text
Average OCR Confidence: 91.25%
Text Regions: 42
```

> [!IMPORTANT]
> OCR confidence is **not** the same as actual OCR accuracy. Measuring real accuracy requires comparing the output against a manually verified ground-truth transcription.

### 3. Structured OCR text

Detected text is also arranged using the bounding-box coordinates returned by PaddleOCR. The goal is to preserve the approximate reading order and document structure of the original prescription.

---

## 🧾 Layout Testing

The project also includes a separate layout experiment:

```powershell
python test_layout.py
```

This tests **PP-DocLayout-L**, a model that detects document layout regions such as:

- 📊 Table
- 📝 Text
- 📄 Other document regions

In the current prescription test, the model detected a **large table/form region covering much of the prescription**. Because of this, layout detection is being explored separately from the main OCR pipeline for now.

---

## 🧭 Workflow at a Glance

```text
 Prescription image
        │
        ├──────────────► test_ocr.py ──► Detected text
        │                                 Confidence score
        │                                 Structured text
        │
        └──────────────► test_layout.py ─► Layout regions
```

---

<div align="center">

Made for testing and comparing OCR on medical prescriptions 💊

</div>
