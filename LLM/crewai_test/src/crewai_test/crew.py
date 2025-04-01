from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.llm import LLM
import os
from openai import OpenAI

# Uncomment the following line to use an example of a custom tool
# from crewai_test.tools.custom_tool import MyCustomTool

# Check our tools documentations for more information on how to use them
# from crewai_tools import SerperDevTool


deepseek_llm = OpenAI(
	model="deepseek-r1-250120",
	api_key=os.environ.get("ARK_API_KEY"),
    base_url="https://ark.cn-beijing.volces.com/api/v3"
)

@CrewBase
class CrewaiTestCrew():
	"""CrewaiTest crew"""

	@agent
	def researcher(self) -> Agent:
		return Agent(
			config=self.agents_config['researcher'],
			# tools=[MyCustomTool()], # Example of custom tool, loaded on the beginning of file
			verbose=True,
			llm=deepseek_llm
		)

	@agent
	def reporting_analyst(self) -> Agent:
		return Agent(
			config=self.agents_config['reporting_analyst'],
			verbose=True
			,llm=deepseek_llm
		)

	@task
	def research_task(self) -> Task:
		return Task(
			config=self.tasks_config['research_task'],
		)

	@task
	def reporting_task(self) -> Task:
		return Task(
			config=self.tasks_config['reporting_task'],
			output_file='report.md'
		)

	@crew
	def crew(self) -> Crew:
		"""Creates the CrewaiTest crew"""
		return Crew(
			agents=self.agents, # Automatically created by the @agent decorator
			tasks=self.tasks, # Automatically created by the @task decorator
			process=Process.sequential,
			verbose=True,
			# process=Process.hierarchical, # In case you wanna use that instead https://docs.crewai.com/how-to/Hierarchical/
		)