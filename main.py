"""

See the getting started guide for more information:
https://ai.google.dev/gemini-api/docs/get-started/python

"""


import requests
import google.generativeai as genai

genai.configure(api_key="")

# Create the model
generation_config = {
  "max_output_tokens": 512,
  "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
  model_name="gemini-1.5-flash",
  generation_config=generation_config,
  # safety_settings = Adjust safety settings
  # See https://ai.google.dev/gemini-api/docs/safety-settings
)

chat_session = model.start_chat(
  history=[
  ]
)

response = chat_session.send_message("")

#print("#---------------------------------------------------------------------------------------------_#")
#print(response.text)

#Elevenlabs area

CHUNK_SIZE = 256

url = "https://api.elevenlabs.io/v1/text-to-speech/"

headers = {
  "Accept": "audio/mpeg",
  "Content-Type": "application/json",
  "xi-api-key": ""
}

data = {
    
  "text": response.text,

  "model_id": "eleven_multilingual_v2",
}

response = requests.post(url, json=data, headers=headers)
with open('bread_recipe.mp3', 'wb') as f:
    for chunk in response.iter_content(chunk_size=CHUNK_SIZE):
        if chunk:
            f.write(chunk)
