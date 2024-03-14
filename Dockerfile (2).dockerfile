# Use Ubuntu as base image
FROM ubuntu

# Install required packages
RUN apt-get update && \
    apt-get install -y python3 python3-pip && \
    pip3 install pandas numpy seaborn matplotlib scikit-learn scipy

# Create directory and move dataset
RUN mkdir /home/doc-bd-a1/
COPY load.py /home/doc-bd-a1/
COPY reviews.csv /home/doc-bd-a1/
COPY dpre.py /home/doc-bd-a1/ 
COPY vis.py /home/doc-bd-a1/ 
COPY eda.py /home/doc-bd-a1/ 
COPY model.py /home/doc-bd-a1/ 
COPY final_in_container.sh /home/doc-bd-a1/

# Set working directory
WORKDIR /home/doc-bd-a1/

CMD ["python3", "/home/doc-bd-a1/load.py", "/home/doc-bd-a1/reviews.csv"]