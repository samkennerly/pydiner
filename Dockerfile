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

# Install project
COPY [".","."]
RUN pip install --editable .
ENV PATH="${WORKDIR}/bin:${PATH}"

CMD ["/bin/bash"]
