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
