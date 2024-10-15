import openai
import os

# Load your OpenAI API key from environment variable
openai.api_key = os.getenv("OPENAI_API_KEY")

# Summarize email content
def summarize_email(email_content):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": f"Summarize the following email content: {email_content}"}
        ]
    )
    return response.choices[0].message.content.strip()

# Generate email from prompt
def generate_email(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": f"Write an email based on the following prompt: {prompt}"}
        ]
    )
    return response.choices[0].message.content.strip()

# Generate multiple concise email responses to email (no lists or bullet points)
def generate_response(email_content, quick=True):
    length = "short" if quick else "long"
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": f"Generate {length}, distinct, concise email responses (1-2 sentences each) to the following email: {email_content}. Each response should be a single email-like reply, without bullet points or lists, and should be a full sentence or two."}
        ],
        n=4  # Generate four distinct responses
    )
    # Ensure responses are returned as distinct email-like responses
    return [choice.message['content'].strip() for choice in response['choices']]





# Generate an answer for a specific question about an email
def generate_answer(email_content, question):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are an expert at analyzing emails."},
            {"role": "user", "content": f"Here is the email: {email_content}. Here is the question: {question}. Answer the question based on the email content."}
        ]
    )
    return response.choices[0].message.content.strip()

# Improve email based on suggestion
def improve_email(email_content, suggestion):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": f"Improve the following email: {email_content}. Here are the suggestions: {suggestion}"}
        ]
    )
    return response.choices[0].message.content.strip()

# Regenerate email response
def regenerate_response(email_content):
    return generate_email(email_content)

# Shorten the email
def shorten_email(email_content):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": f"Shorten the following email: {email_content}"}
        ]
    )
    return response.choices[0].message.content.strip()

# Expand the email
def expand_email(email_content):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": f"Expand the following email: {email_content}"}
        ]
    )
    return response.choices[0].message.content.strip()

# Store a generated response
def store_response(response, response_chain):
    response_chain.append(response)

# Retrieve the full response chain (history of responses)
def retrieve_response_chain(response_chain):
    return response_chain

# Generate full response from a short reply
def generate_full_response_from_reply(reply):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": f"Expand this reply into a full email response: {reply}"}
        ]
    )
    return response.choices[0].message.content.strip()





