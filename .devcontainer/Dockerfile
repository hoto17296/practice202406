FROM python:3.12

# Nginx
RUN apt-get update && apt-get install -y nginx
COPY .devcontainer/nginx.conf /etc/nginx/sites-available/default

# Poetry
ENV POETRY_HOME=/etc/poetry
RUN curl -sSL https://install.python-poetry.org | python -
ENV PATH $POETRY_HOME/bin:$PATH
RUN poetry config virtualenvs.create false

WORKDIR /workspace

COPY . .

RUN cd backend && poetry install --with dev

CMD ["nginx", "-g", "daemon off;"]