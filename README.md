# 📝 Abstractive Text Summarization with Hugging Face Transformers

This repository demonstrates how to perform abstractive text summarization on long-form English passages using the high-level `pipeline` API from Hugging Face Transformers and PyTorch.

## 🚀 Overview

Abstractive summarization generates concise, coherent summaries by synthesizing and rephrasing key information from an input text, rather than simply extracting existing sentences verbatim. This project uses a pre-trained sequence-to-sequence transformer model optimized for text-to-text generation tasks.

## 🧠 Pipeline Configuration

- Pipeline Task: `summarization` (automatically loads default pre-trained architectures such as DistilBART or BART).
- Maximum Length (`max_length = 90`): Sets the upper token limit for the generated summary output.
- Minimum Length (`min_length = 45`): Guarantees sufficient context and depth by enforcing a minimum token threshold.
- Sampling (`do_sample = True`): Enables probabilistic decoding to generate natural and varied linguistic output.

## 🛠️ Tech Stack
- Python
- PyTorch
- Hugging Face Transformers

## 💻 Installation & Usage

1. Install dependencies:
pip install torch transformers

2. Run the summarization script:
python text_summarizer.py

## 📊 Example Demonstration

- Input Text: A paragraph detailing the evolution of artificial intelligence across healthcare, education, and finance, alongside ethical challenges such as bias and copyright.
- Generated Summary: Produces a 2-3 sentence synthesized abstract capturing both the capabilities and governance needs of modern AI systems.
