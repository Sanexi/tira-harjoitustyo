from invoke import task

@task
def test(ctx):
    ctx.run("pytest src")

@task
def coverage(ctx):
    ctx.run("coverage run --omit 'venv/*' --branch -m pytest src ")

@task(coverage)
def coverage_report(ctx):
    ctx.run("coverage html")

@task
def lint(ctx):
    ctx.run("pylint src")

@task
def format(ctx):
    ctx.run("autopep8 --in-place --recursive src")

