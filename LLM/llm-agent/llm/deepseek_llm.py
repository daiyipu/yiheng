import os
from http import HTTPStatus
from typing import Dict, Iterator, List, Optional

# from deepseek_api import DeepSeekClient  # 假设使用DeepSeek官方SDK
from qwen_agent.llm.base import ModelServiceError, register_llm
from qwen_agent.llm.function_calling import BaseFnCallModel
from qwen_agent.llm.schema import ASSISTANT, Message
from qwen_agent.log import logger
from qwen_agent.utils.utils import build_text_completion_prompt

@register_llm('deepseek-r1')  # 👈 关键注册装饰器
class DeepSeekChat(BaseFnCallModel):
    """
    DeepSeek 大模型服务封装类
    功能特性：
    - 支持流式/非流式响应
    - 兼容标准消息格式
    - 支持长上下文处理
    """

    def __init__(self, cfg: Optional[Dict] = None):
        super().__init__(cfg)
        self.model = self.model or 'deepseek-r1-250120'  # 默认模型版本
        initialize_deepseek(cfg)  # 初始化SDK配置

    def _chat_stream(
        self,
        messages: List[Message],
        delta_stream: bool,
        generate_cfg: dict,
    ) -> Iterator[List[Message]]:
        """流式对话核心逻辑"""
        messages = [msg.model_dump() for msg in messages]
        logger.debug(f'[DeepSeek] 输入参数:\n{messages}')

        # 调用DeepSeek SDK
        client = DeepSeekClient()
        response = client.chat_completions.create(
            model=self.model,
            messages=messages,
            stream=True,
            **generate_cfg
        )

        if delta_stream:
            return self._delta_stream_output(response)
        else:
            return self._full_stream_output(response)

    def _chat_no_stream(
        self,
        messages: List[Message],
        generate_cfg: dict,
    ) -> List[Message]:
        """非流式对话"""
        messages = [msg.model_dump() for msg in messages]
        logger.debug(f'[DeepSeek] 输入参数:\n{messages}')

        client = DeepSeekClient()
        response = client.chat_completions.create(
            model=self.model,
            messages=messages,
            stream=False,
            **generate_cfg
        )

        if response.status_code == HTTPStatus.OK:
            return [Message(ASSISTANT, response.choices[0].message.content)]
        else:
            raise ModelServiceError(
                code=response.code, 
                message=f'DeepSeek API错误: {response.message}'
            )

    # 保持与基类兼容的其他方法...

def initialize_deepseek(cfg: Optional[Dict] = None) -> None:
    """DeepSeek SDK初始化"""
    cfg = cfg or {}

    # 配置优先级: 显式参数 > 环境变量 > SDK默认值
    api_key = cfg.get('api_key', '') or os.getenv('DEEPSEEK_API_KEY')
    base_url = cfg.get('base_url', '') or os.getenv('DEEPSEEK_BASE_URL')
    api_version = cfg.get('api_version', 'v1')

    # 初始化客户端配置
    DeepSeekClient.configure(
        api_key=api_key.strip(),
        base_url=base_url or "https://api.deepseek.com/v1",
        api_version=api_version
    )