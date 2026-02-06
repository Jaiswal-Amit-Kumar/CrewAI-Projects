from crewai import Agent, Crew, Process, Task, LLM
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent
from typing import List

llm = LLM(model = "ollama/phi3:latest", base_url = "http://localhost:11434", num_ctx = 3000, timeout = 300)

@CrewBase
class ResearchReport:

    agents_config = 'config/agents.yaml'
    tasks_config = 'config/tasks.yaml'

    # ---------------------------Agents-----------------------------
    # agent 1
    @agent
    def researcher_agent(self) -> Agent:
        return Agent(
            config = self.agents_config['researcher_agent'],
            llm = llm,
            verbose = True,
            return_direct=True
        )
    
    #agent 2
    @agent
    def writer_agent(self) -> Agent:
        return Agent(
            config = self.agents_config['writer_agent'],
            llm = llm,
            verbose = True,
            return_direct=True
        )
    
    # ---------------------------------Tasks---------------------------------
    #task 1
    @task
    def researching_task(self) -> Task:
        return Task(
            config = self.tasks_config['researching_task'],
            output_file = 'research_notes/detailed_research_notes.md'
        )
    
    # task 2
    @task
    def writer_task(self) -> Task:
        return Task(
            research_notes_text = open('research_notes/detailed_research_notes.md').read(),
            config = self.tasks_config['writer_task'],
            context = [research_notes_text],
            output_file = 'research_paper/IEEE_format_research_paper.md',
            return_direct = True
        )
    
    
    # ------------------------------------Crew-------------------------------
    @crew
    def crew(self) -> Crew:
        return Crew(
            agents = self.agents,
            tasks = self.tasks,
            process = Process.sequential,
            verbose = True
        )
