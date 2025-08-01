# 🌙 Dream Visualizer

**Dream Visualizer** is a Gradio-based AI application that transforms free-text dream descriptions into imaginative visual scenes. It works by converting your dream into a visual prompt and then generating an image using a hosted text-to-image model API.

---

## What is this?

Have you ever wished to see your dreams come to life? This app takes your dream text, interprets it into a detailed visual prompt, and uses AI to generate stunning images that capture the mood and symbolism of your dreams.

Behind the scenes, it combines prompt engineering with powerful AI image generation models, all wrapped in a smooth and interactive web interface built with Gradio.

---

## 🚀 How I Built It

This project started from a simple idea — what if we could *see* our dreams?

1. **Initial Approach**  
   I began with symbolic interpretation, trying to analyze dreams by mapping them to symbols and meanings. However, the results were inconsistent and hard to visualize.

2. **Simplified and Improved**  
   I pivoted to a direct visual storytelling approach: turning dream text into scene descriptions using keyword matching and fantasy-style prompts. This produced better and more reliable results.

3. **Image Generation**  
   After experimenting with local and cloud-hosted models, I used Hugging Face’s `stabilityai/stable-diffusion-2` as the default model. The model works best on GPU and supports Ghibli-style rendering.

4. **UI:** Built using Gradio for quick iterations and user-friendly interaction.

This project is a blend of creativity, prompt engineering, and AI technology.

---

## Features

- ✍️ Enter any dream description and get a unique image  
- 🎨 Images have a beautiful, soft fantasy art vibe inspired by Studio Ghibli  
- 🖼️ View recent dream prompts and images in the session  
- 🎲 Use example dreams to test instantly  
- 🚀 Fast generation with GPU acceleration
- 🌐 Deployed as a Gradio web app

---

## 🛠 Tech Stack

- Python 🐍
- Gradio UI 🎨
- Hugging Face Spaces 🚀
- PIL (Pillow) for image handling
- Tempfile for downloads
- Stable Diffusion 2 (via Hugging Face Inference API)

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
[https://huggingface.co/spaces/sree-02/dream-visualizer](https://huggingface.co/spaces/your-username/dream-visualizer)
⚠️ **Note:** The Hugging Face app may not work as expected on CPU-only hardware. For the best experience, run the app with a GPU (e.g., T4) or clone and run locally with GPU enabled (e.g., Google Colab).


---

## Future plans

- Fix image download issues in the web version
- Add better prompt engineering and support more artistic styles
- Improve performance on CPU or deploy with GPU on Hugging Face
- Add model selection or customization options for users
- Mobile-friendly UI

---

## License

This project is open-source under the **MIT License**. Feel free to explore, modify, and share!

---

Thanks for checking out Dream Visualizer! I’d love to hear your feedback and ideas.

Happy dreaming! 🌠
