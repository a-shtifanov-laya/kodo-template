from agenticos.connectors import BaseWorkflowConfig, CrewaiWorkflowConfig
from agenticos.node.models import AgenticConfig

workflows : dict[str,BaseWorkflowConfig] = {}

# Example workflow
# Import the Crew class. If you used the flow from CrewAI docs the following import should work
# If you are getting any erros please correct the import path
from kodo_template.crew import TemplatecrewCrew as Crew

# Define workflows here
# key is the workflow name
workflows["laya-newsletter-heatmap-cliks-workflow"] = CrewaiWorkflowConfig(
    # Description of the workflow
    description="""
        Workflow accepts a path to an html (email) and a file with clicks statistics for each link in the email. 
        It correlates cliks to links and returns a heatmap of the clicks.""",
    # Inputs for the workflow
    inputs={"email_file": "The link to a html file", 
            "clicks_file": "The link to a file with clicks statistics"},
    # The crew class to be used
    crew_cls=Crew,
)

# Create the config object. Change the name to the name of your node
config = AgenticConfig(name="LAYA-newsletter-heatmap-node", workflows=workflows)
