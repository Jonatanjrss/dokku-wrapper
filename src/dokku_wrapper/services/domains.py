from ..core.executor import run_command


class Domains:
    """Gerencia domínios."""

    @staticmethod
    def set_global(domain: str) -> bool:
        output = run_command(["dokku", "domains:set-global", domain])
        if output == "-----> Set localhost":
            return True
        return False
