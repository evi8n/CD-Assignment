cd /Users/evisi/Documents/Winc/random_quotes_app

source venv/Scripts/activate

git pull origin main

pip install -r requirements.txt

systemctl restart random_quotes_app.service

systemctl status random_quotes_app

set -e