FROM python:3.7.4
LABEL description="Python development sandbox"
LABEL maintainer="samkennerly@gmail.com"

# Install system packages
RUN apt-get -y update && apt-get -y install less tree vim

# Install Python packages
COPY ["requirements.txt", "/tmp/requirements.txt"]
RUN pip install --upgrade pip && pip install --requirement /tmp/requirements.txt

# Create project folder
ARG WORKDIR=/context
WORKDIR "${WORKDIR}"

# Find bin/ scripts and src/ code
ENV PATH="${WORKDIR}/bin:${PATH}" PYTHONPATH="${WORKDIR}/src"

# Copy repo files (unless .dockerignore)
COPY [".", "${WORKDIR}"]

CMD ["/bin/bash"]
