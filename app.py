
import gradio as gr
import os
import tempfile
from PIL import Image
from io import BytesIO

# Your functions from previous cells
def dream_to_visual_scene_prompt(dream_text):
    visual_keywords = {
        "forest": "dense forest",
        "lion": "fierce lion",
        "running": "person running",
        "chased": "being chased",
        "falling": "person falling",
        "ocean": "stormy ocean",
        "city": "burning city",
        "shadows": "dark ghostly figures",
        "fire": "blazing fire",
        "sky": "dramatic sky",
        "flying": "person flying above clouds",
    }
    scene_parts = []
    for keyword, visual in visual_keywords.items():
        if keyword in dream_text.lower():
            scene_parts.append(visual)
    style = "Studio Ghibli style, highly detailed, fantasy art, cinematic lighting, trending on ArtStation, 4K resolution"
    if scene_parts:
        scene_description = ", ".join(scene_parts)
    else:
        scene_description = dream_text  # fallback
    return f"{scene_description}. {style}"

def generate_image_from_prompt(prompt):
    from diffusers import StableDiffusionPipeline
    import torch
    pipe = StableDiffusionPipeline.from_pretrained(
        "runwayml/stable-diffusion-v1-5",
        torch_dtype=torch.float16,
        revision="fp16"
    ).to("cuda")
    image = pipe(prompt).images[0]
    return image

# Session-level dream history
dream_history = []

def dream_to_image_simple(dream_text):
    try:
        final_prompt = dream_to_visual_scene_prompt(dream_text)
        image = generate_image_from_prompt(final_prompt)
        dream_history.append((dream_text, final_prompt, image))
        return final_prompt, image
    except Exception as e:
        return f"Error: {str(e)}", None

def get_example():
    return "I was flying over a burning city, chased by shadows, then I fell into the ocean."

def get_history_text():
    if not dream_history:
        return "No dreams generated yet."
    text = ""
    for i, (dream, prompt, _) in enumerate(dream_history[-5:], 1):
        text += f"{i}. Dream: {dream}\n   Prompt: {prompt}\n\n"
    return text.strip()

def download_last_image():
    if not dream_history:
        return None
    img = dream_history[-1][2]
    tmp_file = tempfile.NamedTemporaryFile(delete=False, suffix=".png")
    img.save(tmp_file.name)
    tmp_file.close()
    return tmp_file.name

with gr.Blocks() as demo:
    gr.Markdown("# 🌙 Dream Visualizer")
    gr.Markdown("Describe your dream and see it turned into a surreal image.")

    with gr.Row():
        dream_input = gr.Textbox(lines=4, label="Describe Your Dream")
        with gr.Column():
            example_btn = gr.Button("🎲 Use Example Dream")
            generate_btn = gr.Button("Generate Image 🚀")
            download_btn = gr.Button("⬇️ Download Image")
            download_btn.visible = False

    prompt_output = gr.Textbox(label="🎨 Visual Prompt")
    image_output = gr.Image(type="pil", label="🖼 Generated Dream Image")
    history_output = gr.Textbox(label="📜 Recent Dreams & Prompts", lines=6, interactive=False)

    example_btn.click(fn=get_example, inputs=None, outputs=dream_input)
    generate_btn.click(fn=dream_to_image_simple, inputs=dream_input, outputs=[prompt_output, image_output])
    generate_btn.click(fn=lambda: gr.update(visible=True), inputs=None, outputs=download_btn)
    generate_btn.click(fn=get_history_text, inputs=None, outputs=history_output)
    download_btn.click(fn=download_last_image, inputs=None, outputs=gr.File(label="Download Your Image"))

demo.launch()
