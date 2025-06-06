# Image-to-Image Generation with Stable Diffusion & Flux 1 Dev

> A local, self-hosted pipeline for advanced image-to-image transformations  
> using Stable Diffusion (AUTOMATIC1111 WebUI) and Flux 1 Dev extensions.  
> Focused on realism evaluation, texture reconstruction, and anatomy-preserving edits via LoRA models.

---

## 🧠 Project Objective

This repository is a **technical exploration of how diffusion models handle fine-grained image editing tasks**, specifically:

- Reconstructing textures (e.g., skin, fabric) under prompt control  
- Preserving facial identity and body pose consistency  
- Tuning LoRA weight blends for style fidelity

By running everything locally, we avoid cloud dependencies and gain precise control over GPU memory, sampling, and prompt/seed configurations.

---

## 🧰 Tech Stack & Tools

- **Stable Diffusion WebUI** by AUTOMATIC1111  
- **Flux 1 Dev** extension  
- Custom `.ckpt` and LoRA (`.safetensors`) model files  
- Python 3.10+, PyTorch, xformers, diffusers

> ⚙️ **Tested on:**  
> • Ubuntu 22.04 LTS  
> • NVIDIA RTX 3050 Ti (4 GB VRAM)  
> • 16 GB RAM (with 32 GB swap)  

---

## 🔍 Key Features

- ✅ Local GPU-powered inference (no cloud required)  
- ✅ Image-to-image with adjustable strength, CFG scale, denoise, and sampler  
- ✅ LoRA blending for controlled style transfers  
- ✅ Prompt weighting and seed reproducibility  
- ✅ VRAM optimization (`--medvram`, attention slicing, CPU offload)

---

## 🖼 Example Workflow

```bash
# 1. Clone this repo
git clone https://github.com/<your-username>/img2img-sd-flux-custom.git
cd img2img-sd-flux-custom

# 2. Drop custom models into ./models/
#    e.g., models/flux1-dev.safetensors, models/my-lora.safetensors

# 3. Launch AUTOMATIC1111’s WebUI (inside a virtual environment):
cd ~/stable-diffusion-webui
python launch.py --xformers --medvram --opt-sub-quad-attention

# 4. In the WebUI’s “img2img” tab:
#    • Upload ./images/input.jpg  
#    • Select your LoRA (e.g., “my-lora”) and adjust strength (0.3–0.7)  
#    • Tweak CFG (5–11), steps (50–100), sampler (Euler a, DDIM, etc.)  
#    • Click “Generate” → save to ./images/output.jpg  

# 5. Compare side-by-side (assets/before-after.png)
```

---

## 🗂 Folder Structure

```
img2img-sd-flux-custom/
├── README.md
├── .gitignore
├── requirements.txt         # (if using extra Python scripts)
├── models/
│   ├── flux1-dev.safetensors
│   └── my-lora.safetensors
├── images/
│   ├── input.jpg
│   └── output.jpg
├── config/
│   └── img2img-settings.json
├── scripts/
│   └── launch_notes.md
└── assets/
    └── before-after.png
```

---

## 💡 Applications / Skills Demonstrated

| Category                | Details                                                         |
|-------------------------|-----------------------------------------------------------------|
| 🧠 Prompt Engineering   | Prompt weighting, seed control, sampler choice, CFG tuning       |
| 🛠 VRAM Optimization     | `--medvram`, attention slicing, CPU offload                      |
| 🎨 Style Control         | LoRA blending (e.g., “my-lora.safetensors” for style fidelity)   |
| 📊 Realism Benchmarking  | Before/after comparisons, image fidelity metrics, texture checks |

---

## ⚠️ Disclaimer

> This project uses open-domain models capable of sensitive content.  
> All testing is **local** and for **technical evaluation only**.  
> No explicit or disallowed content is shared. Intended for AI development and research.

---

## 📬 Contributing / Contact

Feel free to [open an issue](https://github.com/<your-username>/img2img-sd-flux-custom/issues) or submit a pull request.  
**Author**: `<Siddharthsinghkumar>`  
**Repo:** [img2img-sd-flux-custom](https://github.com/<your-username>/img2img-sd-flux-custom)
