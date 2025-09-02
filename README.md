# 🎛️ Protocol-Based Computing
### Frequency-Domain Logic Encoding for Protocol-Enforced Systems

![Sheen Banner](https://raw.githubusercontent.com/74Thirsty/74Thirsty/main/assets/rainbow.svg)

[![Made with Python](https://img.shields.io/badge/Python-3.11+-blue?logo=python&logoColor=white)](https://www.python.org/)  
[![LaTeX](https://img.shields.io/badge/LaTeX-pdfTeX-green?logo=latex&logoColor=white)](https://www.latex-project.org/)  
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](./LICENSE)  
[![ArXiv](https://img.shields.io/badge/arXiv-pending-red)](https://arxiv.org/)  

---

# Protocol-Based Computing: Frequency-Domain Logic Encoding

This repository accompanies the whitepaper **“Frequency-Domain Logic Encoding for Protocol-Enforced Systems”** by Christopher Hirschauer (August 30, 2025).

The project explores an alternative to binary computing: replacing 0/1 voltage levels with **frequency-domain logic** to achieve multi-valued encoding, semantic density, and protocol-enforced control.

---

## 📄 Whitepaper

* **PDF:** [`protocol_based_computing_whitepaper.pdf`](./protocol_based_computing_whitepaper.pdf)
* **Source (LaTeX):** [`protocol_based_computing_whitepaper.tex`](./protocol_based_computing_whitepaper.tex)
* **References:** [`references.bib`](./references.bib)

---

## 📊 Figures

All figures are generated using Python and `matplotlib`.

* `waveform_zoom.png` → Zoomed view of a chirp (1–16 kHz, first 5 ms)
* `multitone_packet.png` → Multi-tone symbol packet spectrogram (discrete logic states)
* `frequency_encoded_signal.png` → Full chirp from 1 kHz to 16 kHz

To regenerate the figures:

```bash
python3 make_figures.py
```

---

## 🧩 Core Idea

* **Binary Logic**: 2 frequencies → 1 bit per pulse
* **Hex Logic**: 16 frequencies → 4 bits per pulse
* **General Model**: 2ⁿ frequencies → n bits per pulse

**Key tradeoff:**

* More semantic information per signal.
* Slightly slower execution due to frequency discrimination latency.

**Applications:**

* Plugin rollback / override enforcement
* AI directive validation
* Forensic signal-level logging

---

## ⚙️ Implementation Pathways

* **Software** → Python simulations (chirps, spectrograms).
* **Hardware** → FPGA/DSP frequency discriminators, oscillator banks, ADCs.

---

## 🚀 Quick Start

1. Clone the repo:

   ```bash
   git clone https://github.com/<your-username>/<repo-name>.git
   cd <repo-name>
   ```
2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```
3. Generate figures:

   ```bash
   python3 make_figures.py
   ```
4. Open the PDF whitepaper for the full write-up.

To regenerate:  
```
python3 make_figures.py
```

## 🚀 Quick Start

```
git clone https://github.com/<your-username>/<repo-name>.git
cd <repo-name>
pip install -r requirements.txt
python3 make_figures.py
```

Then open `protocol_based_computing_whitepaper.pdf` for the full write-up.

---

## 🛠 Applications

* Plugin rollback / override enforcement
* AI instruction validation
* Forensic signal-level audit trails

---

## 📬 Contact

**Author:** Christopher Hirschauer
📧 [c.hirschauer@outlook.com](mailto:c.hirschauer@outlook.com)

This version gives you:  
- ASCII gradient-style banner  
- Shields for Python, LaTeX, license, and future arXiv link  
- Polished layout with emojis for quick scanning  
