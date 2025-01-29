from flask import Flask, request, jsonify
import docker

app = Flask(__name__)

# Configurer l'URL de l'API Docker exposée sans TLS
DOCKER_API_URL = "http://host.docker.internal:2375"  # Utiliser 'host.docker.internal' si Flask tourne dans un conteneur Docker

# Initialisation du client Docker
client = docker.DockerClient(base_url=DOCKER_API_URL, tls=False)

@app.route('/')
def home():
    return "Bienvenue sur l'application Flask vulnérable aux attaques API Docker!"

@app.route('/vulnerable', methods=['POST'])
def execute_docker_command():
    # Récupérer la commande Docker envoyée dans la requête JSON
    data = request.get_json()
    command = data.get('command', '')

    if command:
        try:
            # Exemple : Exécution d'une commande 'ps' pour lister les conteneurs en cours d'exécution
            if command == "ps":
                containers = client.containers.list()
                container_info = [{"id": container.id, "name": container.name, "status": container.status} for container in containers]
                return jsonify({'result': container_info})
            else:
                return jsonify({'error': f'Command "{command}" not supported'}), 400
        except Exception as e:
            return jsonify({'error': str(e)}), 400
    return jsonify({'error': 'No command provided'}), 400

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
