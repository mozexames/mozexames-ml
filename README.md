# mozexames-ml

Exams data extractor w/ Machine Learning.

## Getting started

1. `cp .env.example .env`
2. `./run build`
3. Then use `./run app` to execute the main `src/app.py` script.

> **Note**
> If you want to run individual scripts, use `./run python SCRIPT_PATH`.<br>
> <sub>E.g: the `./run app` command essential does `./run python src/app.py`</sub>

## Development

<!-- TODO: Update to python docs -->
- `./run cmd` to start the Interactive Ruby Shell (`irb`)
- `./run bash` to enter `bash`
- To add new `gems`, either:
  - `./run bundle:add GEM_NAME`
  - Or, manually insert the new gem into `Gemfile` then run `./run bundle:install`.

## Credits

This stack is adapted from:

- https://github.com/docker/awesome-compose/tree/master/official-documentation-samples/rails/
- https://github.com/nickjj/docker-rails-example
