# IDForge Dataset Documentation

## 1. Purpose

The IDForge dataset is built for **multimodal manipulation detection** and classification tasks, where models can learn from:
- **Visual data** (frames)
- **Audio data** (optional)
- **Text data** (optional)

The primary goal is to classify whether content is pristine or manipulated, and determine the type of manipulation.

---

## 2. Dataset Overview

- **Dataset Name:** IDForge (Identity-Driven Multimedia Forgery Detection Dataset)
- **Subjects:** 54 English-speaking celebrities from politics and entertainment
- **Total Shots:** 463,576
  - 249,138 shots (Training + Validation + Test)
    - 79,827 pristine
    - 169,311 forged
  - 214,438 shots (Reference Set)
- **Splits:**
  - Training: 61.83%
  - Validation: 6.95%
  - Testing: 31.22%
- **Resolution:** Minimum 1280×720 pixels
- **Clip Length:** Mostly 5-7 seconds

---

## 3. Dataset Directory Structure

```plaintext
dataset/
├── train/
│   ├── pristine/
│   ├── face_audiomismatch_textmismatch/
│   ├── face_rvc_textmismatch/
│   ├── face_tts/
│   ├── face_tts_textgen/
│   ├── lip_audiomismatch_textmismatch/
│   ├── lip_rvc_textmismatch/
│   ├── lip_tts_textgen/
│   ├── rvc_textmismatch/
│   ├── tts_textgen/
│   └── tts_textmismatch/
├── val/
│   └── (same structure as train/)
└── test/
    └── (same structure as train/)
```

Each split (`train/`, `val/`, `test/`) contains **the same manipulation types** organized consistently.

---

## 4. Data Hierarchy

Inside each manipulation type:

```plaintext
manipulation_type/
└── idXX/
    └── idXX_YY/
        └── scene_folder/
            ├── frames_ndarray.npy
            ├── *.mp3 (audio, optional)
            ├── *.txt (text, optional)
            └── frames_ndarray_sr.npy (optional, super-resolved frames)
```

- `idXX/`: Subject identity (example: `id01`, `id02`).
- `idXX_YY/`: A subfolder containing scenes for that identity.
- `scene_folder/`: Actual data for one scene.

✅ Scene folders **always contain** at least `frames_ndarray.npy` (video frames).
✅ Super-resolution frames (`frames_ndarray_sr.npy`) are optionally available.

---

## 5. File Descriptions

| File Name | Description |
|:----------|:------------|
| `frames_ndarray.npy` | A numpy array of the extracted video frames (shape: T × H × W × C) |
| `frames_ndarray_sr.npy` | Super-resolved version of frames (only in some folders) |
| `*.mp3` | Corresponding audio file |
| `*.txt` | Textual metadata |

---

## 6. Labels and Manipulation Types

Label mapping is defined as:

| Label ID | Manipulation Type |
|:--------:|:------------------|
| 0        | pristine |
| 1        | face_audiomismatch_textmismatch |
| 2        | face_rvc_textmismatch |
| 3        | face_tts |
| 4        | face_tts_textgen |
| 5        | lip_audiomismatch_textmismatch |
| 6        | lip_rvc_textmismatch |
| 7        | lip_tts_textgen |
| 8        | rvc_textmismatch |
| 9        | tts_textgen |
| 10       | tts_textmismatch |

✅ Each sample is annotated with both a **binary label** (Real/Fake) and a **multi-label vector** indicating manipulation types.

---

## 7. Splits and ID Organization

| Split | Number of IDs | Notes |
|:-----:|:-------------:|:------|
| Train | 50 IDs         | All IDs except `id00`, `id03`, `id35`, `id40` |
| Validation (Val) | 4 IDs | Only `id00`, `id03`, `id35`, `id40` |
| Test | 54 IDs | Full set: `id00`–`id53` |

✅ There is **no overlap** between train and validation IDs.  
✅ Together, **train + val IDs cover the entire test set**.

---

## 8. Metrics Printed by Code

When running `.dataset_metrics()`, the following are printed:
- Total number of samples
- Number of unique manipulation types
- Distribution of samples per manipulation type
- Number of unique IDs
- Distribution of samples per ID

Example output:

```plaintext
--- Dataset Metrics ---
Total samples: 123456
Number of unique manipulation types: 11
Manipulation types distribution:
  pristine: 12345 samples
  face_tts_textgen: 11234 samples
  ...
Number of unique IDs: 54
IDs distribution:
  id00: 456 samples
  id01: 487 samples
  ...
```

---

## 9. Special Considerations

- **File Naming:** Some folders (e.g., `lip_rvc_textmismatch`, `rvc_textmismatch`) have extra `.mp3.mp4` suffixes.
- **Super-Resolved Frames:** Available for `*_textgen` manipulation types.
- **Short Clips:** Clips shorter than 5 seconds were merged for sentence integrity.
- **Audio Clarity and Resolution:** Minimum 720p, clear speaking faces.
- **Reference Set:** 214,438 extra pristine video shots are available for identity priors.
- **Ethical Approval:** Dataset construction approved by Institutional Review Board (IRB). Complies with YouTube fair use.

---

## 10. Usage Example (PyTorch)

```python
from metrics import MultiModalDataset
from torch.utils.data import DataLoader

dataset = MultiModalDataset(
    root_dir='/arf/scratch/nerdogmus',
    split='train',
    use_super_res=False
)

dataloader = DataLoader(dataset, batch_size=4, shuffle=True, num_workers=4)

for batch in dataloader:
    frames = batch['frames']  # shape (B, T, H, W, C)
    labels = batch['label']   # shape (B,)
    break
```

---
