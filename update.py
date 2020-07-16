def update():
	from git import Repo
	import os
	url = "https://github.com/OfekShochat/common_errors"
	Repo.clone_from(url, ".")
update()