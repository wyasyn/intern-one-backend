# Chatbot Backend

This is a chatbot backend app.

## Initial Setup

This repo currently contains the starter files.

Clone repo and create a virtual environment

```bash
git clone https://github.com/wyasyn/chatbot-deployment.git
cd chatbot-deployment
python3 -m venv venv
source venv/bin/activate
```

Install dependencies

```bash
pip install Flask torch torchvision nltk
```

Install nltk package

```py
python
>>> import nltk
>>> nltk.download('punkt')
```

Modify `intents.json` with different intents and responses for your Chatbot

Run

```bash
python train.py
```

This will dump data.pth file. And then run
the following command to test it in the console.

```bash
python chat.py
```
