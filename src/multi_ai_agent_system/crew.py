from crewai import LLM, Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from .config.base import API_KEY, BASE_URL, MODEL

# If you want to run a snippet of code before or after the crew starts,
# you can use the @before_kickoff and @after_kickoff decorators
# https://docs.crewai.com/concepts/crews#example-crew-class-with-decorators

@CrewBase
class MultiAiAgentSystem():
    """MultiAiAgentSystem crew"""

    # Learn more about YAML configuration files here:
    # Agents: https://docs.crewai.com/concepts/agents#yaml-configuration-recommended
    # Tasks: https://docs.crewai.com/concepts/tasks#yaml-configuration-recommended
    agents_config = 'config/agents.yaml'
    tasks_config = 'config/tasks.yaml'

    ai_llm = LLM(
        model=MODEL,
        base_url=BASE_URL,
        api_key=API_KEY
    )

    # If you would like to add tools to your agents, you can learn more about it here:
    # https://docs.crewai.com/concepts/agents#agent-tools
    @agent
    def planner(self) -> Agent:
        return Agent(
            config=self.agents_config['planner'],
            verbose=True,
            llm=self.ai_llm
        )

    @agent
    def writer(self) -> Agent:
        return Agent(
            config=self.agents_config['writer'],
            verbose=True,
            llm=self.ai_llm
        )
    
    @agent
    def editor(self) -> Agent:
        return Agent(
            config=self.agents_config['editor'],
            verbose=True,
            llm=self.ai_llm
        )

    # To learn more about structured task outputs,
    # task dependencies, and task callbacks, check out the documentation:
    # https://docs.crewai.com/concepts/tasks#overview-of-a-task
    @task
    def plan_task(self) -> Task:
        return Task(
            config=self.tasks_config['plan_task'],
        )

    @task
    def write_task(self) -> Task:
        return Task(
            config=self.tasks_config['write_task'],
        )
    
    @task
    def edit_task(self) -> Task:
        return Task(
            config=self.tasks_config['edit_task'],
        )

    @crew
    def crew(self) -> Crew:
        """Creates the MultiAiAgentSystem crew"""
        # To learn how to add knowledge sources to your crew, check out the documentation:
        # https://docs.crewai.com/concepts/knowledge#what-is-knowledge

        return Crew(
            agents=self.agents, # Automatically created by the @agent decorator
            tasks=self.tasks, # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=True,
            # process=Process.hierarchical, # In case you wanna use that instead https://docs.crewai.com/how-to/Hierarchical/
        )
