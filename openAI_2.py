import requests

def poser_question(question):
    url = "https://api.openai.com/v1/chat/completions"
    headers = {
        "Authorization": "Bearer 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",
        "Content-Type": "application/json"
    }
    data = {
        "model": "gpt-3.5-turbo",
        "messages": [{"role": "user", "content": question}]
    }
    response = requests.post(url, json=data, headers=headers)
    if response.status_code == 200:
        return response.json()["choices"][0]["message"]["content"]
    else:
        return f"Erreur: {response.status_code}, {response.text}"

if __name__ == "__main__":
    question = input("Pose ta question : ")
    reponse = poser_question(question)
    print("ChatGPT :", reponse)

