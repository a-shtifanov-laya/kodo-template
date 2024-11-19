FROM python:3.11-slim

# Install build dependencies, then clean up
RUN apt-get update && apt-get install -y gcc python3-dev && rm -rf /var/lib/apt/lists/*

RUN pip install crewai==0.70.1
RUN pip install crewai-tools==0.12.1
RUN pip install agenticos

WORKDIR /app
COPY . /app

EXPOSE 8000

CMD /bin/sh -c "agentic run --mode=registry --registry=$REGISTRY_URL"