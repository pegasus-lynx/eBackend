psql: ### Starts PostgreSQL server
	@sudo systemctl start postgresql

migrations: ### Generates Django migrations.
	@echo "Creating migrations..."
	@python manage.py makemigrations
	@echo "Migrating..."
	@python manage.py migrate
	@echo "Done!"

server: ### Runs a local development server at http://0.0.0.0:8000
	@python manage.py runserver 0:8000

resetdb: ### Resets local PostgreSQL database.
	dropdb explo -U explo
	createdb explo -U explo
	@echo "Done!"

clean: ### Cleans up migrations.
	@echo "Cleaning..."
	@find . -path "*/migrations/*.py" -not -name "__init__.py" -delete
	@find . -path "*/*/*.pyc"  -delete
	@echo "Done!"