from openai import OpenAI
client = OpenAI(
    base_url="http://localhost:8000/v1",
    api_key="token-abc123", # 随便设，只是为了通过接口参数校验
)

completion = client.chat.completions.create(
  model="glm-4-9b-chat",
  messages=[
    {"role": "user", "content": "你好"}
  ],
  # 设置额外参数
  extra_body={
    "stop_token_ids": [151329, 151336, 151338]
  }
)

print(completion.choices[0].message)