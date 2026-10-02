from transformers import pipeline

# ozetleme pipeline yukle
summarizer = pipeline("summarization")

text = """
Artificial intelligence (AI) has rapidly transformed modern society, driving breakthroughs across healthcare, education, finance, and transportation. By leveraging machine learning algorithms and vast datasets, AI systems can diagnose diseases with high precision, personalize student learning experiences, detect fraudulent financial transactions, and optimize complex supply chains. In recent years, generative models and large language architectures have expanded these capabilities further, allowing computers to generate human-like text, create realistic imagery, and assist in computer programming. However, this swift technological progression also raises significant ethical and practical dilemmas. Issues such as algorithmic bias, data privacy vulnerabilities, copyright infringement, and workforce displacement have sparked global debates. To ensure that artificial intelligence remains beneficial to humanity, researchers, governments, and industry leaders are actively collaborating on regulatory frameworks, ethical standards, and robust validation benchmarks designed to make systems transparent, fair, and accountable.
"""

summary = summarizer(
    text,
    max_length = 90,
    min_length = 45,
    do_sample = True
    )

print(summary[0]["summary_text"])