from invoke import task

@task
def start(ctx):
    ctx.run("python3 src/main.py", pty=True)

@task
def coverage(ctx):
    ctx.run("coverage run --branch -m pytest", pty=True)

@task()
def coverage_report(ctx):
    ctx.run("coverage html", pty=True)

@task()
def report(ctx):
    ctx.run("coverage report -m", pty=True)

@task()
def lint(ctx):
    ctx.run("pylint src", pty=True)

@task
def build(ctx):
    ctx.run("")