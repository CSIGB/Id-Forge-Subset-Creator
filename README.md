# Dataset Overview

This dataset is designed for multimodal manipulation detection tasks, containing synchronized **frames**, **audio**, and **text** data.  
It is structured into **training**, **validation**, and **test** splits, organized by manipulation type and subject IDs.

---

## 📁 Directory Structure

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

- Each **manipulation type** folder contains **subject ID folders** (e.g., `id00/`, `id01/`, etc.).
- Each **subject ID folder** contains **scene folders**.
- Each **scene folder** contains synchronized frames, audio, and text data.

---

## 📂 Inside Each Scene Folder

Each scene folder (e.g., `id01_scene_0005_1_infoswap.mp4/`) includes:

| File | Description |
|:-----|:------------|
| `frames_ndarray.npy` | Numpy array containing extracted video frames |
| `*.mp3` | Audio file extracted from the scene |
| `*.txt` | Text transcript or related text data |
| *(optional)* `frames_ndarray_sr.npy` | Super-resolved frames (only in some `*_textgen` folders) |

👉 **frames_ndarray.npy** is always present.  
👉 **frames_ndarray_sr.npy** appears only in **textgen manipulation types**.

---

## 📊 Dataset Splits and Metrics

| Split   | # of Subject IDs | Description |
|:--------|:----------------:|:------------|
| Train   | 50                | IDs: `id01`, `id02`, ..., `id53` (excluding `id00`, `id03`, `id35`, `id40`) |
| Validation (Val) | 4         | IDs: `id00`, `id03`, `id35`, `id40` |
| Test    | 54                | All IDs from `id00` to `id53` |

**Important properties:**
- **Train IDs** and **Validation IDs** are disjoint (no overlap).
- **Train + Validation IDs** together cover the full set of **Test IDs**.

---

## 📜 Manipulation Types (Classes)

Each manipulation type acts as a separate **class label**.

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

---

## ⚡ Special Notes and Considerations

- **File Naming Differences:**  
  Some folders (e.g., `lip_rvc_textmismatch`, `rvc_textmismatch`) have unusual file names containing extra `.mp3` segments, such as `id01_scene_0012.mp3.mp4/`.  
  This does **not affect** the inner files' availability.

- **Super-Resolved Frames:**  
  Folders under `*_textgen` manipulations contain an additional `frames_ndarray_sr.npy`, which can optionally be used for higher-quality visual inputs.

- **Scene Folder Naming:**  
  The naming of scene folders slightly differs depending on manipulation type (`idXX_scene_XXXX.mp4/`, `idXX-YY_fake.mp4/`, etc.), but the **internal structure is consistent**.

---

## 📋 Summary

> This dataset provides synchronized **visual (frames)**, **audio**, and **text** data per manipulated or pristine sample.  
It is structured carefully across training, validation, and test sets with clean ID separation and consistent multimodal inputs.
```
