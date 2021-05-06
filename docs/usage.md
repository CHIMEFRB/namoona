## Create Repository
In order to generate your repository from the `namoon`  template, run the following command:

```
cookiecutter git+ssh://git@github.com/chimefrb/namoona.git
```

At this point, you will be asked to enter the following parameter details

???+ note "Template Parameters"
	
	- repository [On Github]: chime-frb-night
	- project [Python Compatible]: frb_night
	- backend [URL Prefix]: night
	- author [Name]: Fogell McLovin
	- email [Contact Email]: fogell.mclovin@hawaii-residents.com


This will generate a folder named `<project-name>` in your present working directory
containining all the relevant files with the proper project layout.

* Next, create a repository on GitHub. To avoid errors, do not initialize the new repository
with README, license, or gitignore files.

* Navigate to the directory `<project-name>`.

* Push the project directory to GitHub with the `<URL>` from repository's Quick Setup page

![Screenshot](https://docs.github.com/assets/images/help/repository/copy-remote-repository-url-quick-setup.png)


## First Steps

???+ "Install Your Package"

	```
	pip install --upgrade poetry && poetry install
	```
	This will all the required dependencies for your package in a virtual environment managed by poetry.

???+ note "Initialize Git"

	```
	git init
	git add .
	```
	This will initialize git to manage the version control for the repository.

???+ note "Setup pre-commit"

	```
	poetry pre-commit install
	```
	This will enabled automated checks to be executed for code quality, each time you do a `git commit`

???+ note "First Commit"

	```
	git add . # Adds the files in the local repository and stages them for commit.
	git commit -m "project template from namoona"
	```
	At this point, you should expect to pre-commit to perform code checks, some of which will fail.
	After the checks are performed, you need to re-add all the changed files to the commit, and try once again.

	```
	git add .
	git commit -m "project template from namoona"
	```

	`pre-commit` will not allow you to push code to the Github Repository until it the minimum collaboration standards.

???+ note "First Push"

	```
	git branch -M main
	git remote add origin <URL>
	git remote -v
	git push -u origin main
	```




