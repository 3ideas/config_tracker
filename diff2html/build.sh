docker build -t diff2html .
docker create -ti --name dummy diff2html bash
docker cp dummy:/app/diff2html-cli-master/diff2html-cli-linux  .
docker cp dummy:/app/diff2html-cli-master/node_modules/open/xdg-open .
cp diff2html-cli-linux test/
cp github.min.css test/
cp xdg-open test/
cp template.html test/
docker rm -f dummy
