"""
AI Visual Programming - AI可视化编程工具
支持流程图、逻辑编排、可视化代码
"""

import json
import os
from typing import Dict, List, Any
from datetime import datetime

try:
    from openai import OpenAI
    OPENAI_AVAILABLE = True
except ImportError:
    OPENAI_AVAILABLE = False


class AIVisualProgrammingTools:
    """
    AI可视化编程工具
    支持：流程图、逻辑编排、可视化代码
    """

    def __init__(self, model: str = "mimo-v2.5-pro", api_key: str = None, base_url: str = None):
        self.model = model
        if OPENAI_AVAILABLE:
            self.client = OpenAI(
                api_key=api_key or os.environ.get('OPENAI_API_KEY', ''),
                base_url=base_url or os.environ.get('OPENAI_BASE_URL', 'https://api.xiaomimimo.com/v1')
            )
        else:
            self.client = None

    def generate_flowchart(self, process: str) -> str:
        """生成流程图"""
        if not self.client:
            return "LLM客户端未配置"

        prompt = f"""请为以下流程生成Mermaid流程图：

{process}

请返回Mermaid格式代码："""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=1000
        )

        return response.choices[0].message.content

    def generate_node_editor(self, node_types: List[str]) -> str:
        """生成节点编辑器"""
        if not self.client:
            return "LLM客户端未配置"

        types_text = ", ".join(node_types)

        prompt = f"""请生成可视化节点编辑器：

节点类型：{types_text}

要求：
1. 拖拽连接
2. 属性编辑
3. 执行预览
4. 代码导出"""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=3000
        )

        return response.choices[0].message.content

    def generate_block_programming(self, categories: List[str]) -> str:
        """生成积木式编程"""
        if not self.client:
            return "LLM客户端未配置"

        categories_text = ", ".join(categories)

        prompt = f"""请生成积木式编程界面：

类别：{categories_text}

要求：
1. 拖拽拼接
2. 语法检查
3. 实时预览
4. 代码转换"""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=3000
        )

        return response.choices[0].message.content

    def generate_state_machine_editor(self, states: List[str]) -> str:
        """生成状态机编辑器"""
        if not self.client:
            return "LLM客户端未配置"

        states_text = ", ".join(states)

        prompt = f"""请生成状态机可视化编辑器：

状态：{states_text}

要求：
1. 状态节点
2. 转换箭头
3. 条件编辑
4. 代码生成"""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=2000
        )

        return response.choices[0].message.content

    def generate_logic_builder(self, conditions: List[str], actions: List[str]) -> str:
        """生成逻辑构建器"""
        if not self.client:
            return "LLM客户端未配置"

        conditions_text = ", ".join(conditions)
        actions_text = ", ".join(actions)

        prompt = f"""请生成可视化逻辑构建器：

条件：{conditions_text}
动作：{actions_text}

要求：
1. IF-THEN-ELSE
2. 拖拽编辑
3. 测试功能
4. 代码导出"""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=2000
        )

        return response.choices[0].message.content

    def convert_to_code(self, visual_program: Dict, language: str) -> str:
        """转换为代码"""
        if not self.client:
            return "LLM客户端未配置"

        program_text = json.dumps(visual_program, ensure_ascii=False)

        prompt = f"""请将以下可视化程序转换为{language}代码：

{program_text}

要求：
1. 完整可运行
2. 注释说明
3. 错误处理"""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=3000
        )

        return response.choices[0].message.content


def create_tools(**kwargs) -> AIVisualProgrammingTools:
    """创建可视化编程工具"""
    return AIVisualProgrammingTools(**kwargs)


if __name__ == "__main__":
    tools = create_tools()

    print("AI Visual Programming Tools")
    print()

    # 测试
    flowchart = tools.generate_flowchart("用户注册流程：输入信息 -> 验证 -> 创建账号 -> 发送邮件")
    print(flowchart)
