rsync -av -e "ssh -i ~/dev/sintrafico/keys/map_matching.pem" --exclude '*.pyc' --exclude '.venv/' ./ ubuntu@54.198.176.54:~/dalle/
