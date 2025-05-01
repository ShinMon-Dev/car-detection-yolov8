#!/bin/bash
echo "PORT from Render is: $PORT"
streamlit run app.py --server.port=$PORT --server.address=0.0.0.0
