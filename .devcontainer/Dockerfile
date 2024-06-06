FROM python:3.12

# Poetry
ENV POETRY_HOME=/etc/poetry
RUN curl -sSL https://install.python-poetry.org | python -
ENV PATH $POETRY_HOME/bin:$PATH
RUN poetry config virtualenvs.create false

WORKDIR /workspace

COPY . .

RUN cd backend && poetry install --with dev