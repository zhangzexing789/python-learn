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



Hi Ajay, today I will go through the Xceptor monitoring dashboard.
Let me briefly introduce the technology stack.

We are using:

- Loki and Promtail for log aggregation 
- Telegraf for collecting system and application data
- InfluxDB for storing metrics data and alerting
- Grafana for visualization

⸻

🟦 3. Data Flow（1–2 min）

This diagram shows the end-to-end monitoring data flow.

We collect metrics and logs from:

* Windows servers
* Kubernetes cluster

Then the log data will be sent to InfluxDB through the Telegraf.
Grafana queries the data and builds dashboards.

For alerting, we setup some InfluxDB tasks and send the alerting notification to Symphony and xMatters.

this is the whole data flow for monitoring dash.

🟩 4.1 Upstream File Monitoring（2–3 min）

First, we start from upstream file monitoring.

from this dashboard we can know:

* whether the file receives in s3
* whether it receives on time

If the file is delayed, we can detect it quickly and the alerts will be triggered automatically.
And this is the email notification we have sent out.


we also capture the detail data volume for each upstream system and monitor data volume trends and compare them with expected baselines. 

For dynamic sources like GHSS, we use flexible baseline and base our observation, here we define a maximum baseline with 3000 and another minimum baseline with 2500

These dashboards help us identify the problems early.

we also built a dashboard to track the files processing status, make sure every file is processing successfully.


🟩 4.2 Solace 

Because all the file events are consumed by solace service，so we have built a dashboard to monitor the status for solace service. like the solace Queue Depth.

Once a file arrives, an event is generated and the listener built in Solace will consume the event and triggers downstream processing. 


🟩 4.3 Airflow（2 min）

After that, Airflow is triggered to process the data.

We monitor:

* DAG execution status
* execution duration

4.4 IKP service 
In Xceptor project, we also have the IKP service in DataLayer to process data, from in this dashboard, we can monitor the pod status in the IKP cluster.

🟩 4.6 IKP API Metrics

For IKP API metrics, we track:

- CPU and memory usage
- success rate
- api response time

For performance, we look at response time trends. If latency increases continuously, it indicates performance issues.

For example, high CPU together with high latency usually means a performance bottleneck.

Also, CPU 100% here does not always mean a problem. It represents container-level usage, so we always look at multiple metrics together.
It always mean this api is handling more complex task.

⸻
🟩 4.6 Xceptor API Metrics
Besides, we also monitor the Xceptor API metrics, including sucessful rate of input message api and dataset api.

Question here:
- if Ajay ask why the successful rates of input message api are not 100%, we can say that it is normal becasue there is a existing case which is following up with user and a feed is proccessing failed in Xceptor side. For dataset api, it is normal as well because the authentication token is expired every hour and we have a mechanism to refresh it
-  how to know api is not working
    - we have set up alert rules to notify us if the successful rate drops below a certain threshold, which indicates potential issues with the API. 

Additionally, we monitor response time and CPU/memory usage, as significant deviations from normal patterns can also signal problems with the API performance or stability.

🟩 4.7 Windows server monitoring

In Xceptor side, we have windows servers to host Xceptor Services, including Web server, App Server and DB Server

We track:

* CPU
* memory
* disk usage
* service status

For example, here we can immediately detect if a service is stopped.

If CPU or memory is too high, and at the same time API latency increases, it indicates a system bottleneck.

This helps us quickly identify and troubleshoot issues.

⸻

🟩 4.8 MQ Connectivity（1 min）

We also monitor MQ connectivity.

If the connection fails, it means system integration is broken.

So this ensures all components can communicate properly.


🟩 4.4 Record Count（🔥非常重要）（2 min）
Regarding this dashboard, the issue we encountered last time was an unexpected data deletion in the legal entity table.

So we build this dashboard to monitor the record count trends for some key table in Xceptor DB to detect abnormal drops.

Calculate the 3 day average as the baseline, if the current count is 30% lower than baseline, send alert.

This helps us identify data issues before they impact downstream systems.

⸻

🟩 4.5 Downstream Kafka（1–2 min）

Then the data is delivered to downstream systems via Kafka.

We monitor:

* source record count
* success record count

If they don’t match, it means data delivery has issues.

This ensures no data is lost during delivery.

⸻

🟩 4.9 CI/CD（1 min）

Finally, we monitor CI/CD pipelines using Jenkins.

We track:

* build success rate
* deployment stability

This gives us visibility into release quality.


