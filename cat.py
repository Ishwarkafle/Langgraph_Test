from openai import OpenAI

client = OpenAI(
    base_url="http://127.0.0.1:31415/v1",
    api_key="paste-your-unified-key-here"   # the one from the tray or Keys page
)

response = client.videos.generations.create(   # or images.generations for pictures
    model="auto",          # let FreeLLMAPI pick the best free video model
    prompt="A cute cat wearing sunglasses riding a skateboard in Tokyo at night",
    # some providers also support duration, size, etc.
)

print(response)