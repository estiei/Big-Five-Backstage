# Big-Five-Backstage

[colab-demo-image]: https://colab.research.google.com/assets/colab-badge.svg
[colab-demo-url]: https://colab.research.google.com/drive/1RZPmKsSxfSS9CaFt5wPNRGrmnzDGw8ge?usp=sharing/
[paper-url]: https://aclanthology.org/2024.cogalex-1.13.pdf

[![Colab Demo][colab-demo-image]][colab-demo-url]

Welcome to the official repo of the Big-Five Backstage (B5B) dataset -- a textual dataset comprising fictional character lines with annotations based on their gender and Big-Five personality traits. 
Along with the data, here you can find the research notebooks used in the paper "_Big-Five Backstage: A Dramatic Dataset for Fiction Character Personality Traits & Gender Analysis_" ([paper link][paper-url]).

Authors: [Marina Tiuleneva](https://www.linkedin.com/in/marina-tyuleneva/), [Vadim Porvatov](https://www.researchgate.net/profile/Vadim-Porvatov), [Carlo Strapparava](https://scholar.google.com/citations?user=VTbb1LEAAAAJ&hl=en)

# Dataset

The dataset consists of 3265 text samples corresponding to the concatenation of lines spoken by fictional characters. Texts are extracted from 400 theatre plays written by 132 different authors. Overall, it contains 3419136 words in total with a mean equal to 1047.2 words per character. Each text entry have binary labels representing gender of a character (_Male_ or _Female_) and their five personality traits (_Extraversion_, _Agreeableness_, _Openness_, _Neuroticism_, _Conscientiousness_). The auxiliary part of the dataset includes author-level labels reflecting their gender, country of origin, and years of life.

# Notebooks

We prepared [an introductory notebook][colab-demo-url] demonstrating different properties of the dataset -- feel free to use it to quickly get acquainted with Big-Five Backstage.

# License

Established data and code released as open-source under the MIT license.

# Contact us

If you have some questions about the code, you are welcome to open an issue, I will respond to that as soon as possible.

# Citation

```
@inproceedings{tiuleneva2024big,
  title={Big-Five Backstage: A Dramatic Dataset for Characters Personality Traits \& Gender Analysis},
  author={Tiuleneva, Marina and Porvatov, Vadim A and Strapparava, Carlo},
  booktitle={Proceedings of the Workshop on Cognitive Aspects of the Lexicon@ LREC-COLING 2024},
  pages={114--119},
  year={2024}
}
```
