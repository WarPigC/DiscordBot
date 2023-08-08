import openai
def GPT(text):
    openai.api_key = "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"

    chat_completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": text}])
    for i in chat_completion:
        if i == "choices":
            for j in chat_completion[i]: # type: ignore
                return j["message"]["content"]