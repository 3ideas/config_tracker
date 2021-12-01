FROM registry.access.redhat.com/ubi8/ubi-minimal
#FROM node
WORKDIR /app

COPY diff2html-cli-linux /app/diff2html-cli-linux
COPY xdg-open /app/xdg-open
COPY text1 /app/text1
COPY text2 /app/text2
COPY diff.out /app/diff.out
COPY template.html /app/template.html
RUN ./diff2html-cli-linux -i file diff.out -f html --htmlWrapperTemplate template.html -s side -F result.html
CMD ["bash"]
