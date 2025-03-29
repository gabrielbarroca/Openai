import requests

def poser_question(question):
    url = "https://api.openai.com/v1/chat/completions"
    headers = {
        "Authorization": "Here it's suposed to be my API Key",
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
    question = input("Ask your question : ")
    answer = poser_question(question)
    print("ChatGPT :", answer)

