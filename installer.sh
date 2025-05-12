# 1. optional clean-up
###############################################################################
if [ "$1" == "clean" ]; then
  echo "Cleaning up Python virtual environment and repositories..."
  rm -rf mcp_env ag2
  echo "Clean operation completed."
  exit 0
fi


python3 -m venv mcp_env
source mcp_env/bin/activate
git clone https://github.com/ag2ai/ag2.git
cd ag2
pip install -e .[gemini,mcp,openai,anthropic]
cd ..
pip install ipykernel
pip install -U jupyterlab notebook ipywidgets
python -m ipykernel install --user --name mcp_env --display-name "mcp_env"

