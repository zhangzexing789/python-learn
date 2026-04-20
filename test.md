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
