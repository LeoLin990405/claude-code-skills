#!/usr/bin/env python3
"""
Ollama 操作控制器
通过 HTTP API 与 Ollama 交互
"""

import asyncio
import json
import sys
from pathlib import Path
from typing import Optional, List, Dict, Any
import aiohttp


class OllamaController:
    """Ollama HTTP API 控制器"""

    def __init__(self, base_url: str = "http://localhost:11434"):
        """
        初始化 Ollama 控制器

        Args:
            base_url: Ollama API 基础 URL
        """
        self.base_url = base_url
        self.session: Optional[aiohttp.ClientSession] = None

    async def connect(self):
        """建立连接"""
        self.session = aiohttp.ClientSession()
        # 测试连接
        try:
            async with self.session.get(f"{self.base_url}/api/tags") as resp:
                if resp.status == 200:
                    print(f"✓ 已连接到 Ollama: {self.base_url}")
                else:
                    print(f"✗ 连接失败: HTTP {resp.status}")
        except Exception as e:
            print(f"✗ 连接失败: {e}")

    async def close(self):
        """关闭连接"""
        if self.session:
            await self.session.close()

    # ==================== 模型管理 ====================

    async def list_models(self) -> Dict[str, Any]:
        """
        列出所有可用模型

        Returns:
            模型列表
        """
        try:
            async with self.session.get(f"{self.base_url}/api/tags") as resp:
                if resp.status == 200:
                    data = await resp.json()
                    return {
                        "success": True,
                        "models": data.get("models", [])
                    }
                else:
                    return {
                        "success": False,
                        "error": f"HTTP {resp.status}"
                    }
        except Exception as e:
            return {
                "success": False,
                "error": str(e)
            }

    async def show_model(self, model_name: str) -> Dict[str, Any]:
        """
        显示模型详细信息

        Args:
            model_name: 模型名称

        Returns:
            模型信息
        """
        try:
            async with self.session.post(
                f"{self.base_url}/api/show",
                json={"name": model_name}
            ) as resp:
                if resp.status == 200:
                    data = await resp.json()
                    return {
                        "success": True,
                        "model": data
                    }
                else:
                    return {
                        "success": False,
                        "error": f"HTTP {resp.status}"
                    }
        except Exception as e:
            return {
                "success": False,
                "error": str(e)
            }

    async def pull_model(self, model_name: str) -> Dict[str, Any]:
        """
        拉取模型

        Args:
            model_name: 模型名称

        Returns:
            操作结果
        """
        try:
            async with self.session.post(
                f"{self.base_url}/api/pull",
                json={"name": model_name}
            ) as resp:
                if resp.status == 200:
                    # 流式响应，读取所有进度
                    async for line in resp.content:
                        if line:
                            progress = json.loads(line)
                            if "status" in progress:
                                print(f"  {progress['status']}")
                    return {
                        "success": True,
                        "message": f"模型 {model_name} 拉取完成"
                    }
                else:
                    return {
                        "success": False,
                        "error": f"HTTP {resp.status}"
                    }
        except Exception as e:
            return {
                "success": False,
                "error": str(e)
            }

    async def delete_model(self, model_name: str) -> Dict[str, Any]:
        """
        删除模型

        Args:
            model_name: 模型名称

        Returns:
            操作结果
        """
        try:
            async with self.session.delete(
                f"{self.base_url}/api/delete",
                json={"name": model_name}
            ) as resp:
                if resp.status == 200:
                    return {
                        "success": True,
                        "message": f"模型 {model_name} 已删除"
                    }
                else:
                    return {
                        "success": False,
                        "error": f"HTTP {resp.status}"
                    }
        except Exception as e:
            return {
                "success": False,
                "error": str(e)
            }

    # ==================== 对话功能 ====================

    async def generate(self, model: str, prompt: str, stream: bool = False) -> Dict[str, Any]:
        """
        生成响应

        Args:
            model: 模型名称
            prompt: 提示词
            stream: 是否流式输出

        Returns:
            生成结果
        """
        try:
            async with self.session.post(
                f"{self.base_url}/api/generate",
                json={
                    "model": model,
                    "prompt": prompt,
                    "stream": stream
                }
            ) as resp:
                if resp.status == 200:
                    if stream:
                        # 流式输出
                        full_response = ""
                        async for line in resp.content:
                            if line:
                                chunk = json.loads(line)
                                if "response" in chunk:
                                    print(chunk["response"], end="", flush=True)
                                    full_response += chunk["response"]
                        print()  # 换行
                        return {
                            "success": True,
                            "response": full_response
                        }
                    else:
                        # 非流式输出
                        data = await resp.json()
                        return {
                            "success": True,
                            "response": data.get("response", "")
                        }
                else:
                    return {
                        "success": False,
                        "error": f"HTTP {resp.status}"
                    }
        except Exception as e:
            return {
                "success": False,
                "error": str(e)
            }

    async def chat(self, model: str, messages: List[Dict[str, str]], stream: bool = False) -> Dict[str, Any]:
        """
        对话模式

        Args:
            model: 模型名称
            messages: 消息列表 [{"role": "user", "content": "..."}]
            stream: 是否流式输出

        Returns:
            对话结果
        """
        try:
            async with self.session.post(
                f"{self.base_url}/api/chat",
                json={
                    "model": model,
                    "messages": messages,
                    "stream": stream
                }
            ) as resp:
                if resp.status == 200:
                    if stream:
                        # 流式输出
                        full_response = ""
                        async for line in resp.content:
                            if line:
                                chunk = json.loads(line)
                                if "message" in chunk and "content" in chunk["message"]:
                                    content = chunk["message"]["content"]
                                    print(content, end="", flush=True)
                                    full_response += content
                        print()  # 换行
                        return {
                            "success": True,
                            "response": full_response
                        }
                    else:
                        # 非流式输出
                        data = await resp.json()
                        return {
                            "success": True,
                            "response": data.get("message", {}).get("content", "")
                        }
                else:
                    return {
                        "success": False,
                        "error": f"HTTP {resp.status}"
                    }
        except Exception as e:
            return {
                "success": False,
                "error": str(e)
            }

    # ==================== 嵌入功能 ====================

    async def embeddings(self, model: str, prompt: str) -> Dict[str, Any]:
        """
        生成嵌入向量

        Args:
            model: 模型名称
            prompt: 文本

        Returns:
            嵌入向量
        """
        try:
            async with self.session.post(
                f"{self.base_url}/api/embeddings",
                json={
                    "model": model,
                    "prompt": prompt
                }
            ) as resp:
                if resp.status == 200:
                    data = await resp.json()
                    return {
                        "success": True,
                        "embedding": data.get("embedding", [])
                    }
                else:
                    return {
                        "success": False,
                        "error": f"HTTP {resp.status}"
                    }
        except Exception as e:
            return {
                "success": False,
                "error": str(e)
            }


# ==================== CLI 接口 ====================

async def main():
    """命令行接口"""
    import argparse

    parser = argparse.ArgumentParser(description="Ollama 操作控制器")
    parser.add_argument("--base-url", default="http://localhost:11434", help="Ollama API URL")
    parser.add_argument("--list-models", action="store_true", help="列出所有模型")
    parser.add_argument("--show-model", type=str, metavar="NAME", help="显示模型详情")
    parser.add_argument("--pull", type=str, metavar="NAME", help="拉取模型")
    parser.add_argument("--delete", type=str, metavar="NAME", help="删除模型")
    parser.add_argument("--generate", nargs=2, metavar=("MODEL", "PROMPT"), help="生成响应")
    parser.add_argument("--chat", nargs=2, metavar=("MODEL", "MESSAGE"), help="对话模式")
    parser.add_argument("--stream", action="store_true", help="流式输出")

    args = parser.parse_args()

    controller = OllamaController(base_url=args.base_url)

    try:
        await controller.connect()

        if args.list_models:
            result = await controller.list_models()
            print(json.dumps(result, ensure_ascii=False, indent=2))

        elif args.show_model:
            result = await controller.show_model(args.show_model)
            print(json.dumps(result, ensure_ascii=False, indent=2))

        elif args.pull:
            result = await controller.pull_model(args.pull)
            print(json.dumps(result, ensure_ascii=False, indent=2))

        elif args.delete:
            result = await controller.delete_model(args.delete)
            print(json.dumps(result, ensure_ascii=False, indent=2))

        elif args.generate:
            model, prompt = args.generate
            result = await controller.generate(model, prompt, stream=args.stream)
            if not args.stream:
                print(json.dumps(result, ensure_ascii=False, indent=2))

        elif args.chat:
            model, message = args.chat
            messages = [{"role": "user", "content": message}]
            result = await controller.chat(model, messages, stream=args.stream)
            if not args.stream:
                print(json.dumps(result, ensure_ascii=False, indent=2))

        else:
            parser.print_help()

    finally:
        await controller.close()


if __name__ == "__main__":
    asyncio.run(main())
