FROM python:3.9-alpine
WORKDIR /app
RUN apk update && apk add --no-cache coreutils
RUN pip install mpmath sympy
CMD ["sh", "-c", "./tests/${part}/runner.sh"]
