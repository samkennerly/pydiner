FROM python:3.7.4
LABEL description="Python development sandbox"
LABEL maintainer="samkennerly@gmail.com"

# Create project folder
ARG WORKDIR=/context
WORKDIR "${WORKDIR}"

# Install system packages
RUN apt-get -y update && apt-get -y install less tree zip

# Install Python packages
COPY ["requirements.txt", "."]
RUN pip install --upgrade pip && pip install --requirement requirements.txt

# Find src/ code and bin/ scripts
ENV PYTHONPATH="${WORKDIR}/src" \
    PATH="${WORKDIR}/bin:${PATH}"

# Copy repo files (unless .dockerignore)
COPY [".", "${WORKDIR}"]

CMD ["/bin/bash"]
