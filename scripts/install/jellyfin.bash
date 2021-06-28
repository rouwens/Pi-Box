apt install apt-transport-https -y
wget -O - https://repo.jellyfin.org/jellyfin_team.gpg.key | apt-key add -
echo "deb [arch=$( dpkg --print-architecture ) trusted=yes] https://repo.jellyfin.org/$( awk -F'=' '/^ID=/{ print $NF }' /etc/os-release ) $( awk -F'=' '/^VERSION_CODENAME=/{ print $NF }' /etc/os-release ) main" | sudo tee /etc/apt/sources.list.d/jellyfin.list
apt update
apt install jellyfin -u
