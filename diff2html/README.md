# diff2html docker build env

Build of diff2html for Redhat linux.

Docker image has diff2html installed in it. 

Also Pkg is installed to package it up nicely!


To build the docker image run

docker build -t diff2html .

To run shell in it.

docker run -it diff2html bash



NOTE generates diff2html-cli-linux and xdg-open (both are reqired on the target system for it to work). 

Also the template.html file can be customised and the github.css file is needed for the styling.


Example:

diff -u text1 text2 >diff.out
./diff2html-cli-linux -i file diff.out -f html --htmlWrapperTemplate template.html -s side -F result.html


Note: currently buids from the tarball from https://www.npmjs.com/package/diff2html-cli, the build should really fetch this. See also https://github.com/rtfpessoa/diff2html
