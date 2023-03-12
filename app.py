import openai
import os

openai.api_key = os.environ["OPENAI_API_KEY"]


def ask(question):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
                {"role": "user", "content": f'{question}'}
            ]
    )
    answer = response['choices'][0]['message']['content']
    return answer


if __name__ == "__main__":
    question = input("質問を入力してください。:")
    answer = ask(question)
    print(answer)
