# Use a imagem base oficial do Python (versão 3.11) como base para o Anaconda
FROM python:3.11-buster as base

# Defina variáveis de ambiente para o Anaconda
ENV CONDA_VERSION=23.5.2
ENV CONDA_DIR=/opt/conda

# Instale o Anaconda
RUN apt-get update && \
    apt-get install -y wget bzip2 software-properties-common && \
    apt-get install -y openjdk-11-jre && \
    wget https://repo.anaconda.com/archive/Anaconda3-2024.06-1-Linux-x86_64.sh -O /tmp/anaconda.sh && \
    /bin/bash /tmp/anaconda.sh -b -p ${CONDA_DIR} && \
    rm /tmp/anaconda.sh && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Configure o PATH para o Anaconda
ENV PATH="${CONDA_DIR}/bin:${PATH}"

# Instale o Python 3.12 através do Conda
RUN conda install -y python=3.12

# Crie um usuário não root
RUN useradd -ms /bin/bash nonrootuser

# Mude para o usuário não root
USER nonrootuser

# Defina o diretório de trabalho
WORKDIR /home/nonrootuser

# Exponha a porta 8000 (opcional, se for relevante para seu uso)
EXPOSE 8000

# Comando de entrada padrão
CMD [ "python3.11", "--version" ]