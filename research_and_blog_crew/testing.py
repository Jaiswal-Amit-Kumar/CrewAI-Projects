from crewai import Agent, LLM, Task
import requests

# 🧪 Test Ollama connectivity FIRST
print("🧪 Testing Ollama connectivity...")
try:
    response = requests.get("http://localhost:11434/api/tags", timeout=10)
    print("✅ Ollama server reachable!")
    print("Available models:", [m['name'] for m in response.json()['models']])
except Exception as e:
    print("❌ Ollama NOT reachable:", e)
    print("💡 Start Ollama: ollama serve")
    exit(1)

# ✅ Now create LLM
print("\n🔄 Initializing Ollama LLM...")
llm = LLM(
    model="ollama/llama3.1",  # Remove 'ollama/' prefix
    base_url="http://localhost:11434"
)

agent = Agent(
    role='Local AI Expert',
    goal='Test connection',
    backstory="Local AI testing Ollama integration.",
    llm=llm,
    verbose=True,
    allow_delegation=False,
    tools=[]  # ✅ NO tools as requested
)

test_task = Task(
    description="Say hello briefly. Confirm Ollama model.",
    agent=agent,
    expected_output="Short greeting.",
    tools=[]  # ✅ NO tools
)

print("\n🚀 Running test...")
response = agent.execute_task(test_task)
print("✅ SUCCESS:", response)
