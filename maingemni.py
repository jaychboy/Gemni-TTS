"""
Install the Google AI Python SDK

$ pip install google-generativeai

See the getting started guide for more information:
https://ai.google.dev/gemini-api/docs/get-started/python
"""

import google.generativeai as genai

genai.configure(api_key="AIzaSyAkX_-nPhyYp1oIbh_WBb6q0ohuA2beGEM")

# Create the model
generation_config = {
  "max_output_tokens": 219,
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

response = chat_session.send_message("An authentic recipe for fried rice")

print("#---------------------------------------------------------------------------------------------_#")

print(response.text)