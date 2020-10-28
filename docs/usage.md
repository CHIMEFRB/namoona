In order to generate your backend simply run,

```
cookiecutter git+ssh://git@github.com/chimefrb/namoona.git
```

At this point, you will be asked to enter the following parameter details,

	
	repository [On Github]: chime-frb-night
	project [Python Compatible]: frb_night
	backend [URL Prefix]: night
    # This will yield in a url location of /maestro/night
	author [Name]: Fogell McLovin
	email [Contact Email]: fogell.mclovin@hawaii-residents.com

This will generate a folder named `<project-name>` in your present working directory
containining all the relevant files with the proper project layout.

* Next, create a repository on GitHub. To avoid errors, do not initialize the new repository
with README, license, or gitignore files.

* Navigate to the directory `<project-name>`.

* Push the project directory to GitHub with the `<URL>` from repository's Quick Setup page

![Screenshot](https://docs.github.com/assets/images/help/repository/copy-remote-repository-url-quick-setup.png)

=== "Initialize"

	```
	git init
	```

=== "Commit"

	```
	git add . # Adds the files in the local repository and stages them for commit.
	pre-commit run --all-files
	git commit -m "project template from namoona"
	git branch -M main
	```

=== "Push"

	```
	git remote add origin <URL>
	git remote -v
	git push -u origin main
	```




