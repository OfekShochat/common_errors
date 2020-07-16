from git import Repo

def update():
    Repo.clone_from("https://github.com/OfekShochat/common_errors.git", "./")
update()