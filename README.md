
# sync code
rsync -av -e "ssh -i ~/dev/sintrafico/keys/map_matching.pem" --exclude '*.pyc' --exclude './photos/*' --exclude '.venv/' ./ ubuntu@54.198.176.54:~/dalle/


# send photos
scp -i ~/dev/sintrafico/keys/map_matching.pem ./photos/*.png ubuntu@54.198.176.54:/home/ubuntu/dalle/photos/
