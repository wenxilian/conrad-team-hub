# Python 与嵌入式：L1–L4 能力

> 资料性质：本项目建议 / 教学分析。整理与核查日期：2026-10-12。本站为非官方独立学习资料。

总体判断：通常较强高中生经过训练可完成大学低年级工程课程设计级别原型；更复杂的无人机集群、控制系统涉及高阶知识，但可通过使用成熟平台、限定核心创新范围控制难度。赛事不是统一要求工业级完成品。

编程分层：
- L1 基础：Python 函数、循环、文件读写、调试和可视化。
- L2 工程：传感器数据、硬件控制、模块化、异常处理。
- L3 集成：控制回路、通信、日志、端到端运行及基本自动化测试。
- L4 优化：实验对照、算法基准、误差和可靠性评估。团队总体目标建议 L3，创新核心争取 L4。

测试四层：Proof of Concept (功能可运行)、Performance Testing (有指标)、Benchmarking (与 baseline 比较)、Reliability Testing (扰动/重复/异常条件)。技术报告应保存失败试验，而不是只剪辑一次成功视频。

对于工程类案例：FireAIDSS 偏数据、AI 与多机仿真；Aphelion 偏机电、控制与功耗测量；RescueBot 偏移动机器人、嵌入式、传感与安全。学生必须能解释自己写的代码、借用框架/开源组件的来源、关键结果如何计算。可以采用现有 PX4/ArduPilot、Arduino/ESP32、Python 等工具，但不应暗示每行程序都由学生原创。

建议工程资料目录：`engineering-design.md`、`hardware-bom.xlsx`、`src/`、`tests/`、`data/`、`engineering-validation.md`、`demo/`；这些为**保密项目内部工作区的建议**，不是公开学习网站内容。

## 延伸阅读

- [验证四层](testing.md)。
- [安全边界](../06-planning/safety.md)。

资料边界与更正记录见 [来源核查](../07-resources/source-method.md)。
