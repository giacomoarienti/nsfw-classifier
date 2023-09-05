# nsfw-classifier
NSFW Classifier using [google/vit-base-patch16-224-in21k](https://huggingface.co/google/vit-base-patch16-224-in21k)

## Installation
```bash
python3 -m venv .venv
source .venv/bin/activate

python3 -m pip install -r requirements.txt
```

## Run Chat Interface
`chainlit run chat/app.py`

## Run API
`python3 app.py`

## Pre-Trained Model
[giacomoarienti/nsfw-classifier](https://huggingface.co/giacomoarienti/nsfw-classifier)

## Dataset
[deepghs/nsfw_detect](https://huggingface.co/datasets/deepghs/nsfw_detect)