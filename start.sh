echo "🔍 Validating model..."
python scripts/validate_model.py

if [ $? -eq 0 ]; then
  echo "🚀 Starting API server..."
  fastapi dev main.py
else
  echo "🛑 Model validation failed. Server not started."
fi
