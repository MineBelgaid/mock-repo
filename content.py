import git
from git_contributions_importer import *


repo = git.Repo("P:/JIraBitBucket/ecos-scrape")
mock_repo = git.Repo("P:/FreeLance/mock-repo")

importer = Importer([repo], mock_repo)
importer.set_author(["amine.a.belgaid@gmail.com","amin-belgaid@hotmail.com"])

importer.import_repository()
print("duavj")
print("miijm")
print("xhhnf")
print("timer")
print("bxrbr")
