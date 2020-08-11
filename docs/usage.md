In order to generate your backend simply run,

```
cookiecutter git+ssh://git@github.com/chimefrb/namoona.git
```

At this point, you will be asked to enter the following parameter details,

	
	repository: <project-name> e.g. outrigger-xcorr
	backend: <purpose> e.g. xcorr
	author: <your name> e.g. Kanzi
	email: <your email> e.g. kanzi@bonobo.org

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
	git commit -m "Project Template from namoona"
	```

=== "Push"

	```
	git remote add origin remote repository <URL>
	git remote -v
	git push origin master
	```




