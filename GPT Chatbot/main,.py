import openai



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