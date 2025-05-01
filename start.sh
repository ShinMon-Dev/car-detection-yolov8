#!/bin/bash
export PORT=${PORT:-8501}

# Check if the port is already in use
if lsof -i :$PORT > /dev/null; then
  echo "⚠️ Port $PORT already in use. Trying 8502..."
  export PORT=8502
fi

streamlit run app.py --server.port=$PORT --server.address=0.0.0.0
