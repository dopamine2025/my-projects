import openai
name = input("name:")
age = input("age:")
hobby = input("hobby:")
openai.api_key = "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"
response = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[
        {"role": "user", "content": "using the listed items" + name+ age + hobby + "hobby tell a story"}
    ]
)
print (response['choices'][0]['message']['content'])
