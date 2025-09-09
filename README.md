# CC-Proxy-Executable 🔄

**Use Anthropic clients (like Claude Code) with any OpenAI-compatible API, including Gemini, OpenAI, or custom endpoints.** 🤝

A proxy server that lets you use Anthropic clients with Gemini, OpenAI, or any other OpenAI-compatible API, all via LiteLLM. 🌉

![Anthropic API Proxy](pic.png)

## Quick Start ⚡

The only prerequisite is to have [uv](https://github.com/astral-sh/uv) installed.

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

### Installation and Usage

You can install and run the proxy directly from GitHub with a single command. You will need to provide an API key for the service you want to use.

For OpenAI, you would run:
```bash
LLM_API_KEY="your-openai-api-key" uvx https://github.com/minpeter/cc-proxy-executable.git
```

This will start the proxy server on `http://localhost:8082`.

### Using with Claude Code 🎮

1. **Install Claude Code** (if you haven't already):
   ```bash
   npm install -g @anthropic-ai/claude-code
   ```

2. **Connect to your proxy**:
   ```bash
   ANTHROPIC_BASE_URL=http://localhost:8082 claude
   ```

3. **That's it!** Your Claude Code client will now use the configured backend models through the proxy. 🎯

## Using Custom OpenAI-Compatible APIs

You can easily switch to any OpenAI-compatible API by setting the `LLM_BASE_URL` and `LLM_API_KEY` environment variables.

### Example: Using Friendli.ai

To use the proxy with `friendli.ai`, you would run the following command:

```bash
LLM_BASE_URL="https://api.friendli.ai/serverless/v1" \
LLM_API_KEY="your-friendli-token" \
BIG_MODEL="Qwen/Qwen3-32B" \
SMALL_MODEL="Qwen/Qwen3-235B-A22B-Instruct-2507" \
uvx https://github.com/minpeter/cc-proxy-executable.git
```

In this example:
- `LLM_BASE_URL` is set to the Friendli.ai serverless endpoint.
- `LLM_API_KEY` should be your `FRIENDLI_TOKEN`.
- `BIG_MODEL` and `SMALL_MODEL` are set to the desired model on Friendli.ai.

## How It Works 🧩

This proxy works by:

1. **Receiving requests** in Anthropic's API format 📥
2. **Translating** the requests to OpenAI format via LiteLLM 🔄
3. **Sending** the translated request to the configured backend 📤
4. **Converting** the response back to Anthropic format 🔄
5. **Returning** the formatted response to the client ✅

The proxy handles both streaming and non-streaming responses, maintaining compatibility with all Claude clients. 🌊
