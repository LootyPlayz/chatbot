# chatbot.py
from transformers import pipeline

# Use distilgpt2 (smaller, faster, good for free hosting)
chatbot = pipeline("text-generation", model="distilgpt2")

def get_response(user_input: str) -> str:
    try:
        # Add "User/ Bot" format to guide GPT-2
        prompt = f"User: {user_input}\nBot:"

        result = chatbot(
            prompt,
            max_length=80,             # keep answers short
            num_return_sequences=1,
            pad_token_id=50256,        # EOS token for GPT-2
            do_sample=True,            # randomness
            top_k=50,                  # top-k sampling
            top_p=0.95,                # nucleus sampling
            temperature=0.7            # creativity control
        )

        text = result[0]["generated_text"]

        # Extract only the bot’s part
        if "Bot:" in text:
            response = text.split("Bot:")[-1].strip()
        else:
            response = text.strip()

        # Safety: avoid empty or repeated responses
        if not response:
            response = "Hmm, I’m not sure about that."
        return response

    except Exception as e:
        return f"Error: {str(e)}"
