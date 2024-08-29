from openai import OpenAI

API_KEY = "sk-proj-_oVnThvt0IDK2qAna38ThOKsQKQuXVsn-rjwAzwfkSfXggNKYApbPvfMZ4T3BlbkFJ9r_aG6mYHMoxiRSuOZTCdgo-2xrRfx5aDeg3NUNNCZ3Z3oyNbpubocOAo"

client = OpenAI(api_key=API_KEY)



def chat_gpt(prompt):
    client.models.list()

    response = client.completions.create(model = "text-davinci-003",
    prompt= prompt,
    temperature=0,
    max_tokens=300,
    top_p=1.0,
    frequency_penalty=0.0,
    presence_penalty=0.0)
    return response 

