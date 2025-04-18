## Commands to run the repo locally

- Before making any changes in local make sure local and remote are in sync

```
git fetch origin
git reset --hard origin/main
```

- To resolve git error "You have divergent branches and need to specify how to reconcile them."

```
git pull --rebase origin main
git push origin main

```

```
python3 -m venv myenv
source myenv/bin/activate
```

```
python3 -m pip install --upgrade pip
pip install -r requirements.txt
pip install "mkdocs-material[offline]"
pip install mkdocs-material mkdocs python-markdown-math mkdocs-mermaid2-plugin mkdocs-macros-plugin pyyaml
```

```
python3 scripts/gen_nav.py
```

```
mkdocs serve
mkdocs build
mkdocs build --clean
mkdocs build --verbose
```

- To make MkDocs site available to other computer on local network

```
mkdocs serve -a 0.0.0.0:8000
ifconfig | grep "inet " | grep -Fv 127.0.0.1 | awk '{print $2}'

mkdocs serve --dev-addr=0.0.0.0:8000
ifconfig | grep -E "([0-9]{1,3}\.){3}[0-9]{1,3}" | grep -v 127.0.0.1 | head -1 | awk '{ print $2 }'


192.168.x.x:8000
```

```
deactivate
rm -rf myenv
```
