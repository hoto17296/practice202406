FROM python:3.12

# Nginx
RUN apt-get update && apt-get install -y nginx

# Node
RUN curl -fsSL https://deb.nodesource.com/setup_lts.x | bash && apt-get install -y nodejs

# Poetry
ENV POETRY_HOME /etc/poetry
RUN curl -fsSL https://install.python-poetry.org | python -
ENV PATH $POETRY_HOME/bin:$PATH
RUN poetry config virtualenvs.create false