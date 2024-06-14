# Big-Five-Backstage

[colab-demo-image]: https://camo.githubusercontent.com/84f0493939e0c4de4e6dbe113251b4bfb5353e57134ffd9fcab6b8714514d4d1/68747470733a2f2f636f6c61622e72657365617263682e676f6f676c652e636f6d2f6173736574732f636f6c61622d62616467652e737667
[colab-demo-url]: https://colab.research.google.com/drive/1RZPmKsSxfSS9CaFt5wPNRGrmnzDGw8ge?usp=sharing
[paper-url]: https://colab.research.google.com/drive/1RZPmKsSxfSS9CaFt5wPNRGrmnzDGw8ge?usp=sharing

[![Colab Demo][colab-demo-image]][colab-demo-url]

Welcome to the official repo of the Big-Five Backstage (B5B) dataset -- a textual dataset comprising fictional character lines with annotations based on their gender and Big-Five personality traits. 
Along with the data, here you can find the research notebooks used in the paper "_Big-Five Backstage: A Dramatic Dataset for Fiction Character Personality Traits & Gender Analysis_" ([paper][paper-url]).

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
