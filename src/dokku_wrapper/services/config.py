import re
from typing import List, Dict

from ..core.executor import run_command


class Config:
    """Gerencia domínios."""

    @staticmethod
    def set(app, key, value) -> bool:
        output = run_command(["dokku", "config:set", app, f"{key}={value}"])
        if "Setting config vars" in output:
            return True
        return False

    @staticmethod
    def list(app) -> List[Dict]:
        """Retorna uma lista de apps Dokku existentes."""
        output = run_command(["dokku", "config", app])
        return [{i[0].strip(): i[1].strip()} for i in re.findall(r"(.*?):(.*)", output)]
