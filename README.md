# 🌙 Dream Visualizer

Welcome to **Dream Visualizer** — a creative app that transforms your dream descriptions into beautiful, surreal images inspired by Studio Ghibli’s magical art style.

---

## What is this?

Have you ever wished to see your dreams come to life? This app takes your dream text, interprets it into a detailed visual prompt, and uses AI to generate stunning images that capture the mood and symbolism of your dreams.

Behind the scenes, it combines prompt engineering with powerful AI image generation models, all wrapped in a smooth and interactive web interface built with Gradio.

---

## How this project came to be

I started this project inspired by my fascination with dreams and AI art. The goal was to create a tool that turns abstract dream stories into vivid visuals. 

The core components include:

- **Dream-to-visual prompt conversion:** A custom function that extracts key themes from your dream text and crafts detailed image prompts.
- **Image generation model:** Initially tested with OpenAI’s models, but currently runs best with GPU-accelerated Hugging Face Diffusers models (like Stable Diffusion).
- **UI:** Built using Gradio for quick iterations and user-friendly interaction.

This project is a blend of creativity, prompt engineering, and AI technology.

---

## Features

- ✍️ Enter any dream description and get a unique image  
- 🎨 Images have a beautiful, soft fantasy art vibe inspired by Studio Ghibli  
- 🖼️ View recent dream prompts and images in the session  
- 🎲 Use example dreams to test instantly  
- 🚀 Fast generation with GPU acceleration

---

## Current Limitations & Notes

- **Image download functionality is a work-in-progress** — I’m actively working on making image downloads seamless and reliable.
- The image generation works best with **GPU-enabled environments** due to the computational load of AI models.
- While the app was initially tested on OpenAI models, it now primarily uses Hugging Face's open-source models for cost and flexibility reasons.

---

## Running locally

1. Clone this repo  
2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Run the app:

   ```bash
   python app.py
   ```

4. Open the local URL in your browser and start dreaming!

---

## Live Demo

Try it online at:  
[https://huggingface.co/spaces/your-username/dream-visualizer](https://huggingface.co/spaces/your-username/dream-visualizer)

*(Replace `your-username` with your actual Hugging Face username)*

---

## Future plans

- Fix and polish the image download feature  
- Add more artistic styles and themes  
- Enhance prompt understanding and image quality  
- Add user accounts and dream history saving  
- Mobile-friendly UI

---

## License

This project is open-source under the **MIT License**. Feel free to explore, modify, and share!

---

Thanks for checking out Dream Visualizer! I’d love to hear your feedback and ideas.

Happy dreaming! 🌠
