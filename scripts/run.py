# run.py
from diffusers import AutoPipelineForText2Image
import torch

def generate_image(prompt):
    model_path = "/home/sidd/flux/FLUX.1-dev"
    # Load the pipeline using FP16 precision and the "balanced" device map.
    pipeline = AutoPipelineForText2Image.from_pretrained(
        model_path,
        torch_dtype=torch.float16,
        device_map="balanced",    # Distributes model layers between GPU and CPU
        local_files_only=True
    )
    
    # Enable memory-saving techniques:
    pipeline.enable_attention_slicing()                   # Process attention in smaller chunks
    pipeline.enable_xformers_memory_efficient_attention()   # Use xformers for efficient attention (if supported)
    pipeline.enable_model_cpu_offload()                     # Offload model layers to CPU when idle

    # Generate an image at lower resolution to reduce memory usage.
    image = pipeline(prompt, height=128, width=128).images[0]
    image.show()

if __name__ == "__main__":
    prompt = "change cloths"
    generate_image(prompt)
