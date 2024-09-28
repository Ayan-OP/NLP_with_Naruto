# NLP_with_Naruto: Unveiling the Hidden Depths of the Naruto Universe through Natural Language Processing

![Dashboard](https://github.com/Ayan-OP/NLP_with_Naruto/blob/main/screencapture-89a535c08314fba257-gradio-live-2024-09-05-10_19_42.png)

Embark on an exciting journey through the world of Naruto, empowered by the capabilities of Natural Language Processing (NLP). This project harnesses various NLP techniques to analyze and interact with the beloved anime series, offering a deeper understanding of its themes, characters, and even allowing you to converse with Naruto himself.

## Key Features

### 1. Jutsu Classification: Deciphering the Techniques

* **Unraveling the Jutsu Tapestry:**  Naruto's world is teeming with a vast array of jutsu (techniques), each with its own unique properties and strategic applications. This project tackles the challenge of automatically classifying these jutsu into their distinct types: 
    * **Genjutsu:** Illusions that deceive and manipulate the senses.
    * **Ninjutsu:** Techniques utilizing chakra manipulation and elemental transformations.
    * **Taijutsu:** Hand-to-hand combat techniques honed through rigorous training and physical prowess.
* **DistilBERT at the Helm:** A fine-tuned DistilBERT model, trained on carefully curated jutsu descriptions, lies at the heart of this classification system. It intelligently analyzes textual nuances to accurately categorize each jutsu, providing valuable insights into their nature and combat potential.

### 2. Theme Exploration: Unmasking the Narrative Tapestry

* **Beyond the Surface:**  Delve deeper into the narrative fabric of Naruto, beyond the thrilling battles and captivating characters. This project aims to identify and visualize the prominent themes that shape the series, revealing the underlying messages and emotional core that resonate with fans worldwide.
* **Zero-Shot Classification Prowess:** A zero-shot classification pipeline, powered by the versatile BART model, enables theme extraction even without explicit training on Naruto-specific data. This demonstrates the adaptability and potential of NLP to uncover hidden meanings within any narrative.

### 3. Character Network Analysis: Unveiling the Bonds

* **The Ninja Social Web:** Within the vast cast of characters in Naruto, a complex web of relationships and interactions exists. This project utilizes Named Entity Recognition (NER) to identify characters mentioned in episode scripts and then constructs an interactive network graph to visualize these connections.
* **From Allies to Rivals:**  Explore the intricate bonds of friendship, loyalty, rivalry, and even love that shape the characters' journeys. Witness the evolution of these relationships as the story unfolds, gaining a deeper appreciation for the social dynamics within the Naruto universe.

### 4. Character Chatbot: A Conversation with Naruto Uzumaki

* **Step into the Ninja World:**  Experience the thrill of conversing with Naruto Uzumaki himself through an interactive chatbot. This innovative feature brings the iconic protagonist to life, allowing fans to engage in dynamic conversations and explore his thoughts, feelings, and motivations.
* **Powered by Llama:** A fine-tuned Llama language model, trained on extensive dialogues from the Naruto series, ensures that the chatbot captures Naruto's distinctive personality, humor, and unwavering determination. From discussing his dreams of becoming Hokage to sharing his insights on the ninja way, the chatbot offers a unique and immersive experience for fans of all ages.


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
