from pathlib import Path

from dynaconf import Dynaconf

PATH_ROOT = Path(__file__).parent


settings = Dynaconf(
    envvar_prefix="SBF_GROUP",
    settings_files=["settings.toml", ".secrets.toml"],
    environments=True,
    env_switcher="SBF_ENVIRONMENT",
    includes=[f"{PATH_ROOT}/settings.toml", f"{PATH_ROOT}/.secret.toml"],
)
