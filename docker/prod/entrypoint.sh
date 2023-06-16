python manage.py flush --no-input
echo "Database flushed successfully"

python manage.py migrate
echo "If any required, migrations process has been run"

python manage.py collectstatic --no-input --clear
echo "Static files has successfully been collected"

python manage.py createsuperuser --no-input

exec "$@"