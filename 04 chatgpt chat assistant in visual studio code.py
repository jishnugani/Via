import openai

openai.api_key = ""

messages = [{"role": "system", "content": "You are an expert who can answer all questiosn about Jobs, Careers, and Industries"}]

while input != "quit()":
    message = input("Me: ")
    messages.append({"role": "user", "content": message})
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo-0125",
        messages=messages)
    reply = "Bot: " + response["choices"][0]["message"]["content"]
    messages.append({"role": "assistant", "content": reply})
    print("\n" + reply + "\n")