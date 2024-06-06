FROM python:3.12

# Nginx
RUN apt-get update && apt-get install -y nginx
COPY .devcontainer/nginx.conf /etc/nginx/sites-available/default

# Bun
RUN curl -fsSL https://bun.sh/install | bash
ENV PATH $PATH:/root/.bun/bin

# Poetry
ENV POETRY_HOME /etc/poetry
RUN curl -sSL https://install.python-poetry.org | python -
ENV PATH $POETRY_HOME/bin:$PATH
RUN poetry config virtualenvs.create false

WORKDIR /workspace

COPY . .

RUN cd backend && poetry install --with dev
RUN prisma generate --schema postgres/schema.prisma

RUN cd frontend && bun install
RUN bash generate-api-spec.sh

CMD ["nginx", "-g", "daemon off;"]