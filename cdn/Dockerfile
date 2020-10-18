FROM node:10
RUN npm install light-server -g
ENV SERVE_PREFIX=/
ENV SERVE_PATH=/public
COPY ./src/run.sh /opt/run.sh
RUN chmod +x /opt/run.sh
EXPOSE 80
ENTRYPOINT [ "/opt/run.sh"]