import json
import urllib.error
import urllib.request
from packaging import version


class UpdateError(Exception):
    pass


def maj(owner: str, repo: str, version_actuelle: str) -> dict:

    url = f"https://api.github.com/repos/{owner}/{repo}/releases/latest"
    headers = {"User-Agent": f"{repo}-Updater"}
    req = urllib.request.Request(url, headers=headers)

    try:
        with urllib.request.urlopen(req, timeout=10) as response:
            data = json.loads(response.read().decode("utf-8"))
    except urllib.error.URLError as e:
        raise UpdateError(f"Impossible de contacter GitHub : {e.reason}")
    except json.JSONDecodeError:
        raise UpdateError("Réponse GitHub invalide (JSON corrompu).")

    tag_name = data.get("tag_name", "").lstrip("v")
    html_url = data.get("html_url", "")

    last_v = version.parse(tag_name)
    v_actuelle = version.parse(version_actuelle)

    return {
        "update_available": last_v > v_actuelle,
        "latest_version": tag_name,
        "current_version": version_actuelle,
        "url": html_url
    }