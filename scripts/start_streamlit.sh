#!/bin/bash
cd /home/ec2-user/streamlit-app
pkill -f streamlit
nohup streamlit run app.py --server.port 8501 --server.enableCORS false &
