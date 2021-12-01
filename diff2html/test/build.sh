docker build -t diff2html_test .
docker create -ti --name dummy diff2html_test bash
docker cp dummy:/app/result.html  .
docker rm -f dummy
