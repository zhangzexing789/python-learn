Please analyze the currently opened Xceptor Airflow DAG files and extract a reusable implementation pattern.

I want you to do this in stages.

Stage 1 - analysis only:
1. Summarize the common structure across these DAGs.
2. Identify:
   - dag_id naming pattern
   - file naming pattern
   - default_args pattern
   - schedule pattern
   - task naming pattern
   - common imports
   - helper / utility usage
   - retry / timeout / alerting conventions
   - dependency declaration style
3. Separate:
   - fixed project conventions
   - variable business-specific inputs
4. List anything that is inconsistent across the examples.

Do not generate new code yet.
Do not modify files yet.
Return the result as a structured report.


基于已验证的分析，起草一份仓库级别的 Copilot 指令文件。

目标文件：

.github/copilot-instructions.md

要求：

- 重点关注 Xceptor Airflow DAG 开发的常驻项目规则。

- 包含命名约定、常用导入、辅助函数使用、重试/超时/告警规则以及验证预期。

- 保持简洁易懂，便于操作。

- 不要包含推测性规则。

- 使用 Markdown 格式。

暂时不要编写文件。

请先给我看看草稿。


现在，请起草一份可复用的提示文件，用于创建新的 Xceptor Airflow DAG。

目标文件：

.github/prompts/create-xceptor-dag.prompt.md

要求：

- 此提示应引导 Copilot 根据业务需求创建新的 DAG。

- 它应指示 Copilot 首先检查代码库中类似的 DAG。

- 它应要求重用现有的辅助函数和模式。

- 当缺少输入时，它应明确询问假设条件。

- 它应输出：

1. 类似 DAG 的分析

2. 建议的 DAG 结构

3. 生成的代码

4. 审核清单

请先给我看看草稿。暂时不要创建文件。

现在请为 Xceptor Airflow DAG 生成编写一个代理技能。

目标文件夹：

.github/skills/xceptor-airflow-dag/

目标文件：

.github/skills/xceptor-airflow-dag/SKILL.md

要求：

- 说明何时应使用此技能。

- 要求在生成新代码之前检查现有的 DAG。

- 优先使用现有的仓库辅助方法和约定，而不是通用模式。

- 定义预期的工作流程：

1. 检查示例

2. 识别固定约定和可变输入

3. 提出结构建议

4. 生成代码

5. 提供审查清单

- 参考支持资源：

- examples/

- templates/

- checklists/

请先给我看看草稿。

暂时不要创建文件。


Use the repository instructions, the create-xceptor-dag prompt pattern, and the xceptor-airflow-dag skill to design a new DAG for the following requirement:

[这里写你的真实需求]

Important:
- First inspect similar DAGs in the repository.
- Reuse existing helpers and conventions.
- Do not modify production files yet.
- First show:
  1. similar DAGs found
  2. extracted pattern
  3. assumptions
  4. proposed DAG layout
- Only then generate the DAG code.
