<h1 align="center"><img src="assets/autored-logo2.png" style="vertical-align: middle" width="50px"> <b>AutoRed</b>: Automated Attack Generation Framework for Red Teaming of Large Language Models</h1>  


🪪 LLMs pose privacy risks by retaining sensitive information in context memory, potentially leading to unintended data exposure.

🛡️ Traditional red teaming is costly and slow. 

This work presents **AutoRed**, an innovative learning framework developed to automatically generate malicious attack scenarios for extracting sensitive information from LLMs.

**AutoRed** consists 

- **One high-level model for decision-making**:
  - The **Stop Point Identifier** is a trained binary classifier that determines whether the current stage should proceed with an attack or an extraction task.

- **Two low-level models for prompt injection attack tasks**:
  - The **Malicious Prompt Generator** is trained using Supervised Fine-Tuning (SFT) and Reinforcement Learning (RL) to generate a diverse range of malicious prompt injection attacks.
  - The **Sensitive Information Extractor** is a few-shot engineered GPT-3.5-turbo model designed to extract sensitive data.



## Acknowledgments

This work uses the [**RL4LMs**](https://github.com/allenai/RL4LMs) library developed by [**AllenAI**](https://allenai.org/); see the [license](https://github.com/yoyostudy/AutoRed/blob/main/LICENSE) for details.

  
