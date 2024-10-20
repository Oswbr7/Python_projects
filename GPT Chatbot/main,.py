import openai

openai.api_key = "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"

def chat(prompt):
    response = openai.chat.completions.create(
        model = "gpt-3.5-turbo",
        messages = [{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content.strip()

if __name__ == "__main__":
    while True:
        U_input = input("You: ")
        if U_input.lower() in ["quit", "exit", "bye"]:
            break

        response = chat(U_input)
        print("Chatbot: ", response)