"""
Ollama Controller - HTTP API 实现
支持通过 HTTP API 与 Ollama 交互
"""

import asyncio
import json
import sys
import aiohttp
from typing import Optional, Dict, Any, List, AsyncIterator


class OllamaController:
    """Ollama HTTP API 控制器"""

    def __init__(
        self,
        base_url: str = "http://localhost:11434",
        model: str = "qwen2.5:7b",
        auto_clear: bool = False
    ):
        """
        初始化 Ollama 控制器

        Args:
            base_url: Ollama API 地址
            model: 默认使用的模型
            auto_clear: 是否自动清理对话历史
        """
        self.base_url = base_url.rstrip("/")
        self.model = model
        self.auto_clear = auto_clear
        self.conversation_history: List[Dict[str, str]] = []
        self.session: Optional[aiohttp.ClientSession] = None

    async def __aenter__(self):
        """异步上下文管理器入口"""
        await self.connect()
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        """异步上下文管理器出口"""
        await self.close()

    async def connect(self) -> bool:
        """
        连接到 Ollama 服务

        Returns:
            连接是否成功
        """
