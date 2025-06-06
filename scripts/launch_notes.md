# Launch Notes for Stable Diffusion WebUI

Use the following commands to optimize memory usage and performance:

```bash
python launch.py --xformers --medvram --opt-sub-quad-attention
```
- `--xformers`: Enables memory-efficient attention using xformers.

- `--medvram`: Reduces VRAM usage by slicing large tensors.

- `--opt-sub-quad-attention`: Optimizes sub-quadratic attention.


For systems with limited VRAM (e.g., 4GB), consider:

- `--no-half-vae`: If VAE half-precision causes issues.

- Reducing image resolution (e.g., 256x256 instead of 512x512).

- Using `img2img` strength < 0.8 to speed up inference.

