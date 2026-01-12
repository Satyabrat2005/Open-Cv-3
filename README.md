# Open-CV-3 

![Python](https://img.shields.io/badge/Python-3.9%2B-blue?style=for-the-badge\&logo=python)
![OpenCV](https://img.shields.io/badge/OpenCV-Computer%20Vision-green?style=for-the-badge\&logo=opencv)
![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20macOS%20%7C%20Linux-orange?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Active%20Development-brightgreen?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-purple?style=for-the-badge)

> **A curated collection of advanced computer vision projects built using OpenCV, Python, and modern CV techniques.**
> This repository serves as a growing hub for experimental, research-oriented, and real‑world computer vision applications.

---

##  Overview

**Open-CV-3** is a personal computer vision workspace where I consolidate and evolve my OpenCV-based projects. The goal of this repository is not just to demonstrate OpenCV usage, but to push toward **practical, intelligent, and interactive vision systems**.

This repo currently contains:

*  **Cursor Control using Hand Gestures**
*  **VisionIQ – A modular computer vision experimentation framework**

More projects will be continuously added as this repository grows.

---

## Repository Structure

```text
Open-CV-3/
│
├── cursor-control
|
├── visioniq/
│   ├── app/
│   ├── src/
│   ├── modes/
│   ├── README.md
│   └── Requirements.txt
|   ├── run.sh
│
├── requirements.txt
├── setup.sh
└── README.md
```

---

##  Project 1: Cursor Control using Hand Gestures

###  Description

This project implements **real-time cursor control using hand gestures**, leveraging computer vision and hand landmark detection.

The system captures live video from the webcam, detects hand landmarks, interprets gestures, and maps them to cursor actions such as:

* Cursor movement
* Left click
* Right click
* Scroll

This project demonstrates how **human–computer interaction (HCI)** can be reimagined using vision-based input systems.

###  Core Concepts Used

* OpenCV (Video capture & preprocessing)
* Hand landmark detection (MediaPipe / custom logic)
* Gesture classification
* Screen coordinate mapping
* Real-time performance optimization

###  Features

* Smooth cursor tracking
* Gesture-based clicking
* Minimal latency
* Works with standard webcams

---

##  Project 2: VisionIQ

###  Description

**VisionIQ** is a modular computer vision experimentation framework designed for rapid prototyping and testing of vision ideas.

It acts as a sandbox where multiple CV pipelines can coexist, such as:

* Object detection
* Motion tracking
* Face analysis
* Image transformations
* Feature extraction

VisionIQ focuses on **clean architecture**, **extensibility**, and **research-first development**.

###  Core Concepts Used

* OpenCV pipelines
* Modular CV architecture
* Experiment-driven design
* Performance benchmarking

###  Features

* Plug-and-play vision pipelines
* Easy experimentation
* Scalable project structure
* Research-friendly setup

---

##  Installation & Setup

###  Prerequisites

Ensure the following are installed:

* Python **3.9+**
* pip
* Webcam (for real-time projects)

---

##  Windows Setup

```bash
# Clone the repository
git clone https://github.com/your-username/Open-CV-3.git
cd Open-CV-3

# Create virtual environment
python -m venv venv
venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### Run Cursor Control

```bash
cd cursor-control
python main.py
```

### Run VisionIQ

```bash
cd visioniq
python app.py
```

---

##  macOS Setup

```bash
# Clone repository
git clone https://github.com/your-username/Open-CV-3.git
cd Open-CV-3

# Create virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### Run Cursor Control

```bash
cd cursor-control
python3 main.py
```

### Run VisionIQ

```bash
cd visioniq
python3 app.py
```

---

##  Linux (Ubuntu / Arch)

### Ubuntu

```bash
sudo apt update
sudo apt install python3 python3-venv python3-pip
```

### Arch Linux

```bash
sudo pacman -S python python-pip
```

### Setup

```bash
git clone https://github.com/your-username/Open-CV-3.git
cd Open-CV-3
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### Run Projects

```bash
cd cursor-control
python3 main.py

# or
cd visioniq
python3 app.py
```

---

##  Future Roadmap

*  Multi-hand gesture recognition
*  AI-based gesture learning
*  Depth-based vision support
*  GPU acceleration
*  Plugin system for VisionIQ
*  Benchmarking & metrics dashboard

---

##  Philosophy

> *Computer vision should not be locked behind theory alone.*
> *It should be interactive, experimental, and grounded in real-world use cases.*

Open-CV-3 is built with this mindset — learning by building, testing by experimenting.

---

##  Contributions

Contributions, discussions, and collaborations are welcome.

If you’re interested in:

* Computer vision
* Human–computer interaction
* OpenCV research
* Experimental AI systems

Feel free to open an issue or reach out.

---

##  License

This project is released under the **MIT License**.

---



If you find this repository useful or interesting, consider giving it a ⭐.
More advanced computer vision projects are on the way.

**Built with curiosity, code, and computer vision.** 👁️✨
