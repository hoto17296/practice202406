# Practice 202406

## Setup
Add `.devcontainer/compose.env.yml` file.

``` yaml:compose.env.yml
services:
  workspace:
    environment:
      DEBUG: 1
```

## Start development
0. Open repository in devcontainer
0. Run `Start FastAPI dev server` task
0. Access to http://localhost:8000/