from ..core.executor import run_command
from ..core.exceptions import AppAlreadyExists, AppNotFound, DokkuCommandError
from typing import List, Dict


class Apps:
    """Gerencia aplicações Dokku."""

    @staticmethod
    def create(name: str) -> Dict[str, str]:
        try:
            output = run_command(["dokku", "apps:create", name])
            return {"name": name, "message": output}
        except DokkuCommandError as e:
            if "already exists" in e.message:
                raise AppAlreadyExists(name)
            raise

    @staticmethod
    def destroy(name: str, force: bool = True) -> bool:
        cmd = ["dokku", "apps:destroy", name]
        if force:
            cmd.append("--force")
        try:
            if "Destroying myapp" in run_command(cmd):
                return True
        except DokkuCommandError as e:
            if "is not deployed" in e.message or "does not exist" in e.message:
                raise AppNotFound(name)
            raise
        return False

    @staticmethod
    def list() -> List[str]:
        """Retorna uma lista de apps Dokku existentes."""
        output = run_command(["dokku", "apps:list"])
        apps = [line.strip() for line in output.splitlines() if line.strip()]
        apps.remove('=====> My Apps')
        return apps
