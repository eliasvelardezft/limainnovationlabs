conda create -n limaenv python -y
conda activate limaenv
pip install -r requirements.txt
psql postgres -c "CREATE DATABASE limadb;"
psql postgres -c "CREATE USER limauser;"
psql postgres -c "ALTER USER pedrouser WITH ENCRYPTED PASSWORD 'limapassword';"
psql postgres -c "GRANT ALL PRIVILEGES ON DATABASE limadb TO limauser;"
python manage.py makemigrations 
python manage.py migrate
echo "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.create_superuser('maria', 'martinez', 'mmartinez', 'mmartinez')" | python manage.py shell
cd data
python fill.py
cd ..
python manage.py runserver