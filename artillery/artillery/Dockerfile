:QFROM node:10-alpine

RUN npm install --ignore-scripts -g artillery
RUN npm install -g artillery-plugin-influxdb

COPY test-scenario.yaml .

RUN apk add curl

ENTRYPOINT [ "artillery", "run", "test-scenario.yaml" ]

