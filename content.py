import git
from git_contributions_importer import *


repo = git.Repo("P:/JIraBitBucket/ecos-scrape")
mock_repo = git.Repo("P:/FreeLance/mock-repo")

importer = Importer([repo], mock_repo)
importer.set_author("amine.a.belgaid@gmail.com")

importer.import_repository()
print("iducx")
print("toeoy")
print("gxcjs")
print("fevad")
