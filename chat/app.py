from transformers import pipeline
import chainlit as cl
from PIL import Image
import io

pipe = pipeline("image-classification", model="giacomoarienti/nsfw-classifier")


@cl.on_chat_start
async def start():
    files = None

    # Wait for the user to upload a file
    while files == None:
        files = await cl.AskFileMessage(
            content="Please upload an image file to begin!", accept=["image/*"]
        ).send()

    # Decode the file
    file = files[0]
    image = Image.open(io.BytesIO(file.content))

    # Let the user know that the system is ready
    elements = [
        cl.Image(name=file.name, content=file.content, display="inline"),
    ]
    await cl.Message(
        content=f"`{file.name}` uploaded!",
        elements=elements,
    ).send()

    response = pipe(image)
    await cl.Message(
        content=f"**Prediction:** {response[0]['label']}\n**Confidence:** {response[0]['score']}"
    ).send()
