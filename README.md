# EchoScan: Smartphone Acoustic Sonar
### iQOO Hackathon 2026 — Team TRIOH

EchoScan transforms an iQOO smartphone into a portable acoustic sonar for detecting hidden structural anomalies (hollow plaster, moisture, micro-cracks). 

## 🚧 Current Status: Phase 1 (Architecture & Proof of Concept)
This repository currently contains our signal processing proof-of-concept scripts and the architecture blueprint for the upcoming 30-hour city battle. 

## 🏗️ Planned Architecture
1. **iQOO 15 (Hardware Layer):** Speaker (Acoustic Sweep) + Mic (Reflection Capture)
2. **Signal Engine:** Android `AudioTrack`/`AudioRecord` APIs + TarsosDSP for FFT feature extraction.
3. **On-Device AI:** Quantized 1D-CNN model running on the Snapdragon Hexagon NPU via TensorFlow Lite & QNN Delegate.
4. **User Output:** Jetpack Compose UI displaying a real-time Risk Heatmap.

## 🧪 Proof of Concept (Python)
We have included a Python simulation script (`/poc/signal_simulation.py`) that demonstrates our intended signal processing approach. It generates a 18kHz-22kHz linear chirp, simulates an acoustic reflection, and plots the resulting FFT spectrogram to show how hollow vs. solid states alter the frequency response.

## 👥 Team TRIOH
* **P. Nandini** (Team Lead: Product, Pitch, Integration)
* **Nuthakki Keerthi Sree** (Tech/AI: Signal pipeline, ML, UI)
* **Nomula Niharika** (Research/Test: Dataset, Validation)

*Submission for iQOO Hackathon 2026 — Smart Living Domain.*
