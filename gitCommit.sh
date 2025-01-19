#Update repo
git add .
git commit -am "$1"
branch=$(git rev-parse --abbrev-ref HEAD)
git push origin $branch
