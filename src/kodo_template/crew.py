from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task

# Uncomment the following line to use an example of a custom tool
from kodo_template.tools.custom_tool import EmlToHtmlTool, HtmlLinkParserTool

# Check our tools documentations for more information on how to use them
from crewai_tools import FileReadTool
file_tool = FileReadTool()

@CrewBase
class TemplatecrewCrew():
	"""Templatecrew crew"""

	@agent
	def data_scientist(self) -> Agent:
		return Agent(
			config=self.agents_config['data_scientist'],
			tools=[EmlToHtmlTool(), HtmlLinkParserTool()],
			verbose=True,
			max_iter=1,
			max_retry_limit=1
		)
	
	# @task
	# def convert_task(self) -> Task:
	# 	return Task(
	# 		config=self.tasks_config['convert_task'],
	# 	)

	@task
	def html_parse_task(self) -> Task:
		return Task(
			config=self.tasks_config['html_parse_task']
		)
	
	
	# @task
	# def heatmap_task(self) -> Task:
	# 	return Task(
	# 		config=self.tasks_config['heatmap_task'],
	# 		output_file='heatmap.png'
	# 	)

	@crew
	def crew(self) -> Crew:
		"""Creates the Templatecrew crew"""
		return Crew(
			agents=self.agents, # Automatically created by the @agent decorator
			tasks=self.tasks, # Automatically created by the @task decorator
			process=Process.sequential,
			verbose=True,
			# process=Process.hierarchical, # In case you wanna use that instead https://docs.crewai.com/how-to/Hierarchical/
		)