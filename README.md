# Course Materials

This repository contains interactive course materials for studying mechanical vibrations and the basics of parallel programming using Python. The environment is powered by **JupyterLite**, allowing you to run simulations directly in your browser without any local installation.

## 🚀 How to Use
1. Access the interactive environment via the link provided in your course dashboard (or GitHub Pages).
2. Use the **File Browser** on the left to navigate through the modules.
3. Open any `.ipynb` file to start learning.
4. To execute a code cell, select it and press `Shift + Enter`.

---

## 📂 Course Structure

### 1_Introduction
**Focus:** Getting started with Python for engineers.
* Fundamentals of Python syntax.
* Introduction to NumPy and Matplotlib for vibration data visualization.
* **Goal:** Learn how to translate physical vibration problems into readable code.

### 2_Free_Forced_Vibration
**Focus:** Mechanical oscillations and dynamics.
* **Free Vibration:** Exploring natural frequencies and damping ratios.
* **Forced Vibration:** Investigating system responses to external harmonic forces and the phenomenon of resonance.

### 3_Parallel_Programming
**Focus:** Introduction to Parallel Computing (Message Passing Interface).
* Basic concepts of process communication (`rank`, `size`, `send/recv`).
* Syntax examples of distributed computing using the `mpi4py` library.
* **Note:** These scripts are provided as **syntax examples only**. Due to browser security sandboxing, MPI execution is not supported within the JupyterLite environment. To run these, a local MPI installation is required.

---

## 🛠 Local Setup (Optional)
If you wish to run these notebooks on your own computer:
1. Install Python 3.8+.
2. Install required libraries:
   ```bash
   pip install numpy matplotlib mpi4py
