from invoke import task

@task
def start(ctx):
	ctx.run("python3 src/main.py")

@task
def test(ctx):
	ctx.run("python3 src/tests/harry_test.py")
@task
def coverage(ctx):
	ctx.run("coverage run --branch -m pytest src")

@task(coverage)
def coverage_report(ctx):
	ctx.run("coverage html")
@task
def lint(ctx):
	ctx.run("pylint src")