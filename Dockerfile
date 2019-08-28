FROM python:3.7.4
LABEL description="Python development sandbox"
LABEL maintainer="samkennerly@gmail.com"

# Create project folder
ARG WORKDIR=/context
WORKDIR "${WORKDIR}"

# Install system packages
RUN apt-get -y update && \
    apt-get -y install gcc less tree vim zip

# Install Python packages
COPY ["requirements.txt","."]
RUN pip install --upgrade pip && \
    pip install --requirement requirements.txt

# Copy project files (use .dockerignore to exclude)
COPY [".","."]

# Use setup.py to install project packages
#COPY ["setup.py","."]
#RUN pip install --editable .

# Find src/ code and bin/ scripts
ENV PYTHONPATH="${WORKDIR}/src" \
    PATH="${WORKDIR}/bin:${PATH}"

CMD ["/bin/bash"]
