---
title: "Trace AI Agents in MATLAB with OpenTelemetry"
created: 2026-10-15
captured: 2026-10-15
type: video
domain: gcs-software
source: https://www.youtube.com/watch?v=eXDkMO7lgg0
channel: "MATLAB"
published: "2026-10-14"
tags: [drone, gcs-software, video, youtube]
transcript: true
---

# Trace AI Agents in MATLAB with OpenTelemetry

**채널**: MATLAB (공신력 화이트리스트)
**게시**: 2026-10-14
**영상**: https://www.youtube.com/watch?v=eXDkMO7lgg0

## 설명 요약

Learn how to instrument an agentic chatbot using the MATLAB® Interface to OpenTelemetry Support Package and export traces, metrics, and logs to your existing observability platform. Follow each request as it moves through large language model (LLM) calls, tool executions, and agent decisions, and visualize the complete execution path with distributed tracing. This example demonstrates how OpenTelemetry can help engineers and platform teams understand the behavior of AI-powered applications runni

## 자막 (자동 추출, 최대 8000자)

Here's an agentic chatbot running in MATLAB, and every step it takes is traced. You can see each LLM call, tool execution, and decision captured as part of a single request. This isn't just logs, it's a distributed trace, and that means you can answer questions like where is the time spent, how much each request costs, and what actually happened inside the agent loop. When something goes wrong, you can correlate these traces with metrics and logs, even in a production deployment. All of this data is exported using the OpenTelemetry standard, so it will work with cloud providers like Splunk and Datadog, as well as open-source tools like Grafana and Elastic. Our example today shows how to add observability to an AI agent. AI agents are programs that autonomously plan and execute workflows. Typically, agents use large language models to process user queries and identify actions that need to be taken, also known as tool calls. The agent then executes the tool calls that the LLM has identified and returns the result to the LLM. Then, the LLM generates an answer or executes more tool calls. The agent in this example finds the smallest root of a quadratic equation. First, we initialize and configure OpenTelemetry. We only do this one time during our MATLAB session. We set a service name, but otherwise take the default. Next, we load our API key. For security reasons, I store mine in an environment variable. A trace consists of multiple spans, each describing a unit of work, and contains attributes we want to track. Typically, we want a span for each function, and occasionally multiple spans within a function. Nested functions will result in a parent-child relationship between their spans. To build observability into the AI agent workflow, we capture inputs, outputs, properties, and metadata of our interactions with the LLM. We start with a span to capture the details of the agent creation, which we will set as attributes in the span. For each LLM request, we're going to record the request input and output, the number of tokens, and the defined tools in our trace. In addition to our trace, we can use metric instruments to track aggregated quantities like the total token usage across requests. For each tool call, we're going to record information about the tool used as well as its input and output. Now that we've set up our instrumentation, it's time to start the agent. First, we set a top-level span to trace the entire workflow. That context is inherited by functions called within the top-level span's duration. Next, we create a tool registry containing a list of available tools. Then we define our query to solve the simple math problem and answer the query using the agent. We pass in the tool registry to the agent to let our LLM know which tools it can use. Finally, we end the top-level span and clear its scope, and we could display the response here. In this case, the smallest root of x squared plus 2x minus 3 is -3. Now that the agent has run, we can view the trace in our observability provider. It will look something like this. The visualization shows each request sent to the LLM, every tool call, the order in which they happen, and the time they take. For spans where we set additional attributes like token counts, we can see those details. Instrumenting your code with the Open Telemetry add-on for MATLAB makes it possible to trace requests across services, correlate MATLAB workloads with the rest of your system, and debug issues in complex distributed workflows running in production. Instead of guessing what happened inside an AI agent, you can see the full execution path including latency, failures, and cost drivers. You can try this yourself using the Open Telemetry add-on for MATLAB. Start by instrumenting your own workflows, whether that's Simulink Process Advisor CI pipelines, MATLAB Production Server deployments, or AI agents. We make it easy with an auto trace function. From there, you can extend this to track performance trends over time, alert on failures or cost spikes, and integrate MATLAB workloads into your broader observability strategy. Check the links below to get started.
