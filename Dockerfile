FROM python:3.13-slim

WORKDIR /app
COPY ["sing file program.py", "/usr/local/bin/project-scaffold.py"]

ENTRYPOINT ["python", "/usr/local/bin/project-scaffold.py"]
CMD ["--help"]
