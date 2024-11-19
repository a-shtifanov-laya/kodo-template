# Kodosumi Template Workflow

This template is designed to help you set up a multi-agent AI system with ease, leveraging the powerful and flexible framework provided by crewAI and agenticos. Our goal is to enable your agents to collaborate effectively on complex tasks, maximizing their collective intelligence and capabilities. Read more about the project [here](https://masumi.network).

## Installation

### Requirements

- Python >=3.10 <=3.13
- CrewAI
- FastAPI
- Uvicorn
- [uv](https://docs.astral.sh/uv/)

### Setup Instructions

1. **Install `uv`:**

   ```bash
   pip install uv
   ```

2. **Install `pipx` and `crewai`:**

   ```bash
   python3 -m pip install --user pipx
   python3 -m pipx ensurepath
   pipx install crewai
   ```

3. **Clone the Repository:**

   ```bash
   git clone <repository-url>
   cd kodo-template
   ```

4. **Install Dependencies:**

   ```bash
   crewai install
   ```

5. **Set Up Environment Variables:**

   Create a `.env` file in the root directory with the following content:

   ```plaintext
   OPENAI_API_KEY=your_openai_api_key
   ```

## Customizing

- Modify `src/templatecrew/config/agents.yaml` to define your agents.
- Modify `src/templatecrew/config/tasks.yaml` to define your tasks.
- Modify `src/templatecrew/crew.py` to add your own logic, tools, and specific args.
- Modify `src/templatecrew/main.py` to add custom inputs for your agents and tasks.

## Running the Project

To kickstart your crew of AI agents and begin task execution, run this from the root folder of your project:

```bash
crewai run
```

This command initializes the templatecrew Crew, assembling the agents and assigning them tasks as defined in your configuration.

## Running the Agentic Package

To run the agentic package, use:

```bash
agentic run
```

Ensure FastAPI and Uvicorn are installed as they are required for the HTTP server mode.

## Running a Remote Node as a Tool

1. **Create Config Files:**

   ```bash
   agentic init
   ```

2. **Run Locally:**

   ```bash
   agentic run
   ```

   - Visit [http://127.0.0.1:8000/health](http://127.0.0.1:8000/health) to check the status.
   - Visit [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs) for the Swagger UI.

3. **Attach to the Registry:**

   ```bash
   agentic run --mode=registry --registry=wss://dev-agentic-registry.house-of-communication.world
   ```

   - Visit the Swagger UI at [https://dev-agentic-registry.house-of-communication.world/swagger/index.html](https://dev-agentic-registry.house-of-communication.world/swagger/index.html).

4. **Run and Attach to the Registry from Docker:**

   ```bash
   docker-compose up
   ```

   - Verify the endpoints:
     - [http://localhost:8001/docs](http://localhost:8001/docs)
     - [http://localhost:8002/docs](http://localhost:8002/docs)

## Support

For support, questions, or feedback regarding the Templatecrew Crew or crewAI:
- Visit [masumi homepage](https://www.masumi.network/)
- Join our Discord (if you know you know)
- Visit CrewAI [documentation](https://docs.crewai.com)