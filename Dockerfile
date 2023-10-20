FROM python:3.12.0
LABEL description="Python development sandbox"
LABEL maintainer="samkennerly@gmail.com"

# Install system packages
RUN apt-get -y update && apt-get -y install less tree vim

# Install Python packages
COPY requirements.txt /tmp
RUN pip install --upgrade pip && pip install --requirement /tmp/requirements.txt

# Ensure that Python can find the files in this repo
COPY [".", "/context"]
ENV PATH="/context/bin:${PATH}" PYTHONPATH="/context/src"

WORKDIR '/context'
CMD ["/bin/bash"]
