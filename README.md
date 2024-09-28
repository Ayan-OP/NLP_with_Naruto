# NLP_with_Naruto: Unveiling the Hidden Depths of the Naruto Universe through Natural Language Processing

[![Project Image 1]](path/to/image1.png)
[![Project Image 2]](path/to/image2.png)
[![Project Image 3]](path/to/image3.png)

Embark on an exciting journey through the world of Naruto, empowered by the capabilities of Natural Language Processing (NLP). This project harnesses various NLP techniques to analyze and interact with the beloved anime series, offering a deeper understanding of its themes, characters, and even allowing you to converse with Naruto himself.

## Key Features

### 1. Jutsu Classification

* **Unravel the Secrets of Jutsu:** Accurately classify Naruto's diverse array of jutsu (techniques) into their respective types: Genjutsu (illusion techniques), Ninjutsu (ninja techniques), and Taijutsu (hand-to-hand combat techniques).
* **Powered by DistilBERT:**  Leverages a fine-tuned DistilBERT model to analyze jutsu descriptions and make precise classifications, aiding in comprehending their nature and strategic applications.

### 2. Theme Exploration

* **Uncover the Heart of the Story:** Identify and visualize the prominent themes that weave through the Naruto series, from friendship and determination to the complexities of power and sacrifice.
* **Zero-Shot Classification:** Employs a zero-shot classification pipeline with a BART model to extract themes from episode scripts, even without explicit training on Naruto-specific data.

### 3. Character Network Analysis

* **Map the Web of Relationships:** Extract character names from episode scripts using Named Entity Recognition (NER) with spaCy.
* **Visualize Interactions:** Construct an interactive network graph that reveals the intricate relationships and connections between characters, shedding light on their social dynamics and alliances.

### 4. Character Chatbot: Converse with Naruto!

* **Bring Naruto to Life:** Engage in dynamic conversations with a virtual Naruto, powered by a fine-tuned Llama language model.
* **Authentic Personality and Speech:** Experience Naruto's distinctive personality, humor, and speech patterns as you chat with him about his adventures, dreams, and the ninja way.

## Project Structure

* `crawler`: Fetches jutsu data from the Naruto Fandom wiki using Scrapy.
* `theme_classifier`:  Performs theme identification and visualization from episode scripts.
* `character_network`:  Extracts character names and generates the interactive network graph.
* `character_chatbot`:  Trains and interacts with the Naruto chatbot.
* `text_classification`:  Houses the core components for jutsu classification.
* `utils`:  Provides utility functions, including subtitle data loading.
* `gradio_app.py`:  The main Gradio application for the user interface.
* `stubs`:  Stores intermediate output files for efficiency.
* `.env`:  Securely stores the Hugging Face token.
* `data`:  Contains the subtitles, conversation transcripts, and extracted jutsu data.

## Getting Started

1. Clone the repository.
2. Install dependencies using `pip install -r requirements.txt`.
3. Set up your Hugging Face token in the `.env` file.
4. Run `python gradio_app.py` to launch the interactive interface.

## Usage

- Access the Gradio interface via the provided link.
- Explore each section:
    - **Theme Classification:** Input themes and a path to subtitles/scripts.
    - **Character Network:** Provide a path to subtitles/scripts and NER output.
    - **Jutsu Classification:** Input text describing a jutsu.
    - **Character Chatbot:** Start chatting with Naruto!

## Contributing

I welcome contributions! Feel free to open issues or submit pull requests.

## License

This project is licensed under the MIT License.

## Acknowledgments

- Naruto and all related characters and concepts belong to Masashi Kishimoto.
- This project is a tribute to the Naruto series and a demonstration of the power of NLP.

Let's dive deeper into the world of Naruto with the help of NLP!
