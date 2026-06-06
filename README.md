# 🎨 AI Visual Programming

AI可视化编程工具，支持流程图、逻辑编排、可视化代码。

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10+-blue?logo=python" />
  <img src="https://img.shields.io/badge/OpenAI-API-green?logo=openai" />
  <img src="https://img.shields.io/badge/License-MIT-yellow" />
</p>

## ✨ 特性

- 📊 流程图生成
- 🔧 节点编辑器
- 🧩 积木式编程
- 🔄 状态机编辑器
- 🔀 逻辑构建器
- 💻 代码转换

## 🚀 快速开始

```bash
pip install openai

python tools.py
```

## 📖 使用

```python
from ai_visual_programming import create_tools

tools = create_tools()

# 流程图
flowchart = tools.generate_flowchart("用户注册流程")

# 节点编辑器
editor = tools.generate_node_editor(["输入", "处理", "输出"])

# 积木式编程
blocks = tools.generate_block_programming(["控制", "逻辑", "数学"])

# 状态机编辑器
state_machine = tools.generate_state_machine_editor(["空闲", "处理中", "完成"])

# 逻辑构建器
logic = tools.generate_logic_builder(["条件1", "条件2"], ["动作1", "动作2"])

# 转换为代码
code = tools.convert_to_code(visual_program, "Python")
```

## 📁 项目结构

```
ai-visual-programming/
├── tools.py       # 可视化编程工具核心
└── README.md
```

## 📄 许可证

MIT License
