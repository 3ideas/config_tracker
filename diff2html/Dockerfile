FROM registry.access.redhat.com/ubi8/nodejs-12
#FROM node
WORKDIR /app

#RUN npm install -g diff2html-cli
RUN npm install -g pkg
RUN npm install --global yarn
USER root
RUN yum install zip unzip -y
RUN cd /app
COPY diff2html-cli-master.zip  .
RUN unzip diff2html-cli-master.zip
COPY template.html .
WORKDIR /app/diff2html-cli-master
RUN yarn install
RUN yarn build
RUN pkg .



CMD ["diff2html","bash"]
