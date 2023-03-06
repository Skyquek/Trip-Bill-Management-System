set -eu pipefail

# Install python requirements.
tool/gh_codespaces/install_dependencies.sh

# Perform the migrations.
python mini-project/BillManagementSystem/manage.py makemigrations accounting
python mini-project/BillManagementSystem/manage.py migrate




