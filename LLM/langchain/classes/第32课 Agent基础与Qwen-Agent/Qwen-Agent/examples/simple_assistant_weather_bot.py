"""A weather forecast assistant implemented by assistant"""

import os
from qwen_agent.agents import Assistant
from qwen_agent.tools.base import BaseTool, register_tool
import json5

ROOT_RESOURCE = os.path.join(os.path.dirname(__file__), 'resource')


@register_tool('temperature_sensing')
class TemperatureSensing(BaseTool):
    # 该工具的描述，供智能体参考
    description = '表达对气温的感受，输入摄氏度气温，返回对该气温的评价。'
    # 该工具参数的描述，供智能体参考
    parameters = [{
        'name': 'temperature',
        'type': 'int',
        'description': '摄氏度气温',
        'required': True
    }]

    def call(self, params, **kwargs):
        # params是LLM根据描述生成的入参，需进一步解析
        temperature = int(json5.loads(params)['temperature'])
        if temperature < 15:
            sense = '冷'
        elif 15 < temperature < 25:
            sense = '适中'
        else:
            sense = '热'
        return sense


def init_agent_service():
    llm_cfg = {'model': 'qwen-max'}
    system = ('你扮演一个天气预报助手，你具有查询天气、表达感受和画图能力。'
              '你需要查询相应地区的天气，然后表达你对气温的直接感受，最后调用给你的画图工具绘制一张城市的图。')

    tools = ['image_gen', 'amap_weather', 'temperature_sensing']
    bot = Assistant(
        llm=llm_cfg,
        name='天气预报助手',
        description='查询天气、表达感受和画图',
        system_message=system,
        function_list=tools,
    )

    return bot


def app_tui(query="海淀区天气"):
    # Define the agent
    bot = init_agent_service()

    # Chat
    messages = []

    # Query example: 海淀区天气
    query = query

    if not query:
        print('user question cannot be empty！')
    else:
        messages.append({'role': 'user', 'content': [{'text': query}]})

    response = []
    for response in bot.run(messages):
        print('bot response:', response)
    messages.extend(response)


if __name__ == '__main__':
    # from authentications import DASHSCOPE_API_KEY, AMAP_TOKEN
    DASHSCOPE_API_KEY = os.environ.get('DASHSCOPE_API_KEY')
    AMAP_TOKEN = os.environ.get('AMAP_TOKEN')
    os.environ["DASHSCOPE_API_KEY"] = DASHSCOPE_API_KEY
    os.environ["AMAP_TOKEN"] = AMAP_TOKEN
    app_tui()
