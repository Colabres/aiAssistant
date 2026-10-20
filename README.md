
# aiAssistant — Local LLM-Powered Voice Assistant

**Python | Local LLMs | llama.cpp | Context Retrieval | Speech Processing**

A modular AI assistant designed to explore low-latency interaction with locally hosted large language models.

Instead of relying on a remote AI service for every interaction, aiAssistant runs its language model locally and uses a two-stage processing pipeline to identify relevant information before constructing a compact prompt.

The project focuses on practical challenges in LLM application engineering: efficient context management, modular components, response latency, and maintaining useful information across conversations.

## Overview

aiAssistant is an experimental personal AI assistant combining local language model inference, context retrieval, and optional speech interaction.

The system is designed around a simple principle: not every interaction requires sending the entire available context to a language model.

Instead, the assistant first processes the user's input, identifies relevant stored information, and constructs a smaller prompt for the main language model.

This approach explores the trade-offs between context size, information relevance, response quality, and inference latency.

The project also supports adding new facts through conversation without retraining or fine-tuning the underlying model.

## Key Features

### Local LLM Inference

- Runs language models locally using `llama.cpp`.
- Reduces dependence on external inference services.
- Allows experimentation with different local models and inference configurations.

### Two-Stage Processing Pipeline

The assistant separates context selection from response generation.

1. **Input processing:** Interpret the incoming user request.
2. **Context retrieval:** Identify stored facts relevant to the request.
3. **Prompt construction:** Assemble a compact prompt containing the selected information.
4. **Response generation:** Send the prompt to the local language model.

The goal is to reduce unnecessary context processing while preserving relevant information.

### Conversational Knowledge Updates

The assistant supports adding new facts through conversation.

Rather than modifying the model's weights, information is stored externally and can be retrieved during later interactions.

This separates the language model's general capabilities from the assistant's application-specific knowledge.

### Modular Speech Interface

Speech recognition and speech synthesis are implemented as replaceable components.

This allows the project to experiment with different speech-processing solutions without redesigning the core assistant.

### Configurable Architecture

The project separates application logic, configuration, and supporting components to make experimentation and further development easier.

## System Architecture

The assistant follows a retrieval-assisted generation approach.

```text
             User Input
                 |
                 v
        Input Processing
                 |
                 v
       Context Identification
                 |
                 v
        Relevant Fact Retrieval
                 |
                 v
       Compact Prompt Assembly
                 |
                 v
          Local LLM
          (llama.cpp)
                 |
                 v
          AI Response
                 |
                 v
       Optional Speech Output
```

New information can be stored separately from the language model and made available to subsequent interactions.

The architecture is intended to support independent experimentation with retrieval strategies, model inference, and speech-processing components.

## Technology Stack

| Area | Technology |
|------|------------|
| Primary language | Python |
| LLM inference | llama.cpp |
| Language models | Locally hosted LLMs |
| Context management | Application-level fact retrieval |
| Speech interface | Pluggable speech recognition and synthesis |
| Configuration | Project configuration files |
| Testing | Python test components |

## Engineering Decisions

### Why Local Inference?

Local inference provides greater control over model selection, runtime configuration, and the handling of user data.

It also makes it possible to investigate inference performance directly without relying entirely on external API services.

The trade-off is that model execution depends on the available local hardware and its computational resources.

### Why Separate Retrieval from Generation?

Sending increasingly large conversation histories or knowledge collections to a language model increases the amount of context that must be processed.

aiAssistant explores a different approach: selecting relevant information before constructing the final generation prompt.

This introduces an additional processing stage but may reduce the amount of context handled by the main model.

The effectiveness of this approach depends on retrieval accuracy, intermediate processing overhead, and model performance.

### Why Store Facts Externally?

Updating model weights whenever new information becomes available is impractical for a personal assistant.

External fact storage makes it possible to add or update application knowledge independently of the language model.

It also allows experimentation with different information retrieval and context selection strategies.

### Why Modular Speech Components?

Speech recognition and synthesis technologies have different performance characteristics, hardware requirements, and integration constraints.

Keeping these components separate from the assistant's main logic makes it easier to replace or improve them.

## Performance Considerations

Response latency is an important design concern.

The system explores several factors that influence the responsiveness of local LLM applications:

- Prompt length and context size.
- Retrieval and preprocessing overhead.
- Local model inference speed.
- Hardware limitations.
- Additional processing required for speech interaction.

The two-stage pipeline is designed to investigate whether the cost of retrieving relevant context can be offset by reducing the amount of information processed during response generation.

No universal latency improvement is assumed; performance depends on the model, hardware, and workload.

## Project Status

**Status: Experimental prototype / ongoing development**

aiAssistant is a personal software engineering project focused on exploring practical LLM application architecture.

The current implementation provides a foundation for experimenting with local inference, context retrieval, conversational knowledge management, and speech interaction.

It is not presented as a production-ready assistant.

## Possible Future Development

- Benchmark response latency across different models and context sizes.
- Evaluate retrieval accuracy and the impact of missing context.
- Improve conversational knowledge management.
- Expand automated testing.
- Compare alternative speech recognition and synthesis components.
- Improve configuration and setup portability.

---

## Installation, Configuration and Usage

The original project setup instructions are retained below to preserve the development workflow, dependencies, configuration details, and commands needed to resume work on the assistant.

## Quickstart
```bash
# create & activate venv (PowerShell)
python -m venv .venv
.\.venv\Scripts\Activate.ps1

pip install -r requirements.txt -r requirements-dev.txt
python -m src.app --mode cool
