FROM arm64v8/ubuntu


COPY qemu-aarch64-static /usr/bin


RUN apt-get update && \
    apt-get install -y python3 python3-pip libgl1-mesa-glx libglib2.0-0 && \
    rm -rf /var/lib/apt/lists/*


COPY requirements.txt ./
RUN pip install -r requirements.txt

COPY . .

EXPOSE 9000
