echo "We will now initialise the VENV"
python -m venv BT4014

echo "Now, we will activate the environment"
call BT4014\Scripts\activate

echo "And finally we will install the requirements"
pip install -r requirements.txt

echo "Done."
pause