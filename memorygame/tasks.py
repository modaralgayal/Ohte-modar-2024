from invoke import task

@task
def start(ctx):
    ctx.run("python3 memorygame/main.py")