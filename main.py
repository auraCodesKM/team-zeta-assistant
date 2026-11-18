import os

from openai import OpenAI

client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

if __name__ == "__main__":
    q = input("Ask: ")
    print(client.chat.completions.create(model="gpt-4o-mini", messages=[{"role": "user", "content": q}])
          .choices[0].message.content)
