import openai


def generate_prompt(input, api_key):
    
    # Add the openai api key
    openai.api_key = api_key
    
    # Create the prompt text
    prompt_text = f"Generate a creative valentine's day greeting for {input}"
    
    # Fetch the response from the openai API
    response = openai.Completion.create(
    engine="text-davinci-001",
    prompt=prompt_text,
    temperature=0.5,
    max_tokens=40,
    top_p=1,
    best_of=3,
    frequency_penalty=0,
    presence_penalty=0
    )
    caption = response["choices"][0]["text"].strip()
    return caption