#!/bin/bash

# Copy output files from container to local machine
docker cp bd-a1-container:/home/doc-bd-a1/res_dpre.csv "C:\Users\ohazz\OneDrive\Desktop\assigment_output/"
docker cp bd-a1-container:/home/doc-bd-a1/eda-in-1.txt "C:\Users\ohazz\OneDrive\Desktop\assigment_output/"
docker cp bd-a1-container:/home/doc-bd-a1/eda-in-2.txt "C:\Users\ohazz\OneDrive\Desktop\assigment_output/"
docker cp bd-a1-container:/home/doc-bd-a1/vis.png "C:\Users\ohazz\OneDrive\Desktop\assigment_output/"
docker cp bd-a1-container:/home/doc-bd-a1/k.txt "C:\Users\ohazz\OneDrive\Desktop\assigment_output/"

# Stop the container
docker stop bd-a1-container
